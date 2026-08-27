import pandas as pd

# Shopify KPI Report - Saves 5h/week
def shopify_report(file_path):
    df = pd.read_csv(file_path)
    total_sales = df['total_price'].sum()
    aov = df['total_price'].mean()
    top_product = df['product_name'].mode()[0]
    print(f"Total Sales: ${total_sales:.2f}")
    print(f"AOV: ${aov:.2f}")
    print(f"Top: {top_product}")
    return df
