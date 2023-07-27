import pandas as pd

# Read the dataset from the CSV file
df = pd.read_csv('C:/Users/jalaj/VsCodeLiter/PYs/terrorism_eda/globalterrorismdb_0718dist.csv', encoding='latin1')

# Display the first few rows of the dataset
print(df.head())

# Get information about the dataset
print(df.info())

# Check statistical summary of numeric columns
print(df.describe())

# Explore the countries with the most terrorist incidents
top_countries = df['country_txt'].value_counts().head(10)
print("Top 10 Countries with the Most Terrorist Incidents:")
print(top_countries)

# Explore the regions with the most terrorist incidents
top_regions = df['region_txt'].value_counts().head(5)
print("Top 5 Regions with the Most Terrorist Incidents:")
print(top_regions)

# Explore the cities with the most terrorist incidents
top_cities = df['city'].value_counts().head(10)
print("Top 10 Cities with the Most Terrorist Incidents:")
print(top_cities)

# Explore the attack types
attack_types = df['attacktype1_txt'].value_counts()
print("Attack Types:")
print(attack_types)

# Visualize the hot zones on a map using latitude and longitude
import matplotlib.pyplot as plt

# Filter out records with missing latitude or longitude
filtered_df = df[(df['latitude'].notnull()) & (df['longitude'].notnull())]

# Create a scatter plot of terrorist incidents
plt.figure(figsize=(12, 8))
plt.scatter(filtered_df['longitude'], filtered_df['latitude'], alpha=0.5, marker='.')
plt.title('Hot Zones of Terrorism')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
