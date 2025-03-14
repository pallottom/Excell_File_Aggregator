#Excel File Aggregator

This Python script processes multiple Excel or CSV files from a given directory, extracts selected columns, adds a Source_name column to track the origin of each row, and consolidates all the processed data into a single Excel file.

##Requirements

Ensure you have the following installed:

`Python 3.11.3+`


##Installation

1. Clone or download the repository:

```git clone https://github.com/yourusername/ExcelAggregator.git
cd ExcelAggregator```

2. Install dependencies:

```pip install pandas openpyxl```

``` pyenv local 3.11.3
python -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt ```