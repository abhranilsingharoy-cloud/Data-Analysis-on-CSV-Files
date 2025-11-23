import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# FILE NAME: sales_analysis.py
# PURPOSE: Load sales data, perform analysis, and plot charts
# ---------------------------------------------------------

def main():
    # 1. Load CSV using Pandas
    file_path = 'sales_data.csv'
    
    try:
        print(f"Loading data from {file_path}...")
        df = pd.read_csv(file_path)
        
        # Convert Date column to datetime objects
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'])
            
        # Calculate Total Revenue per transaction
        df['TotalSales'] = df['Quantity'] * df['UnitPrice']
        
        print("Data loaded successfully.")
        print("-" * 30)
        print(df.head())
        print("-" * 30)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found. Please ensure it exists.")
        return

    # 2. Use groupby(), sum() for analysis
    
    # Analysis A: Revenue by Product
    product_revenue = df.groupby('Product')['TotalSales'].sum().sort_values(ascending=False)
    
    # Analysis B: Quantity Sold by Region
    region_quantity = df.groupby('Region')['Quantity'].sum()

    print("\n--- Total Revenue by Product ---")
    print(product_revenue)

    # 3. Plot charts
    # We will save the charts as an image file as part of the deliverables
    
    plt.figure(figsize=(12, 5))

    # Subplot 1: Bar Chart (Revenue by Product)
    plt.subplot(1, 2, 1)
    product_revenue.plot(kind='bar', color='#4c72b0')
    plt.title('Total Revenue by Product')
    plt.ylabel('Revenue ($)')
    plt.xlabel('Product')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Subplot 2: Pie Chart (Quantity by Region)
    plt.subplot(1, 2, 2)
    region_quantity.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
    plt.title('Quantity Sold by Region')
    plt.ylabel('')  # Hide y-label for cleaner pie chart

    plt.tight_layout()
    
    # Save the output chart
    output_filename = 'sales_charts.png'
    plt.savefig(output_filename)
    print(f"\nCharts saved to '{output_filename}'")
    
    plt.show()

if __name__ == "__main__":
    main()
