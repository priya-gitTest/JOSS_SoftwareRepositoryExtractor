import pandas as pd

# --- Configuration ---
# This should be the output file from the first script.
INPUT_CSV_FILE = "joss_repositories_20250806_080130_licenses.csv"
# This will be the new file where the counts are saved.
OUTPUT_COUNTS_CSV = "license_counts_summary.csv"
# -------------------

def count_licenses_with_pandas(file_path):
    """
    Reads a CSV file using pandas and counts the occurrences of each license.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pandas.Series: A Series object with license names as the index and their counts as values,
                       or None if an error occurs.
    """
    try:
        # Read the CSV file into a pandas DataFrame.
        # Assumes the first row is the header.
        df = pd.read_csv(file_path)

        # Check if the 'License' column exists in the DataFrame
        if 'License' not in df.columns:
            print(f"Error: The CSV file '{file_path}' does not contain a 'License' column.")
            return None
            
        # Use the value_counts() method to count unique values in the 'License' column.
        # This will also handle missing values (NaN) by default.
        license_counts = df['License'].value_counts()
        
        return license_counts
        
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_path}' is empty.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    """
    Main function to run the license counting, print the results, and save them to a CSV.
    """
    print(f"Counting licenses from '{INPUT_CSV_FILE}' using pandas...")
    
    counts = count_licenses_with_pandas(INPUT_CSV_FILE)
    
    # The result from value_counts() is a pandas Series. We can check if it's not None and not empty.
    if counts is not None and not counts.empty:
        print("\n--- License Counts ---")
        # The Series is already sorted by count in descending order.
        # We can just print it directly.
        print(counts.to_string())
        print("----------------------")

        # --- Save the counts to a new CSV file ---
        try:
            # Convert the Series to a DataFrame to have named columns, then save.
            # 'reset_index' converts the Series index (the license names) into a column.
            counts_df = counts.reset_index()
            counts_df.columns = ['License', 'Count'] # Rename the columns for clarity
            counts_df.to_csv(OUTPUT_COUNTS_CSV, index=False) # index=False prevents writing row numbers
            print(f"\nLicense counts have been successfully saved to '{OUTPUT_COUNTS_CSV}'.")
        except Exception as e:
            print(f"\nAn error occurred while saving the counts to CSV: {e}")

    elif counts is not None:
        print("No licenses were found or counted.")

if __name__ == "__main__":
    main()
