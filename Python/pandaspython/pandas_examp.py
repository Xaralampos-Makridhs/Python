import pandas as pd

# Define the data in a dictionary
data = {
    'Store_ID': [1, 2, 1, 3, 2, 1, 3],  # Store IDs
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02', '2023-01-03', '2023-01-02'],  # Dates of sales
    'Product': ['Laptop', 'Phone', 'Laptop', 'Tablet', 'Phone', 'Laptop', 'Tablet'],  # Products sold
    'Quantity': [2, 5, 3, 10, 3, 1, 7],  # Quantity sold
    'Price': [1000, 500, 1000, 300, 500, 1000, 300]  # Price of each product
}

# Create a DataFrame from the data dictionary
df = pd.DataFrame(data)

# Print the entire DataFrame
print(df)

# Print the first 5 rows of the DataFrame
print(df.head(5))

# Add a new column 'Total_Sales' by multiplying Quantity and Price
df['Total_Sales'] = df['Quantity'] * df['Price']

# Calculate total sales per store by grouping by 'Store_ID' and summing 'Total_Sales'
total_sales = df.groupby('Store_ID')['Total_Sales'].sum()
print(total_sales)

# Calculate total sales per day by grouping by 'Date' and summing 'Total_Sales'
sales_per_day = df.groupby('Date')['Total_Sales'].sum()
print(sales_per_day)

# Calculate total sales per product by grouping by 'Product' and summing 'Total_Sales'
sales_per_product = df.groupby('Product')['Total_Sales'].sum()
print(sales_per_product)

# Display basic analytic stats (mean, min, max) for the 'Quantity' and 'Price' columns
print(df[['Quantity', 'Price']].describe())

# Find the product with the most sales by first finding the maximum sales amount
max_sales_product = sales_per_product.max()

# Use the max sales value to find the product name that corresponds to this value
top_product = sales_per_product[sales_per_product == max_sales_product].index[0]
print(f'Προϊόν με τις περισσότερες πωλήσεις: {top_product}')
