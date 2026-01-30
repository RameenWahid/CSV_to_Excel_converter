# CSV to Excel Converter

## Project Overview
This project is a **CSV to Excel converter** using Python `pandas`. It also performs basic data cleaning and normalization, making it realistic for internship-level datasets.

The project handles **missing numeric and string values**, normalizes column names, and exports the cleaned data to Excel automatically.

## Features
- Reads CSV files using Python `pandas`
- Fills missing numeric values (e.g., Quantity, Unit Price) with **0**
- Fills missing string/text values (e.g., Customer Name, Status) with **"N/A"**
- Normalizes column names (lowercase and replaces spaces with underscores)
- Exports the cleaned dataset to Excel (`.xlsx`)
- Basic error handling included (File not found, other exceptions)

## Example Dataset
| Order ID | Customer Name | Order Date  | Product     | Quantity | Unit Price | Total Amount | Status    |
|----------|---------------|------------|------------|---------|------------|--------------|----------|
| 1001     | Ayesha Khan   | 01-01-2025 | Laptop     | 1       | 85000      | N/A          | Completed|
| 1002     | Ali Raza      | 03-01-2025 | Mouse      | 2       | 1500       | 3000         | Completed|
| 1003     | Sara Ahmed    | 05-01-2025 | Keyboard   | N/A     | 2500       | 2500         | Pending  |

*(Full dataset includes 25 customers for realistic testing)*

## How to Run
1. Install Python 3.x
2. Install required library:
```bash
pip install pandas openpyxl
