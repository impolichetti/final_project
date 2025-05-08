# final_project
marriage dataset

## Data Source
- The data used in this project is sourced from a CSV file containing information about divorce rates, income levels, and other demographic variables. Specifically, the file includes divorce rates for two age groups (35-44 and 45-54 years old) across different income levels (poor, middle class, and rich) and education levels (higschool, some college, bachelors only, bachelors or more, and graduate degree).
- The data spans the years 1960-2012.

## Transformation Steps
- **Data Cleaning**: 
  - Missing values are filled with 0 to prevent issues with calculations.
  - Irrelevant or unnecessary columns are removed, and only relevant data is retained.
  
- **Data Aggregation**: 
  - For each age group (35-44 and 45-54), data points for poor, middle, and rich income categories are summed to create new columns for combined data across both age groups.
  - The resulting combined columns include: `poor_all`, `mid_all`, `rich_all`, `HS_all`, `SC_all`, `BAp_all`, `BAo_all`, and `GD_all`.

- **Data Insertion**: 
  - After the transformations, the data is inserted into a SQLite database to be served by a Flask web application.

## Destination
- The processed data is stored in a **SQLite database**, named `data.db`. This database contains a table called `DivorceData` where each row corresponds to one record of transformed data for a given year.
- The data is then accessed by a Flask web application to render dynamic visualizations (such as line graphs) that show trends over time.

## Automation
- **Flask Web Application**: 
  - The pipeline is automated as part of a Flask web application, which serves the transformed data through a REST API and renders visualizations in a web browser.
  - The data processing and insertion into the database are done programmatically by the Flask application at the start of the server.

- **Plotting and Visualization**: 
  - The pipeline also includes automation for generating line graphs that show divorce rates over time for different income groups. This visualization is generated dynamically every time the Flask application is loaded.
  
