import pandas as pd

# Load the dataset
file_path = "C:/Users/HP/Desktop/excelca2project/covid19dataset.xlsx"  # Replace with your file path
df = pd.read_excel(file_path, sheet_name='COVID-19_Daily_Counts_of_Cases_', engine='openpyxl')

# Standardize the date format
df['date_of_interest'] = pd.to_datetime(df['date_of_interest'], errors='coerce', dayfirst=False)

# Drop irrelevant columns (probable and 7-day avg columns)
columns_to_drop = [col for col in df.columns if '7DAY_AVG' in col or 'PROBABLE' in col]
df_cleaned = df.drop(columns=columns_to_drop)

# Drop rows with null or invalid dates
df_cleaned = df_cleaned.dropna(subset=['date_of_interest'])

# Fill remaining missing values with 0
df_cleaned = df_cleaned.fillna(0)

# Save the cleaned dataset
cleaned_file_path = "covid19dataset_cleaned.xlsx"  # Output file name
df_cleaned.to_excel(cleaned_file_path, index=False)

print(f"Cleaned dataset saved as: {cleaned_file_path}")
