import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import numpy_financial as npf

# Import dataset:supermarket_sales - Sheet1.csv
supermarket_sales = pd.read_csv('supermarket_sales - Sheet1.csv')
print(supermarket_sales.head())
print(supermarket_sales.info())

# Using drop duplicates to check branches and cities
supermarket_city = supermarket_sales[["City",'Branch']]
supermarket_city =supermarket_city.drop_duplicates(subset=["City"])
print(supermarket_city)

# Check if there is any missing value in the file
print(supermarket_sales.isna().any())

# Sorting Total sales by descending values to find out top 5 highest sales.
print(supermarket_sales.sort_values('Total', ascending = False).head().to_string())

# View most popular product by quantities sold
# Grouping the product line by sales quantities to find out min, max and sum
supermarket_Yangon=supermarket_sales[supermarket_sales["City"]=="Yangon"]
print(supermarket_Yangon.groupby('Product line')["Quantity"].agg([min,max,sum]))

supermarket_Mandalay=supermarket_sales[supermarket_sales["City"] == "Mandalay"]
print(supermarket_Mandalay.groupby('Product line')["Quantity"].agg([min,max,sum]))

supermarket_Naypyitaw=supermarket_sales[supermarket_sales["City"] == "Naypyitaw"]
print(supermarket_Naypyitaw.groupby('Product line')["Quantity"].agg([min,max,sum]))

print(supermarket_sales.groupby('Product line')["Quantity"].agg([min,max,sum]))

# Create a new list of dicts based on above info to visualize the data
data = [['Yangon',322,263,313,257,371,333],
        ['Mandalay',316,297,270,320,295,322],
        ['Naypyitaw',333,342,369,277,245,265],
        ['City Total',971,902,952,854,911,920]]
columns = ['City','Electronic accessories','Fashion accessories','Food and beverages','Health and beauty','Home and lifestyle','Sports and travel']
supermarket_quantity = pd.DataFrame(data=data, columns=columns)
print(supermarket_quantity.to_string())

# View supermarket_quantity in a bar chart
supermarket_quantity.plot(
    x="City", y=['Electronic accessories','Fashion accessories','Food and beverages','Health and beauty','Home and lifestyle','Sports and travel'], kind="bar",
)
plt.xticks(rotation = 360)
plt.title("Product Line")
plt.xlabel("City")
plt.ylabel("Quantities")


# View gross income by gender
supermarket_Female=supermarket_sales[supermarket_sales["Gender"]=="Female"]
supermarket_Female=supermarket_Female["gross income"].sum()
print(supermarket_Female)

supermarket_Male=supermarket_sales[supermarket_sales["Gender"]=="Male"]
supermarket_Male=supermarket_Male["gross income"].sum()
print(supermarket_Male)

supermarket_sales_grossincome=supermarket_sales["gross income"].sum()
print(supermarket_sales_grossincome)

Percentage_Female=supermarket_Female/supermarket_sales_grossincome
print(Percentage_Female)
Percentage_Male=supermarket_Male/supermarket_sales_grossincome
print(Percentage_Male)

data=[['Female',supermarket_Female,Percentage_Female],
      ['Male',supermarket_Male,Percentage_Male]]
columns=['Gender','Gross Income','Percentage']
Grossincome_Gender=pd.DataFrame(data=data,columns=columns)
print(Grossincome_Gender)

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

pd.options.mode.chained_assignment = None
supermarket_total_sales['Date']=pd.to_datetime(supermarket_total_sales['Date'])
supermarket_total_sales['Time']=pd.to_datetime(supermarket_total_sales['Time'])
print(supermarket_total_sales.info())

supermarket_total_sales['Year']=supermarket_total_sales['Date'].dt.year
supermarket_total_sales['Month']=supermarket_total_sales['Date'].dt.month
supermarket_total_sales['Week']=supermarket_total_sales['Date'].dt.isocalendar().week
print(supermarket_total_sales.info())
print(supermarket_total_sales.head())

supermarket_total_sales_month=supermarket_total_sales.groupby(['Branch','Month','Week'])['Total'].sum()
print(supermarket_total_sales_month)

#Add column 'Mean' to supermarket_total_sales
#print(supermarket_total_sales.info())
supermarket_total_sales['Mean']=supermarket_total_sales.groupby('Week')['Total'].mean()
print(supermarket_total_sales.info())
#print(supermarket_total_sales.head())
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

# Grouping total sales by branch to get min,max,sun,mean

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

# To view popular payment type
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

# Iterrow to check customer's satisfaction by Rating

# Rating is higher than 8, find out invoice no.
for index, row in supermarket_sales.iterrows():
    print(row['Invoice ID'],row['Rating']>8)

# Rating is lower than 5, find out invoice no.
for index, row in supermarket_sales.iterrows():
    print(row['Invoice ID'],row['Rating']<5)

# To view customer satisfaction by rating
supermarket_rating=supermarket_sales.groupby(['Product line'])['Rating'].agg(['count','mean','max'])
supermarket_rating.columns = ['Rating_count','Rating_mean','Rating_Highest']
supermarket_rating = supermarket_rating.reset_index()
print(supermarket_rating)

supermarket_rating_less5=supermarket_sales[supermarket_sales['Rating']<5]
supermarket_rating_less5=supermarket_rating_less5.groupby(['Product line'])['Rating'].agg(['count','min'])
supermarket_rating_less5.columns = ['Rating_countPoor','Rating_Lowest']
supermarket_rating_less5 = supermarket_rating_less5.reset_index()
print(supermarket_rating_less5)

#Merge general rating and poor rating dataframes
supermarket_rating_all=supermarket_rating.merge(supermarket_rating_less5, on = 'Product line')
supermarket_rating_all['Percentage_Poor']=supermarket_rating_all['Rating_countPoor']/supermarket_rating_all['Rating_count']
supermarket_rating_all['Percentage_Good'] = 1- supermarket_rating_all['Percentage_Poor']
print(supermarket_rating_all.to_string())


# View Rating Highest,Lowest, Average
supermarket_rating_all.plot(
    x="Product line", y=['Rating_Highest','Rating_mean','Rating_Lowest'], kind="bar",
)
plt.xticks(rotation = 360)
plt.title("Customer Rating")
plt.xlabel("Product Line")
plt.ylabel("Rating")
plt.show()

# Customer satisfaction %
supermarket_rating_all.plot(
    x="Product line", y=['Percentage_Good','Percentage_Poor',], kind="bar",
)
plt.xticks(rotation = 360)
plt.title("Customer Rating")
plt.xlabel("Product Line")
plt.ylabel("Rating % ")
plt.show()

supermarket_rating_percentage=supermarket_rating_all[['Product line','Percentage_Good','Percentage_Poor']]
print(supermarket_rating_percentage)

# View Peak time by sales transactions
supermarket_peaktime=supermarket_sales[['Branch','City','Time','Total']]
supermarket_peaktime['Time']=pd.to_datetime(supermarket_peaktime['Time'])
supermarket_peaktime['Time_Hour']=supermarket_peaktime['Time'].dt.hour
supermarket_peaktime=supermarket_peaktime.sort_values('Time')
supermarket_peaktime['Time']=supermarket_peaktime['Time'].apply(str)
print(supermarket_peaktime.info())
sns.scatterplot(supermarket_peaktime['Time'], supermarket_peaktime['Total'])
plt.title('Peak Hours')
plt.show()

#View Sales total and average by hours
supermarket_peaktime_total=supermarket_peaktime.groupby('Time_Hour').agg(['sum','mean'])
supermarket_peaktime_total.columns = ['Total_sum','Total_mean']
supermarket_peaktime_total = supermarket_peaktime_total.reset_index()
supermarket_peaktime_total['Time_Hour']=supermarket_peaktime_total['Time_Hour'].apply(str)
print(supermarket_peaktime_total)
fig, ax = plt.subplots()
ax.plot(supermarket_peaktime_total["Time_Hour"], supermarket_peaktime_total["Total_sum"],marker="o")
ax.set_xlabel(" Time")
ax.set_ylabel(" Sales total (€)")
ax.set_title(" Total of Sales by Hours")
plt.show()

fig, ax = plt.subplots()
ax.plot(supermarket_peaktime_total["Time_Hour"], supermarket_peaktime_total["Total_mean"],marker="o")
ax.set_xlabel(" Time")
ax.set_ylabel(" Sales mean (€)")
ax.set_title(" Average of Sales by Hours")
plt.show()

# To find out the Key info
supermarket_sales['Total']=supermarket_sales['Total'].round(1)
supermarket_total=supermarket_sales['Total'].sum()
print("The total sales is " + str(supermarket_total) +" Euro.")

supermarket_sales['gross income']=supermarket_sales['gross income'].round(1)
supermarket_gross_income=supermarket_sales['gross income'].sum()
print("The gross income is " + str(supermarket_gross_income) + " Euro.")

supermarket_sales['cogs']=supermarket_sales['cogs'].round(1)
supermarket_cogs=supermarket_sales['cogs'].sum()
print("The cost of goods sold is " + str(supermarket_gross_income) + " Euro.")

# Using reused code to calculate annual forecast based on quarter total sales amount
supermarket_totalsales_branch_quarter = supermarket_sales.groupby('Branch')['Total'].sum()
supermarket_totalsales_branch_quarter = supermarket_totalsales_branch_quarter.reset_index()
print(supermarket_totalsales_branch_quarter)

def format_float(n):

    formatted_float = "€{:,.2f}".format(n)
    return formatted_float

def totalsales_quarter(n):

    totalsales_year = n * 4
    #print ("The annual total sales forecast is %d." %(totalsales_year))
    return totalsales_year
length = (supermarket_totalsales_branch_quarter.shape[0])
list = []

for i in range(0,length):
    x = totalsales_quarter(supermarket_totalsales_branch_quarter.iloc[i, 1])
    if i == 0:
        print("Branch A annual forecast sales is " + format_float(x))
    if i == 1:
        print("Branch B annual forecast sales is " + format_float(x))
    if i == 2:
        print("Branch C annual forecast sales is " + format_float(x))

   # print(x)
    list.append(x)


# To find out the highest total sales forecast
print(max(list))

index = list.index(max(list))
if index == 0:
    print("The highest total sales forecast is Branch A "+format_float(max(list)))

if index == 1:
    print("The highest total sales forecast is Branch B "+format_float(max(list)))

if index == 2:
    print("The highest total sales forecast is Branch C "+format_float(max(list)))
    print(max(list))

# Expansion plan in branch C as this is most profitable supermarket
Branch_C_year1_cashflow = max(list)
Branch_C_5years_cashflow=([(Branch_C_year1_cashflow),(Branch_C_year1_cashflow*1.05),(Branch_C_year1_cashflow*(1.05**2)),(Branch_C_year1_cashflow*(1.05**3)),(Branch_C_year1_cashflow*(1.05**5))])

print(Branch_C_5years_cashflow)

for i in range(0,5):
  year=str(i+1)
  print("year "+year+ " "+ format_float(Branch_C_5years_cashflow[i]))


# Calculate NPV if rate is 3%
Branch_C_5years_cashflow_npv=npf.npv(rate=0.03, values=Branch_C_5years_cashflow)
print("The forecast net present value in Branch C is €"+ str(round(Branch_C_5years_cashflow_npv, 2)))

# Investment 1 : Invest 1 million in Branch C for 5 years at rate 3%
Investment1 = ([-1000000,200000,350000,450000,650000])
Branch_C_5years_investment1_npv=npf.npv(rate=0.03, values=Investment1)
print("The investment 1 net present value in Branch C is €"+ str(round(Branch_C_5years_investment1_npv, 2)))

# Investment 2 : Invest €500,000 in Branch C for 3 years at rate 3%
Investment2 = ([-500000,100000,250000,350000])
Branch_C_5years_investment2_npv=npf.npv(rate=0.03, values=Investment2)
print("The investment 2 net present value in Branch C is €"+ str(round(Branch_C_5years_investment2_npv, 2)))



