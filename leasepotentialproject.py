#Creating a dataframe

import pandas as pd   # importing library
file_path = "C://Users/SINDHU/Desktop/Python Exercise Data.xlsx"    # loading the data from an excel file

df =pd.read_excel(file_path)       #reading the file from an excel file

print(df.head())   #Display the first few rows of the Dataframe





# Extract State from Site No column by removing US and XXXX, and create a State column

df['state'] = df['Site No'].str.replace(r'US-', '', regex=True).str.replace(r'-\d{4}', '', regex=True)

print(df[['Site No', 'state']].head())  # Display the Site Number and state columns





# The column for start date is named 'Date Start' and site type is 'Site Type'
filtered_df = df[(df['Date Start'].notna()) & (df['Site Type'] != 'TWR-IP')]

# Creating a summary table counting the number of sites for each site type
summary_table = filtered_df['Site Type'].value_counts().reset_index()
summary_table.columns = ['Site Type', 'Number of Sites']

print(summary_table)  # Display the summary table





#Creating a Multiline Graph
import matplotlib.pyplot as plt

# 'Year Built' and 'Overall Structure Height (AGL)' columns
# Group by 'Year Built' and 'Site Type' and calculate the average height
average_height = filtered_df.groupby(['Year Built', 'Site Type'])['Overall Structure Height (AGL)'].mean().reset_index()

# Create a multiline graph
plt.figure(figsize=(12, 6))
for site_type in average_height['Site Type'].unique():
    subset = average_height[average_height['Site Type'] == site_type]
    plt.plot(subset['Year Built'], subset['Overall Structure Height (AGL)'], marker='o', label=site_type)

plt.title('Average Overall Structure Height (AGL) by Year Built and Site Type')
plt.xlabel('Year Built')
plt.ylabel('Average Overall Structure Height (AGL)')
plt.legend()
plt.grid()
plt.show()














