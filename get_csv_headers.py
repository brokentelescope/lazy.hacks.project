import pandas as pd

def get_csv_headers(file_path):
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        # Return the column headers
        return df.columns.tolist()
    except Exception as e:
        # Handle any exceptions that may occur
        return str(e)

# Example usage
file_path = 'path/to/your/csvfile.csv'
headers = get_csv_headers(file_path)
print("Column headers:", headers)
