
import pandas as pd

#Load AviationData.csv
aviation_df = pd.read_csv("AviationData.csv", encoding='latin-1')
#except UnicodeDecodeError
aviation_df = pd.read_csv("AviationData.csv", encoding='cp1252')
#Load USState_Codes.csv
state_codes_df = pd.read_csv("USState_Codes.csv", encoding='latin-1')
#except UnicodeDecodeError:
state_codes_df = pd.read_csv("USState_Codes.csv", encoding='cp1252')

#Preview
print(aviation_df.head())
print(state_codes_df.head())

#Clean the Aviation Data
#rows with missing values in key columns
aviation_df_cleaned = aviation_df.dropna(subset=['Location', 'Event.Date'])

#Extract 2-letter state code from the Location
aviation_df_cleaned['State'] = aviation_df_cleaned['Location'].str.extract(r',\s*([A-Z]{2})')
