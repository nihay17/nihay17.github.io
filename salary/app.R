library(shiny)
library(DBI)
library(RPostgres)
library(ggplot2)

# Define the User Interface (UI)
ui <- fluidPage(
  titlePanel("EPPS6354 Shiny workshop 1: University Database - Instructor Salaries"),
  mainPanel(
    plotOutput("salaryPlot")
  )
)

# Define the Server Logic
server <- function(input, output, session) {
  
  # Establish connection to the PostgreSQL database
  con <- dbConnect(
    RPostgres::Postgres(),
    dbname   = "university",   # Adjust if your database name differs
    host     = "localhost",
    port     = 5432,           # Default PostgreSQL port
    user     = "postgres",     # Your PostgreSQL username
    password = "life123$" # Your PostgreSQL password
  )
  
  # Ensure the database connection is closed when the session ends
  session$onSessionEnded(function() {
    dbDisconnect(con)
  })
  
  # Reactive expression to fetch average salary by department, sorted high to low
  instructor_data <- reactive({
    query <- "SELECT dept_name, AVG(salary) AS avg_salary 
              FROM instructor 
              GROUP BY dept_name 
              ORDER BY avg_salary DESC;"
    dbGetQuery(con, query)
  })
  
  # Render the plot for average instructor salary by department
  output$salaryPlot <- renderPlot({
    data <- instructor_data()
    
    ggplot(data, aes(x = reorder(dept_name, -avg_salary), y = avg_salary)) +
      geom_bar(stat = "identity", fill = "steelblue") +
      theme_minimal() +
      labs(
        title = "Average Instructor Salary by Department",
        x = "Department",
        y = "Average Salary"
      ) +
      theme(
        axis.text.x = element_text(angle = 90, hjust = 1),
        text = element_text(family = "Palatino")
      )
  })
}

# Run the Shiny application
shinyApp(ui = ui, server = server)
