# Excel File Aggregator

This Python script processes multiple Excel or CSV files from a given directory, extracts selected columns, adds a Source_name column to track the origin of each row, and consolidates all the processed data into a single Excel file.

## To run the script:

Open the following folders:

_dist_ > _Excell_aggregaror_ > 

And run _Excell_aggregaror.exe_

## Step-by-Step Execution

1. Set Directory Path:

Copy and paste the full data folder path example for example <_L:\Sinead\Daniel\Brightfield\fiji output\13939_6>_

If the folder doesn’t exist, it returns an error.

2. Column Selection:

The user will be prompted to select the columns to extract.

Type _ALL_ to select all available columns.
Press _Enter_ to load predefined column names from columns.txt (if the file exists in the input folder).
Press _Ctrl+C_ to quit the program.

3. Processing Files:

Each file is processed.

4. Save Output:

Processed data is saved in a new folder processed/ inside the input folder.

The final file is named _output.xlsx_.


## For developers: 
### Requirements

Ensure you have the following installed:

`Python 3.11.3+`

Required Python libraries: `pandas`and `openpyxl`


### Installation

1. Clone or download the repository:

``` git clone https://github.com/pallottom/ExcelAggregator.git ```


2. Install dependencies:

```pip install pandas openpyxl```

3. Launch the program:

Type in you terminal `python Excell_aggregator.py`


