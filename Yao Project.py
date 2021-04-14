import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
supermarket_sales = pd.read_csv (r'C:\Users\maggie\Desktop\Python\Project\supermarket_sales - Sheet1.csv')
print(supermarket_sales.head())
print(supermarket_sales.info())

supermarket_city = supermarket_sales[["City",'Branch']]
print(supermarket_city)
supermarket_city =supermarket_city.drop_duplicates(subset=["City"])
print(supermarket_city)

print(supermarket_sales.isna().any())

print(supermarket_sales.sort_values('Total', ascending = False).head().to_string())

supermarket_Yangon=supermarket_sales[supermarket_sales["City"]=="Yangon"]
print(supermarket_Yangon.info())
print(supermarket_Yangon.groupby('Product line')["Quantity"].agg([min,max,sum]))

supermarket_Mandalay=supermarket_sales[supermarket_sales["City"] == "Mandalay"]
print(supermarket_Mandalay.info())
print(supermarket_Mandalay.groupby('Product line')["Quantity"].agg([min,max,sum]))

supermarket_Naypyitaw=supermarket_sales[supermarket_sales["City"] == "Naypyitaw"]
print(supermarket_Mandalay.info())
print(supermarket_Naypyitaw.groupby('Product line')["Quantity"].agg([min,max,sum]))

data = [['Yangon','322','263','313','257','371',333],
        ['Mandalay','316','297','270','320','295',322],
        ['Naypyitaw','333','342','369','277','245','265']]
columns = ['City','Electronic accessories','Fashion accessories','Food and beverages','Health and beauty','Home and lifestyle','Sports and travel']
supermarket_quantity = pd.DataFrame(data=data, columns=columns)
print(supermarket_quantity.to_string())

