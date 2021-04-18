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

# To analyse Total sales
supermarket_total_sales = supermarket_sales[["Branch","City","Date","Time","Total"]]
print(supermarket_total_sales.head())
print(supermarket_total_sales.info())

supermarket_total_sales['Date']=pd.to_datetime(supermarket_total_sales['Date'])
supermarket_total_sales['Time']=pd.to_datetime(supermarket_total_sales['Time'])
print(supermarket_total_sales.info())

supermarket_total_sales['Year']=supermarket_total_sales['Date'].dt.year
supermarket_total_sales['Month']=supermarket_total_sales['Date'].dt.month
supermarket_total_sales['Week']=supermarket_total_sales['Date'].dt.week
print(supermarket_total_sales.info())
print(supermarket_total_sales.head())

supermarket_total_sales_month=supermarket_total_sales.groupby(['Branch','Month','Week'])['Total'].sum()
print(supermarket_total_sales_month)

#To add column 'Mean' to supermarket_total_sales
print(supermarket_total_sales.info())
supermarket_total_sales['Mean']=supermarket_total_sales.groupby('Week')['Total'].mean()
print(supermarket_total_sales.info())
print(supermarket_total_sales.head())
print(supermarket_total_sales.isna().any())
supermarket_total_sales=supermarket_total_sales.sort_values('Total')
print(supermarket_total_sales)

# Drop 'Date' and 'time' to see if still missing value
supermarket_total_sales=supermarket_total_sales.drop(['Date','Time'], axis='columns', inplace=False)
print(supermarket_total_sales.info())
print(supermarket_total_sales.isna().sum())

# Fill missing value with average mean value
supermarket_total_sales=supermarket_total_sales.fillna(supermarket_total_sales.mean())
print(supermarket_total_sales.info())
print(supermarket_total_sales.isna().sum())
print(supermarket_total_sales.head())

# Grouping total sales by branch and city to get min,max,sun,mean

supermarket_total_sales_week=supermarket_total_sales.groupby(['Branch','Week'])['Total'].agg(['min', 'max','sum','mean'])
print(supermarket_total_sales_week.info())
print(supermarket_total_sales_week)

# rename columns
supermarket_total_sales_week.columns = ['week_min', 'week_max', 'week_sum','week_mean']

# reset index to get grouped columns back
supermarket_total_sales_week = supermarket_total_sales_week.reset_index()

print(supermarket_total_sales_week.info())

#Supermarket_total_sales_week per branch

supermarket_total_sales_week['Week']=supermarket_total_sales_week['Week'].apply(str)
supermarket_total_sales_week_A = supermarket_total_sales_week[supermarket_total_sales_week['Branch']=='A']
print(supermarket_total_sales_week_A)
supermarket_total_sales_week_B = supermarket_total_sales_week[supermarket_total_sales_week['Branch']=='B']
print(supermarket_total_sales_week_B)
supermarket_total_sales_week_C = supermarket_total_sales_week[supermarket_total_sales_week['Branch']=='C']
print(supermarket_total_sales_week_C)

# View Total Sales by mean, min, max, sum for each branch
fig, ax = plt.subplots()
ax.plot(supermarket_total_sales_week_A["Week"], supermarket_total_sales_week_A["week_mean"],marker="o",label="A Yangon")
ax.plot(supermarket_total_sales_week_B["Week"], supermarket_total_sales_week_B["week_mean"],marker="o", label="B Mandalay")
ax.plot(supermarket_total_sales_week_C["Week"], supermarket_total_sales_week_C["week_mean"],marker="o", label = "C Naypyitaw")
ax.set_xlabel(" Week")
ax.set_ylabel(" Weekly Mean (€)")
ax.set_title(" Total Sales Per Week by Mean")
leg = ax.legend()
plt.show()

fig, ax = plt.subplots()
ax.plot(supermarket_total_sales_week_A["Week"], supermarket_total_sales_week_A["week_sum"],marker="o",label="A Yangon")
ax.plot(supermarket_total_sales_week_B["Week"], supermarket_total_sales_week_B["week_sum"],marker="o", label="B Mandalay")
ax.plot(supermarket_total_sales_week_C["Week"], supermarket_total_sales_week_C["week_sum"],marker="o", label = "C Naypyitaw")
ax.set_xlabel(" Week")
ax.set_ylabel(" Weekly Total (€)")
ax.set_title(" Total Sales Per Week")
leg = ax.legend()
plt.show()

fig, ax = plt.subplots()
ax.plot(supermarket_total_sales_week_A["Week"], supermarket_total_sales_week_A["week_min"],marker="o",label="A Yangon")
ax.plot(supermarket_total_sales_week_B["Week"], supermarket_total_sales_week_B["week_min"],marker="o", label="B Mandalay")
ax.plot(supermarket_total_sales_week_C["Week"], supermarket_total_sales_week_C["week_min"],marker="o", label = "C Naypyitaw")
ax.set_xlabel(" Week")
ax.set_ylabel(" Weekly Min (€)")
ax.set_title(" Weekly Minimum Sales")
leg = ax.legend()
plt.show()

fig, ax = plt.subplots()
ax.plot(supermarket_total_sales_week_A["Week"], supermarket_total_sales_week_A["week_max"],marker="o",label="A Yangon")
ax.plot(supermarket_total_sales_week_B["Week"], supermarket_total_sales_week_B["week_max"],marker="o", label="B Mandalay")
ax.plot(supermarket_total_sales_week_C["Week"], supermarket_total_sales_week_C["week_max"],marker="o", label = "C Naypyitaw")
ax.set_xlabel(" Week")
ax.set_ylabel(" Weekly Max (€)")
ax.set_title(" Weekly Maximum Sales")
leg = ax.legend()
plt.show()

# To check which payment type is popular
print(supermarket_sales.info())
supermarket_payment=supermarket_sales.groupby('Payment')['gross income'].agg(['sum','count'])
print(supermarket_payment)
supermarket_payment.columns = ['Total_sum', 'Total_count']
supermarket_payment = supermarket_payment.reset_index()
print(supermarket_payment)

fig, ax = plt.subplots()
ax.bar(supermarket_payment["Payment"], supermarket_payment["Total_sum"])
ax.set_ylabel(" Gross income (€)")
ax.set_title(" Payment Type")
plt.show()

fig, ax = plt.subplots()
ax.bar(supermarket_payment["Payment"], supermarket_payment["Total_count"])
ax.set_ylabel(" Count")
ax.set_title(" Payment Type")
plt.show()

# To find out most profitable by customer type
supermarket_customer_type=supermarket_sales.groupby(['Branch','Customer type'])['gross income'].sum()
print(supermarket_customer_type)
supermarket_customer_type.columns = ['gross_sum']
supermarket_customer_type = supermarket_customer_type.reset_index()
print(supermarket_customer_type)

sns.barplot(data = supermarket_customer_type
            ,x = 'Branch'
            ,y = 'gross income'
            ,hue = 'Customer type'
            ,ci = None
            )
plt.show()
