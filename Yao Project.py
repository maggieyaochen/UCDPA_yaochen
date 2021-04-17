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
data = [['Yangon',322,263,313,257,371,333],
        ['Mandalay',316,297,270,320,295,322],
        ['Naypyitaw',333,342,369,277,245,265],
        ['City Total',971,902,952,854,911,920]]
columns = ['City','Electronic accessories','Fashion accessories','Food and beverages','Health and beauty','Home and lifestyle','Sports and travel']
supermarket_quantity = pd.DataFrame(data=data, columns=columns)
print(supermarket_quantity.to_string())

print(supermarket_quantity.info())

# To view supermarket_quantity in a bar chart
supermarket_quantity.plot(
    x="City", y=['Electronic accessories','Fashion accessories','Food and beverages','Health and beauty','Home and lifestyle','Sports and travel'], kind="bar",
)
plt.xticks(rotation = 360)
plt.title("Product Line")
plt.xlabel("City")
plt.ylabel("Quantities")


# To view gross income by gender
print(supermarket_sales.head())
supermarket_gender=supermarket_sales.groupby("Gender")["gross income"].sum()
print(supermarket_gender)

Total_gross_income=7994+7384
Female=7994/Total_gross_income
Male=7384/Total_gross_income
print(Female)
print(Male)

# To view gross income by gender and product line
supermarket_gender=supermarket_sales.groupby(["Gender","Product line"])["gross income"].sum()
print(supermarket_gender)

supermarket_product=supermarket_sales.groupby(["Product line"])["gross income"].sum()
print(supermarket_product)

# To view gross income % by gender for each product line
supermarket_gender=pd.DataFrame({
    "Female":[1290,1449,1579,883,1430,1360],
    "Male":[1296,1136,1093,1458,1134,1364],

    }, index=['Electronic accessories','Fashion accessories','Food and beverages','Health and beauty','Home and lifestyle','Sports and travel']
)
print(supermarket_gender)
print(supermarket_gender.info())

stacked_data = supermarket_gender.apply(lambda x: x*100/sum(x), axis=1)
stacked_data.plot(kind="bar", stacked=True)
plt.title("Gross income % by Gender for each product line")
plt.xlabel("Product line")
plt.ylabel("Percentage of Gross income (%)")
plt.xticks(rotation = 360)
plt.show()

Total_grossincome = [2587,2585,2673,2342,2564,2624]

my_labels = 'Electronic accessories','Fashion accessories','Food and beverages','Health and beauty','Home and lifestyle','Sports and travel'
plt.pie(Total_grossincome,labels=my_labels,autopct='%1.1f%%')
plt.title('Product line')
plt.axis('equal')
plt.show()