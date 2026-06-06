# Data Analysis on CSV Files

## Overview
A comprehensive Python script for analyzing and visualizing sales data from CSV files. This tool automates the process of loading transactional data, computing key metrics such as total revenue by product and quantity sold by region, and generating insightful visual charts to help drive business decisions.

## Features
- **Data Loading & Cleaning**: Automatically loads CSV data and converts date columns into usable datetime objects.
- **Financial Metrics**: Calculates total sales dynamically from quantities and unit prices.
- **Data Aggregation**: Groups data to find the highest grossing products and regional sales distributions.
- **Data Visualization**: Generates ready-to-present bar and pie charts utilizing `matplotlib`, saving them automatically as image files for easy sharing.

## Prerequisites
- Python 3.7+
- Ensure you have `pip` installed to manage dependencies.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/abhranilsingharoy-cloud/Data-Analysis-on-CSV-Files.git
   cd Data-Analysis-on-CSV-Files
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure your data file is named `sales_data.csv` and is placed in the root directory. The CSV should contain columns such as `Date`, `Product`, `Region`, `Quantity`, and `UnitPrice`.

2. Run the analysis script:
   ```bash
   python sales_analysis.py
   ```

3. Review the outputs:
   - The script will print the Total Revenue by Product in the terminal.
   - It will generate an image file named `sales_charts.png` containing a Bar chart of Revenue by Product and a Pie chart of Quantity by Region.

## Project Structure
```
.
├── sales_analysis.py   # Main analysis script
├── sales_data.csv      # Sample sales dataset
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

## Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## License
This project is open-source and available under the [MIT License](LICENSE).
