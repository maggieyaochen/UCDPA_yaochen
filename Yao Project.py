import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Importing dataset : supermarket_sales - Sheet1.csv
supermarket_sales = pd.read_csv('supermarket_sales - Sheet1.csv')
print(supermarket_sales.head())
print(supermarket_sales.info())

# Using dropping duplicates to check branches and cities
supermarket_city = supermarket_sales[["City",'Branch']]
print(supermarket_city)
supermarket_city =supermarket_city.drop_duplicates(subset=["City"])
print(supermarket_city)

# To check if there is any missing value in the file
print(supermarket_sales.isna().any())

# Sorting Sales Totals by descending values to find out top 5 highest sales.
print(supermarket_sales.sort_values('Total', ascending = False).head().to_string())

# Grouping the product line to see sales quantities in each city to find out min, max and sum
supermarket_Yangon=supermarket_sales[supermarket_sales["City"]=="Yangon"]
print(supermarket_Yangon.info())
print(supermarket_Yangon.groupby('Product line')["Quantity"].agg([min,max,sum]))

supermarket_Mandalay=supermarket_sales[supermarket_sales["City"] == "Mandalay"]
print(supermarket_Mandalay.info())
print(supermarket_Mandalay.groupby('Product line')["Quantity"].agg([min,max,sum]))

supermarket_Naypyitaw=supermarket_sales[supermarket_sales["City"] == "Naypyitaw"]
print(supermarket_Mandalay.info())
print(supermarket_Naypyitaw.groupby('Product line')["Quantity"].agg([min,max,sum]))

print(supermarket_sales.groupby('Product line')["Quantity"].agg([min,max,sum]))

# Create a new list of dicts to visualize the data
data = [['Yangon','322','263','313','257','371','333'],
        ['Mandalay','316','297','270','320','295','322'],
        ['Naypyitaw','333','342','369','277','245','265'],
        ['City Total','971','902','952','854','911','920']]
columns = ['City','Electronic accessories','Fashion accessories','Food and beverages','Health and beauty','Home and lifestyle','Sports and travel']
supermarket_quantity = pd.DataFrame(data=data, columns=columns)
print(supermarket_quantity.to_string())

print(supermarket_quantity.reset_index())

supermarket_quantity.reset_index().plot(
    x="City",y=['Electronic accessories','Fashion accessories','Food and beverages','Health and beauty','Home and lifestyle','Sports and travel'], kind="bar"
)
plt.title("Product Type Sales")
plt.xlabel("City")
plt.ylabel("Quantities")