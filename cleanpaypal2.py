import pandas as pd
import argparse

# List of columns to remove (hardcoded)
COLUMNS_TO_REMOVE = ["Time", "TimeZone", "Type", "Status", "Currency", "To Email Address", "Address Line 2/District/Neighborhood", "Transaction ID", "Option 1 Name", "Option 1 Value", "Option 2 Name", "Option 2 Value", "Reference Txn ID", "Quantity", "Receipt ID", "Item Details"]  # Replace with your column names

# Dictionary of columns to rename: {"old_name": "new_name"}
COLUMNS_TO_RENAME = {
    "State/Province/Region/County/Territory/Prefecture/Republic": "State",
    "Zip/Postal Code": "Zip",
    # Add more renaming pairs as needed
}

# Consistent output file (it will rewrite each time run).
OUTPUT_FILE = "CleanedPayPal.csv"

def modify_columns(input_file):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Remove the specified columns
    df = df.drop(columns=COLUMNS_TO_REMOVE)

    # Rename the specified columns
    df = df.rename(columns=COLUMNS_TO_RENAME)

    # Save the modified DataFrame to a new CSV file
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Columns {COLUMNS_TO_REMOVE} removed and columns renamed as {COLUMNS_TO_RENAME}. Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Remove specific columns from a CSV file.")
    parser.add_argument("input_file", type=str, help="Path to the input CSV file.")

    # Parse the arguments
    args = parser.parse_args()

    # Call the function to remove columns
    modify_columns(args.input_file)

