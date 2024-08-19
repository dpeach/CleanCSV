# To clean up a CSV file. This version is specifically for PayPal CSVs.

# This version asks for a Save As filename in case we dont want to overwrite the 
# previous version.

import pandas as pd
import sys
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename

# List of columns to remove (hardcoded)
COLUMNS_TO_REMOVE = ["Time", "TimeZone", "Type", "Status", "Currency", "To Email Address", "Address Line 2/District/Neighborhood", "Transaction ID", "Option 1 Name", "Option 1 Value", "Option 2 Name", "Option 2 Value", "Reference Txn ID", "Quantity", "Receipt ID", "Item Details"]  # Replace with your column names

# Dictionary of columns to rename: {"old_name": "new_name"}
COLUMNS_TO_RENAME = {
    "State/Province/Region/County/Territory/Prefecture/Republic": "State",
    "Zip/Postal Code": "Zip",
    # Add more renaming pairs as needed
}

def modify_columns(input_file):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Remove the specified columns
    df = df.drop(columns=COLUMNS_TO_REMOVE)

    # Rename the specified columns
    df = df.rename(columns=COLUMNS_TO_RENAME)

    # Prompt the user to select a save location and filename
    root = Tk()
    root.withdraw()  # Hide the root window
    output_file = asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

    if output_file:
        # Save the modified DataFrame to the chosen file
        df.to_csv(output_file, index=False)
        print(f"Columns {COLUMNS_TO_REMOVE} removed, columns renamed as {COLUMNS_TO_RENAME}, and saved to {output_file}")
    else:
        print("Save operation canceled.")

if __name__ == "__main__":
    # Get the file path from the argument
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        modify_columns(input_file)
    else:
        print("Please drag and drop a CSV file onto this script.")
