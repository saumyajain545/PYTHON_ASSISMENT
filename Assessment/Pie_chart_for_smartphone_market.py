# Import Matplotlib library
import matplotlib.pyplot as plt

# List of smartphone brands
brands = ['Samsung', 'Apple', 'Vivo', 'Oppo']

# Market share values
market_share = [35, 30, 20, 15]

# Highlight the brand with maximum market share
explode = [0.1, 0, 0, 0]

# Create pie chart
plt.pie(
    market_share,
    labels=brands,
    explode=explode,
    autopct='%1.1f%%'
)

# Add chart title
plt.title("Smartphone Market Share")

# Display chart
plt.show()

'''
output
A pie chart is displayed showing:

Samsung → 35%
Apple → 30%
Vivo → 20%
Oppo → 15%

Samsung slice is highlighted because it has
the highest market share.
'''
