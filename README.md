# Sales Data Cleaning and Dashboard Project

## Project Overview
This project involves generating messy sales data, cleaning it, and creating a dashboard to visualize key business metrics. The goal is to simulate real-world data issues, apply data cleaning techniques, and present insights through a visually appealing dashboard.

## Features
- **Messy Data Generation**: Creates synthetic sales data with missing values, duplicates, and inconsistencies.
- **Data Cleaning**: Processes and cleans the messy dataset to make it suitable for analysis.
- **Dashboard Creation**: Generates key business metrics and visualizations.

## Project Structure
```
📂 Sales-Data-Cleaning-Dashboard
├── 📄 generate_messy_sales_data.py   # Script to generate messy sales data
├── 📄 messy_sales_data.csv           # Generated messy data
├── 📄 clean_messy_data.py            # Script to clean messy data
├── 📄 cleaned_sales_data.csv         # Cleaned dataset
├── 📂 Dashboard                      # Folder containing PowerBI Dashboard
│   ├── 📄 Interactive_Sales_Dashboard.pbix  # PowerBI Interactive Dashboard
├── 📄 dashboard.png                  # Snapshot of the final dashboard
├── 📄 README.md                      # Documentation
```

## Getting Started

### Prerequisites
Ensure you have Python installed along with the required libraries:
```bash
pip install pandas numpy faker
```

### Running the Project

1. **Generate Messy Data**  
   Run the following command to generate a dataset with errors:
   ```bash
   python generate_messy_sales_data.py
   ```
   This creates `messy_sales_data.csv`.

2. **Clean the Data**  
   Run the cleaning script to remove duplicates, handle missing values, and correct inconsistencies:
   ```bash
   python clean_messy_data.py
   ```
   The cleaned data is saved as `cleaned_sales_data.csv`.

3. **Analyze and Visualize**  
   Use `cleaned_sales_data.csv` to create visualizations and dashboards.

## Dashboard
The dashboard visualizes:
- Monthly sales trends
- Revenue breakdown by product
- Sales distribution by region
- Profit margin and growth

The dashboard was built in **Power BI** and is available in the `Dashboard` folder as `Interactive_Sales_Dashboard.pbix`.

## Contribution
Feel free to contribute by improving the data cleaning process, adding new visualizations, or enhancing the dashboard.
