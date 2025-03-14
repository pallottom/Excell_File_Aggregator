import pandas as pd
import os


# Set directory where images are stored
def set_path():
    input_folder = input("Enter the path to the Excel file: ").strip()
    if not os.path.exists(input_folder):
        print("Error: File not found.")
        return
    return input_folder


# Get all Excel and csv files in the folder
def get_file_names(input_folder):
    files = [f for f in os.listdir(input_folder) if f.endswith(('.xlsx', '.xls', '.csv'))]

    if not files:
        print("Error: No Excel files found in the folder.")
        return

    print(f"Found {len(files)} files.")
    return files


def read_file(file_path):
    """Reads an Excel or CSV file and returns a DataFrame. Input is a the file path"""
    try:
        if file_path.endswith('.csv'):
            return pd.read_csv(file_path)
        else:
            return pd.read_excel(file_path)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None


# Ask user to select columns to keep
def get_selected_columns(df):
    """Asks the user for column selection and validates input. Input is a dataframe"""

    print("\nIf you want to select ALL columns, type ALL. Else you can choose amomngst the available columns:")
    available_columns = df.columns.tolist()
    print(available_columns)

    while True:
        user_input = input("To select ALL the columns, type ALL or enter the column names to keep (comma-separated): ").strip()
        
        if user_input.upper() == "ALL":  # Check if the user wants all columns
            return available_columns  # Return all available columns
        
        selected_columns = [col.strip() for col in user_input.split(',')]

        # Check for spelling mistakes or missing columns
        missing_columns = [col for col in selected_columns if col not in available_columns]
        if missing_columns:
            print(f"Error: The following columns do not exist: {missing_columns}")
            print("Please check the spelling and try again.")
        else:
            break


    return selected_columns

def process_files(input_folder, files, selected_columns, read_file):
    """
    Processes multiple files, extracts selected columns, and adds a 'Source_name' column.

    Parameters:
    - input_folder (str): Path to the input folder.
    - files (list): List of file names to process.
    - selected_columns (list): Columns to extract.
    - read_file (function): Function to read the file into a DataFrame.

    Returns:
    - List of processed DataFrames.
    """
    output = []

    for file in files:
        file_path = os.path.join(input_folder, file)  # Construct file path
        df = read_file(file_path)  # Read the file

        # Check for missing columns
        missing_columns = [col for col in selected_columns if col not in df.columns]
        if missing_columns:
            print(f"Skipping {file}: Missing columns {missing_columns}")
            continue

        # Select relevant columns
        temp_df = df[selected_columns].copy()
        temp_df.loc[:, 'Source_name'] = file  # Avoid SettingWithCopyWarning

        output.append(temp_df)  # Append the DataFrame to the list

        print(f"Processing file: {file}")

    return output  # Return the list of processed DataFrames



#Save file
# Check if there are any DataFrames in output_df
def save_output(output, input_folder):
        
    output_folder = os.path.join(input_folder, "processed")  # Create output folder if not exists
    os.makedirs(output_folder, exist_ok=True)

    if output:
        # Concatenate the list of DataFrames into one DataFrame
        final_df = pd.concat(output, ignore_index=True)

    # Write the final DataFrame to an Excel file
        output_file = os.path.join(output_folder, 'output.xlsx')
        with pd.ExcelWriter(output_file) as writer:
            final_df.to_excel(writer, index=False)

    else:
        print("No files processed, no data to concatenate.")



# Main script execution
def main():
    input_folder = set_path()
    if not input_folder:
        return  # Exit if no folder is found

    files = get_file_names(input_folder)
    if not files:
        return  # Exit if no files are found

    # Read the first file to get column names
    file_path = os.path.join(input_folder, files[0])
    df = read_file(file_path)
    if df is None:
        print("Error: Could not read the first file to determine columns.")
        return

    selected_columns = get_selected_columns(df)
    processed_dataframes = process_files(input_folder, files, selected_columns, read_file)
    
    save_output(processed_dataframes, input_folder)
    print("🎉 Processing complete.")

# Run the script
if __name__ == "__main__":
    main()
