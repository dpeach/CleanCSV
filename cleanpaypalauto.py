# To clean up a CSV file. This version is specifically for PayPal CSVs.

# This version runs and automatically defines a saved file name.

import pandas as pd
import sys
import os

# List of columns to remove (hardcoded)
COLUMNS_TO_REMOVE = ["Time", "TimeZone", "Type", "Status", "Currency", "To Email Address", "Address Line 2/District/Neighborhood", "Transaction ID", "Option 1 Name", "Option 1 Value", "Option 2 Name", "Option 2 Value", "Reference Txn ID", "Quantity", "Receipt ID", "Item Details"]  # Replace with your column names

# Dictionary of columns to rename: {"old_name": "new_name"}
COLUMNS_TO_RENAME = {
    "State/Province/Region/County/Territory/Prefecture/Republic": "State",
    "Zip/Postal Code": "Zip",
    # Add more renaming pairs as needed
}

# Predefined output file name
OUTPUT_FILE = os.path.join("C:\\Users\\stephaniep\\Desktop\\CleanedPayPal.csv")  # Change to your desired output file name

def modify_columns(input_file):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Remove the specified columns
    df = df.drop(columns=COLUMNS_TO_REMOVE)

    # Rename the specified columns
    df = df.rename(columns=COLUMNS_TO_RENAME)

    # Save the modified DataFrame to a new CSV file
    df.to_csv(OUTPUT_FILE, index=False)
    # print(f"Columns {COLUMNS_TO_REMOVE} removed, columns renamed as {COLUMNS_TO_RENAME}, and saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    # Get the file path from the argument
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        modify_columns(input_file)
    else:
        print("Please drag and drop a CSV file onto this script.")
