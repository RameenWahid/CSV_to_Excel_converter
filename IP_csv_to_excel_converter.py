
import pandas as pd
import os

input_file = r"C:\Users\TECHNOSELLERS\OneDrive\Desktop\python_programs\pandas\IP_csv_to_excel_converter.csv"

script_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(script_dir,"IP_csv_to_excel_converter.xlsx")

try:
    df = pd.read_csv(input_file)
    print("CSV file read successfully!")

    for i in df.columns:
        if pd.api.types.is_numeric_dtype(df[i]):
            df[i] = df[i].fillna(0)
        else:
            df[i] = df[i].fillna("N/A")

    df.columns = df.columns.str.lower().str.replace(" ", "_")

    df.to_excel(output_file, index = False)
    print("Excel file successfully created!")

except FileNotFoundError:
    print("file not found!")
except Exception as e:
    print("Error :",e)
