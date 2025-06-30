import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
   data = input("Enter the path to the CSV file (only sales file): ")
   df = pd.read_csv(data)
except FileNotFoundError as FF:
    print(f"File not found: {FF}. Please check the file path and try again.")
except Exception as E:
    print(f"Value error: {E}. Please check the file format and content.")

for col in df.columns:
    if df[col].isnull().any():
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col].fillna(df[col].mean(), inplace=True)
        elif pd.api.types.is_string_dtype(df[col]) or df[col].dtype == 'object':
            df[col].fillna(df[col].mode()[0], inplace=True)


for col in df.columns:
    if 'date' in col.lower():
        df[col] = pd.to_datetime(df[col])
        break

if 'revenue' not in df.columns:
    if 'quantity' in df.columns and 'price' in df.columns:
        df['revenue'] = df['quantity'] * df['price']
    else:
        print("Columns 'quantity' and 'price' are required to calculate revenue. please check the CSV file.")

def product_revenue():
    product_revenue = df.groupby('product')['revenue'].sum().sort_values(ascending=False)
    max_product = product_revenue.idxmax()
    min_product = product_revenue.idxmin()
    print("--------------------------------------")
    print("Product Revenue Analysis")
    print("--------------------------------------")
    ans = int(input("Enter \n 1 for product with maximum revenue \n 2 for product with minimum revenue \n 3 for the complete list of product revenue \n 4 for Visualization of product revenue: "))
    if ans == 1:
        print(f"Product with maximum revenue: {max_product} with revenue {product_revenue[max_product]}")
        print("--------------------------------------")
    elif ans == 2:
        print(f"Product with minimum revenue: {min_product} with revenue {product_revenue[min_product]}")
        print("--------------------------------------")
    elif ans == 3:
        print("Product revenue list:")
        print(product_revenue)
        print("--------------------------------------")
    elif ans == 4:
        plt.figure(figsize=(10,10))
        plt.pie(product_revenue, labels=product_revenue.index, autopct='%1.1f%%', startangle=140)
        plt.title('Product Revenue Distribution')
        plt.axis('equal')
        plt.show()
        print("--------------------------------------")
    else:
        print("Invalid choice. Please try again.")

def region_revenue():
    region_revenue = df.groupby('region')['revenue'].sum().sort_values(ascending=False)
    max_region = region_revenue.idxmax()
    min_region = region_revenue.idxmin()
    print("--------------------------------------")
    print("Region Revenue Analysis")
    print("--------------------------------------")
    ans = int(input("Enter \n 1 for region with maximum revenue \n 2 for region with minimum revenue \n 3 for the complete list of region revenue \n 4 for Visualization of region revenue: "))
    if ans == 1:    
        print(f"Region with maximum revenue: {max_region} with revenue {region_revenue[max_region]}")
        print("--------------------------------------")
    elif ans == 2:
        print(f"Region with minimum revenue: {min_region} with revenue {region_revenue[min_region]}")   
        print("--------------------------------------")
    elif ans == 3:
        print("Region revenue list:")
        print(region_revenue)
        print("--------------------------------------")
    elif ans == 4:
        plt.figure(figsize=(10,6))
        sns.barplot(x=region_revenue.index, y=region_revenue.values, color='skyblue')
        plt.title('Region-wise Revenue')
        plt.xlabel('Region')
        plt.ylabel('Total Revenue')
        
        plt.tight_layout()
        plt.show()
        print("--------------------------------------")
    else:
        print("Invalid choice. Please try again.")

def monthly_revenue():
    df['month'] = df['date'].dt.to_period('M')
    monthly_revenue = df.groupby('month')['revenue'].sum().sort_values(ascending=False)
    max_revenue = monthly_revenue.idxmax()
    min_revenue = monthly_revenue.idxmin()
    print("--------------------------------------")
    print("Monthly Revenue Analysis")   
    print("--------------------------------------")
    ans = int(input("Enter \n 1 for month with maximum revenue \n   2 for month with minimum revenue \n 3 for the complete list of monthly revenue \n 4 for Visualization of monthly revenue: "))
    if ans == 1:    
        print(f"Month with maximum revenue: {max_revenue} with revenue {monthly_revenue[max_revenue]}")
        print("--------------------------------------")
    elif ans == 2:
        print(f"Month with minimum revenue: {min_revenue} with revenue {monthly_revenue[min_revenue]}")
        print("--------------------------------------")
    elif ans == 3:
        print("Monthly revenue list:")
        print(monthly_revenue)
        print("--------------------------------------")
    elif ans == 4:
        plt.figure(figsize=(9,6))
        sns.barplot(x=monthly_revenue.index, y=monthly_revenue.values, color='yellow')
        plt.title('Monthly Revenue')
        plt.xlabel('Month')
        plt.ylabel('Total Revenue')
        plt.tight_layout()
        plt.show()
        print("--------------------------------------")
    else:
        print("Invalid choice. Please try again.")

while True:
    print("--------------------------------------------")
    print("Welcome to the Sales Analysis Application")
    print("Choose an option:")
    print("1. Product Revenue Analysis")
    print("2. Region Revenue Analysis")
    print("3. Monthly Revenue Analysis")
    print("4. Exit")
    print("--------------------------------------------")
    choice = input("Enter your choice: ")    
    print("--------------------------------------------")
    if choice == '1':
        product_revenue()
    elif choice == '2':
        region_revenue()
    elif choice == '3':
        monthly_revenue()
    elif choice == '4':
        print("Exiting the application.")
        break
    else:
        print("Invalid choice. Please try again.")

    
