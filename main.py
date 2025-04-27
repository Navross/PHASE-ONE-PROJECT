
import pandas as pd

#Load AviationData.csv
aviation_df = pd.read_csv("AviationData.csv", encoding='latin-1')

#Load USState_Codes.csv
state_codes_df = pd.read_csv("USState_Codes.csv")


#Preview
print(aviation_df.head())
print(state_codes_df.head())

#Clean the Aviation Data
#rows with missing values in key columns
aviation_df_cleaned = aviation_df.dropna(subset=['Location', 'Event.Date'])

aviation_df_cleaned['State'] = aviation_df_cleaned['Location'].str.extract(r',\s*([A-Z]{2})')

#Merge with State Codes
merged_df = pd.merge(aviation_df_cleaned, state_codes_df, left_on='State', right_on='Abbreviation', how='left')
print(merged_df[['Location', 'State']].head())

# Incidents per State
incidents_per_state = merged_df['State'].value_counts()
print("Top States by Incidents:")
print(incidents_per_state.head(10))

#Incidents by Year
import matplotlib.pyplot as plt

merged_df['Event.Date'] = pd.to_datetime(merged_df['Event.Date'], errors='coerce')
merged_df['Year'] = merged_df['Event.Date'].dt.year

yearly_counts = merged_df['Year'].value_counts().sort_index()

plt.figure(figsize=(12, 6))
plt.bar(yearly_counts.index.astype(str), yearly_counts.values)
plt.title("Aviation Incidents per Year")
plt.xlabel("Year")
plt.ylabel("Number of Incidents")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
