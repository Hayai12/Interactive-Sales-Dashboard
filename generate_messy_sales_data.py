import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

num_records = 1000

# Generate initial clean data
data = {
    "Order ID": [f"ORD-{i+1:05d}" for i in range(num_records)],
    "Order Date": pd.date_range(start="2023-01-01", periods=num_records, freq='D'),
    "Customer Name": [fake.name() for _ in range(num_records)],
    "Product": np.random.choice(["Laptop", "Smartphone", "Tablet"], num_records),
    "Region": np.random.choice(["North America", "Europe", "Asia", "South America"], num_records),
    "Salesperson": [fake.name() for _ in range(num_records)],
    "Quantity": np.random.randint(1, 20, num_records),
    "Unit Price": np.round(np.random.uniform(50, 1000, num_records), 2),
}

df = pd.DataFrame(data)

# Intentionally introduce messiness:
for col in ["Product", "Region", "Quantity", "Unit Price"]:
    df.loc[df.sample(frac=0.05).index, col] = None

# Intentionally add duplicates (around 2%)
duplicates_df = df.sample(frac=0.02)
df = pd.concat([df, duplicates_df], ignore_index=True)

# Calculate Sales Amount with care for missing values
df["Sales Amount"] = df["Quantity"] * df["Unit Price"]

# Create Order ID and Date
df["Order ID"] = [f"ORD-{i+1:05d}" for i in range(len(df))]
df["Order Date"] = pd.date_range(start="2023-01-01", periods=len(df), freq='D')

# Save messy data
df.to_csv("messy_sales_data.csv", index=False)

print("Messy data generated successfully in messy_sales_data.csv")
