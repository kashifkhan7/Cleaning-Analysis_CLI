# Sales Analysis CLI Application 📊

This command-line Python app allows users to analyze sales data from a CSV file. It provides insights into:

- Product-wise revenue
- Region-wise revenue
- Monthly revenue trends
- Interactive visualizations (pie and bar charts)

## Features
- Automatic null value handling
- Revenue calculation (if not in file)
- Monthly, regional, and product revenue insights
- CLI-based menu interface
- Uses Pandas, Matplotlib, and Seaborn

## How to Use

1. Clone this repository
2. Install required packages:
3. Run the app: python CLI_App.py


4. When prompted, enter the path to your CSV sales file (must include at least `price`, `quantity`, and `product` columns).

## Example CSV Format

| date       | product  | region   | price | quantity |
|------------|----------|----------|-------|----------|
| 2023-01-01 | Laptop   | West     | 50000 | 2        |
| 2023-01-02 | Monitor  | East     | 8000  | 5        |

## License

MIT License

