#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    https://shiny.posit.co/
#

library(shiny)
library(ggplot2)
library(dplyr)
library(DBI)
library(RPostgres)
library(tidyr)

sidebarPanel(
  actionButton("select_all", "Select All Counties"),
  selectInput("selected_counties", "Select Counties:", choices = NULL, multiple = TRUE)
)

server <- function(input, output, session) {
  
  # Connect to PostgreSQL database
  con <- dbConnect(
    RPostgres::Postgres(),
    dbname   = "food",
    host     = "127.0.0.1",
    port     = 5432,
    user     = "postgres",
    password = "life123$"
  )
  
  # Retrieve county names for dropdown
  counties <- dbGetQuery(con, "SELECT DISTINCT \"County_Name\" FROM \"Texas_Counties\"")
  updateSelectInput(session, "selected_counties", choices = counties$County_Name)
  
  # Observe "Select All" button click
  observeEvent(input$select_all, {
    updateSelectInput(session, "selected_counties", selected = counties$County_Name)
  })
  
  # Fetch filtered data based on selection
  county_data <- reactive({
    req(input$selected_counties)
    query <- sprintf("SELECT * FROM \"Texas_Counties\" WHERE \"County_Name\" IN ('%s')",
                     paste(input$selected_counties, collapse = "', '"))
    
    dbGetQuery(con, query) %>%
      pivot_longer(cols = c("2019", "2020", "2021", "2022"), 
                   names_to = "Year", values_to = "Food_Insecurity") %>%
      mutate(Year = as.numeric(Year))
  })
  
  # Render line plot
  output$insecurityPlot <- renderPlot({
    data <- county_data()
    
    ggplot(data, aes(x = Year, y = Food_Insecurity, color = County_Name)) +
      geom_line(size = 1) +
      geom_point(size = 2) +
      labs(title = "Food Insecurity Rates Over Time",
           x = "Year", y = "Food Insecurity (%)") +
      theme_minimal()
  })
  
  # Close DB connection when session ends
  session$onSessionEnded(function() {
    dbDisconnect(con)
  })
}


# Run the application 
shinyApp(ui = ui, server = server)
