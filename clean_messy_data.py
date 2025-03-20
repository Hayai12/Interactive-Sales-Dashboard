import pandas as pd

# Load messy data
df = pd.read_csv("messy_sales_data.csv")
initial_rows = len(df)

print("=== Initial Data Overview ===")
print(f"Total Rows: {initial_rows}")
print("Missing Values by Column:\n", df.isnull().sum())
print("Duplicate Rows:", df.duplicated().sum())
print("=" * 40)

# Step 1: Remove duplicate rows
num_duplicates = df.duplicated().sum()
if num_duplicates > 0:
    df.drop_duplicates(inplace=True)
    print(f"Removed {num_duplicates} duplicate rows.")
else:
    print("No duplicate rows found.")
print("=" * 40)

# Step 2: Remove rows missing essential values
essential_cols = ["Product", "Quantity", "Unit Price"]
missing_essential = df[essential_cols].isnull().sum()
print("Missing values in essential columns BEFORE dropping rows:")
print(missing_essential)
rows_before = len(df)
df.dropna(subset=essential_cols, inplace=True)
rows_after = len(df)
print(f"Dropped {rows_before - rows_after} rows due to missing essential fields.")
print("=" * 40)

# Step 3: Fill missing values in non-essential columns
missing_region_before = df["Region"].isnull().sum()
df["Region"].fillna("Unknown Region", inplace=True)
missing_region_after = df["Region"].isnull().sum()
print(f"Filled {missing_region_before - missing_region_after} missing 'Region' values with 'Unknown Region'.")
print("=" * 40)

# Step 4: Recalculate the Sales Amount column
df["Sales Amount"] = df["Quantity"] * df["Unit Price"]
print("Recalculated 'Sales Amount' column.")
print("=" * 40)

# Step 5: Convert Order Date and add Month and Year columns
df["Order Date"] = pd.to_datetime(df["Order Date"], errors='coerce')
df["Month"] = df["Order Date"].dt.month_name()
df["Year"] = df["Order Date"].dt.year
print("Converted 'Order Date' to datetime and added 'Month' and 'Year' columns.")
print("=" * 40)

# Final overview and saving the cleaned dataset
final_rows = len(df)
print("=== Final Data Overview ===")
print(f"Total Rows after cleaning: {final_rows}")
print("Missing Values by Column:\n", df.isnull().sum())
df.to_csv("cleaned_sales_data.csv", index=False)
print("Cleaned data saved to 'cleaned_sales_data.csv'.")
