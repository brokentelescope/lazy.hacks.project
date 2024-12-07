import pandas as pd

def calculate_correlation(file1, file2):
    try:
        # Load the datasets with date parsing
        df1 = pd.read_csv(file1, parse_dates=['Date'])
        df2 = pd.read_csv(file2, parse_dates=['Date'])

        # Set 'Date' as index for both DataFrames and sort by index
        df1.set_index('Date', inplace=True)
        df2.set_index('Date', inplace=True)

        # Align both DataFrames based on index
        df1, df2 = df1.align(df2, join='inner')  # Inner join aligns only overlapping indices
        
        # Calculate correlation only if there are common dates
        if not df1.empty and not df2.empty:
            correlation_matrix = df1.corrwith(df2)
            return correlation_matrix
        else:
            return "No common data to correlate."

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    file1 = 'first_dataset.csv'
    file2 = 'second_dataset.csv'

    correlation_result = calculate_correlation(file1, file2)

    if isinstance(correlation_result, pd.Series):
        print("Correlation between the datasets:\n", correlation_result)
    else:
        print("Error:", correlation_result)
