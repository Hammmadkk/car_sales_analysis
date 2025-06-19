import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('data/car_sales_data.csv', parse_dates=['Date'])

# 1. Line Plot - Units Sold Over Time
plt.figure(figsize=(12, 5))
plt.plot(df['Date'], df['Units Sold'], marker='o', linestyle='-', color='teal')
plt.title('Units Sold Over Time')
plt.xlabel('Date')
plt.ylabel('Units Sold')
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Scatter Plot - Units Sold vs Total Sales
plt.figure(figsize=(8, 5))
plt.scatter(df['Units Sold'], df['Total Sales'], color='green', alpha=0.6)
plt.title('Units Sold vs Total Sales')
plt.xlabel('Units Sold')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

# 3. Bar Chart - Total Sales by Region
region_sales = df.groupby('Region')['Total Sales'].sum().sort_values()
plt.figure(figsize=(8, 5))
region_sales.plot(kind='bar', color='coral')
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales Amount')
plt.tight_layout()
plt.show()

# 4. Histogram - Distribution of Unit Prices
plt.figure(figsize=(8, 5))
plt.hist(df['Unit Price'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Unit Prices')
plt.xlabel('Unit Price')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 5. Pie Chart - Car Model Distribution
car_counts = df['Car Model'].value_counts()
plt.figure(figsize=(7, 7))
plt.pie(car_counts, labels=car_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Car Model Share')
plt.axis('equal')
plt.tight_layout()
plt.show()

# 6. Subplot - Units Sold and Total Sales Over Time
fig, axs = plt.subplots(2, 1, figsize=(12, 8))
axs[0].plot(df['Date'], df['Units Sold'], color='blue', marker='o')
axs[0].set_title('Units Sold Over Time')
axs[1].plot(df['Date'], df['Total Sales'], color='darkgreen', marker='x')
axs[1].set_title('Total Sales Over Time')
plt.tight_layout()
plt.show()

# 7. Customized Dual Axis Plot - Units Sold and Total Sales
fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.set_xlabel('Date')
ax1.set_ylabel('Units Sold', color='tab:red')
ax1.plot(df['Date'], df['Units Sold'], color='tab:red', label='Units Sold')
ax1.tick_params(axis='y', labelcolor='tab:red')

ax2 = ax1.twinx()
ax2.set_ylabel('Total Sales', color='tab:blue')
ax2.plot(df['Date'], df['Total Sales'], color='tab:blue', label='Total Sales')
ax2.tick_params(axis='y', labelcolor='tab:blue')

plt.title('Units Sold and Total Sales Over Time')
fig.tight_layout()
plt.show()
