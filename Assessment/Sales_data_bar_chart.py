# Program to plot product-wise sales bar chart

import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
sales_data = pd.read_csv("sales.csv")

# Display data
print(sales_data)

# Plot bar chart
plt.bar(sales_data["Product"], sales_data["Sales"])

# Add title and labels
plt.title("Product-wise Sales")

plt.xlabel("Products")

plt.ylabel("Sales")

# Display chart
plt.show()

'''
output
Bar chart displaying product-wise sales.
'''
