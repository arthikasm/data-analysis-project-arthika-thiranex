import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv", encoding="latin1")

print("First 5 Rows")
print(df.head())

print("\nDataset Information")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

category_sales = df.groupby("Category")["Sales"].sum()

print("\nSales by Category")
print(category_sales)

category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.ylabel("Sales")
plt.savefig("category_sales.png")
plt.show()

top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

top_products.plot(kind="bar")
plt.title("Top 10 Products by Sales")
plt.ylabel("Sales")
plt.savefig("top_products.png")
plt.show()

df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = df.groupby(df["Order Date"].dt.month)["Sales"].sum()

monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("monthly_sales.png")
plt.show()

print("\nAnalysis Completed Successfully")