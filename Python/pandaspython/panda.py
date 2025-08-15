#Pandas
import pandas as pd 

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alex', 'George', 'Mary'],
    'Age': [24, 22, 25],
    'City': ['Thessaloniki', 'Athens', 'Patra'],
}

# Create DataFrame
df = pd.DataFrame(data)
print(df)

print('--------------------------------------------')

# If you want to insert a .csv file
df = pd.read_csv('./Breast_cancer_dataset.csv')  # Make sure the path is correct

print('--------------------------------------------')

# Prints the first 5 rows from the CSV
print(df.head(5))

print('--------------------------------------------')

# Prints the last 5 rows from the CSV
print(df.tail(5))

print('--------------------------------------------')

# Prints the dimensions of the DataFrame (rows, columns)
print(df.shape)

print('--------------------------------------------')

# Prints the labels (column names) of the DataFrame
print(df.columns)

print('--------------------------------------------')

# Print data types of each column
print(df.dtypes)

print('--------------------------------------------')

# Access a specific column (e.g., 'diagnosis')
dg = df['diagnosis']
print(diag)

print('--------------------------------------------')

# Access more than one column
twocolumns = df[['diagnosis', 'radius_mean']]
print(twocolumns)

print('--------------------------------------------')

# Filter data based on a condition (e.g., radius_mean > 20)
filtered = df[df['radius_mean'] > 20]
print(filtered)

print('--------------------------------------------')

# Access data in rows and columns using integer indices
access = df.iloc[4, 3]  # Access value in the 5th row, 4th column
print(access)

print('--------------------------------------------')

# Access data in rows and columns using labels
label_access = df.loc[0, 'diagnosis']  # Access value in row 0, 'diagnosis' column
print(label_access)

print('--------------------------------------------')

# Add a new column to the DataFrame
df['name_column'] = ['etc', 'etc', 'etc']  # Adding 'name_column' with values
print(df)

print('--------------------------------------------')

# Delete a column
df.drop(columns=['name_column'], inplace=True)  # Delete 'name_column'
print(df)

print('--------------------------------------------')

# Sort by a specific column (e.g., 'diagnosis')
df.sort_values('diagnosis')  # Sort by 'diagnosis' column
print(df)

print('--------------------------------------------')

# Sort by a specific column in descending order
df.sort_values('diagnosis', ascending=False)  # Sort by 'diagnosis' in descending order
print(df)

print('--------------------------------------------')

# Filter with a query (e.g., diagnosis > 20)
df.query('diagnosis > 20')  # Query to filter rows where 'diagnosis' > 20
print(df)

print('--------------------------------------------')

# Describe the statistics of the DataFrame
print(df.describe())

print('--------------------------------------------')

# Prints the unique values and their frequencies in a column (useful for categorical data)
print(df['diagnosis'].value_counts())  # Example with 'diagnosis' column

print('--------------------------------------------')

# Returns a DataFrame with boolean values for the empty cells
print(df.isnull())  # Boolean DataFrame indicating where the values are missing

print('--------------------------------------------')

#Group by
df.groupby('column_name'): Grouping data based on the column.
df.groupby('column_name').agg({'column_name': 'mean'}): #Calculating the mean for the grouped column.


# Drops rows with empty cells (NaN)
df.dropna(inplace=True)  # Remove rows that contain NaN values
print(df)

print('--------------------------------------------')

# Replace empty values (NaN) with a specified value
df.fillna(value='Unknown', inplace=True)  # Replace NaN with 'Unknown'
print(df)

print('--------------------------------------------')

# Merge two datasets (example with df2, which doesn't exist here)
# df.merge(df2, on='common_column')  # Combine two datasets on a common column
# This will throw an error since df2 is not defined in the current code.

# Uncomment the next lines if df2 exists:
# print(df)

print('--------------------------------------------')

# Combine two datasets vertically (example with df2, which doesn't exist here)
# pd.concat([df, df2])  # Concatenate two DataFrames
# This will throw an error since df2 is not defined in the current code.

#You can find this .csv dataset in the Kaggle
#https://www.kaggle.com/datasets



