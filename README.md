# CleanCSV
This is a python3 program that cleans up CSV files to include just the columns you need. It also has a way to rename columns.

# Backstory
We regularly download a PayPal CSV to use in our office. It includes many columns that we don't need. It also has some strange column names that I would like to shorten. This script does both.

Something like this is helpful when you are regularly dealing with the need to change a particular CSV/spreadsheet file. Maybe on the scale of quarterly or more often. It probably isn't that helpful for something you deal with just a couple of times a year.

I used ChatGPT to help build this. I think this is my first successful collaboration with ChatGPT. I knew enough about what I wanted to do that I could create appropriate prompts for this program.

As I am not an expert on coding nor documentation, I am going to at least put enough information on here that will make it easy for me to adapt this in the future.

# Adjustments
Inside the script are the sections COLUMNS_TO_REMOVE and COLUMNS_TO_RENAME. Those are what you will need to change for your purposes.

## COLUMNS_TO_REMOVE
The format is
``` COLUMNS_TO_REMOVE =  ["ColumnName1", "ColumnName2", "etc"] ```

Put each column name in that you want to delete.

## COLUMNS_TO_RENAME
This is a dictionary replacement.
``` COLUMNS_TO_RENAME = {"OriginalName1": "NewName1", "OriginalName2": "NewName2"} ```

# Usage
The basic script is set up to run with:
``` python3 CleanCSV.py INPUTFILE ```

The output file is hard coded on the basic script. It will output to the same directory as run as a file named "CleanedPayPal.csv" unless changed in the OUTPUT_FILE line.

# Alternate Version
I will also upload a version that can be run on Windows and will generate a Save As dialog box.

# Requirements
Libraries that will be used (and may be automatically installed) are:
- pandas
- sys
- tkinter
- argparse
- os

This is dependent on which version of the program you use.

# Versions
There are 3 versions of the program that I have uploaded. You run them with ``` python SCRIPTNAME INPUTFILE.csv ```
## cleanpaypal.py
This is the version I would use on Linux. It outputs to a file in the current working directory.

## cleanpaypalauto.py
This is a Windows version. It will save to a consistent file on the desktop. That can be changed in the script. It will overwrite the same file each time.

## cleanpaypalsaveas.py
This is also a Windows version. This one gives a Save As dialog box.

# .bat File
Here is the batch file that can be put on your desktop to drag and drop your csv file onto.

```
@echo off
python path\to\cleanpaypalXXX.py %1
```
