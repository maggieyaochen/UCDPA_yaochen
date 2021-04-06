import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
supermarket_sales= pd.read_csv (r'C:\Users\maggie\Desktop\Python\Project\supermarket_sales - Sheet1.csv')
print(supermarket_sales)
print(supermarket_sales.shape)
print(supermarket_sales.columns)
print(supermarket_sales.sort_values("Total"))
print(supermarket_sales.groupby)
