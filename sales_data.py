import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Data Collection (reading data from CSV)
sales_data = pd.read_csv('sales_data.csv')

# Step 2: Data Transformation (cleaning and preprocessing)
# For simplicity, let's assume the data is already clean

# Step 3: Data Processing (calculating total sales revenue by product category)
total_sales_by_category = sales_data.groupby('Product_Category')['Sales_Amount'].sum()

# Step 4: Data Analysis (visualizing total sales by category)
total_sales_by_category.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales Amount ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


