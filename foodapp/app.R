library(shiny)
library(ggplot2)
library(readr)
library(dplyr)
library(tidyr)

# Load CSV file
food_data <- read_csv("Food Insecurity Dataset.csv", show_col_types = FALSE)

# Reshape data for plotting
food_data_long <- pivot_longer(food_data, cols = c("2019", "2020", "2021", "2022"), 
                               names_to = "year", values_to = "food_insecurity")

# Filter out any potential NA values in county names
valid_counties <- food_data_long %>%
  filter(!is.na(`County Name`)) %>%
  pull(`County Name`) %>% unique()

# UI
ui <- fluidPage(
  titlePanel("Food Insecurity in Texas Counties"),
  
  sidebarLayout(
    sidebarPanel(
      actionButton("select_all", "Select All Counties"),  # Button to select all
      actionButton("clear_all", "Clear All Counties"),    # Button to clear selection
      
      checkboxGroupInput("selected_counties", "Select Counties:", 
                         choices = valid_counties, 
                         selected = valid_counties),  # Removes NA
      
      sliderInput("selected_years", "Select Year Range:", 
                  min = 2019, max = 2022, value = c(2019, 2022), step = 1, sep = "")
    ),
    
    mainPanel(
      plotOutput("linePlot")
    )
  )
)

# Server
server <- function(input, output, session) {
  
  # Update selection based on button clicks
  observeEvent(input$select_all, {
    updateCheckboxGroupInput(session, "selected_counties",
                             choices = valid_counties,
                             selected = valid_counties)
  })
  
  observeEvent(input$clear_all, {
    updateCheckboxGroupInput(session, "selected_counties", choices = valid_counties, selected = NULL)
  })
  
  # Filter data based on user selection
  filtered_data <- reactive({
    food_data_long %>%
      filter(`County Name` %in% input$selected_counties,
             as.numeric(year) >= input$selected_years[1],
             as.numeric(year) <= input$selected_years[2])
  })
  
  output$linePlot <- renderPlot({
    # Get the last selected year dynamically
    latest_year <- max(as.numeric(input$selected_years))  
    
    ggplot(filtered_data(), aes(x = as.numeric(year), y = food_insecurity, color = `County Name`)) +
      geom_line(linewidth = 1) +
      geom_point(size = 2) +
      geom_text(data = filtered_data() %>% filter(year == latest_year),  # Label at last selected year
                aes(label = `County Name`), hjust = -0.2, size = 3, check_overlap = TRUE) +
      labs(title = "Food Insecurity Trends in Texas Counties",
           x = "Year", y = "Food Insecurity (%)",
           color = "County") +
      theme_minimal() +
      theme(
        legend.position = "bottom",  # Moves legend below the graph
        legend.title = element_blank(),  # Removes legend title
        legend.text = element_text(size = 10)  # Adjust legend text size
      )
  })
}

# Run the app
shinyApp(ui = ui, server = server)
