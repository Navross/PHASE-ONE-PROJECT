
import pandas as pd
import matplotlib.pyplot as plt

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

#Save the merged data
merged_df.to_csv("Cleaned_AviationData.csv", index=False)

# Incidents per State
incidents_per_state = merged_df['State'].value_counts().sort_values(ascending=False)
print("Top States by Incidents:")
print(incidents_per_state.head(10))

#visualize incidents per state
plt.figure(figsize=(14, 7))
plt.bar(incidents_per_state.index, incidents_per_state.values, color='steelblue')

plt.xlabel("U.S. State")
plt.ylabel("Number of Aviation Accidents")
plt.title("Aviation Accidents per U.S. State")
plt.xticks(rotation=90)  

plt.tight_layout()
plt.show()

#top 10 states
top_states = incidents_per_state.head(10)

plt.figure(figsize=(10, 6))
plt.bar(top_states.index, top_states.values, color='salmon')
plt.xlabel("U.S. State")
plt.ylabel("Number of Accidents")
plt.title("Top 10 States by Aviation Accidents")
plt.show()

#Incidents by Year

merged_df['Event.Date'] = pd.to_datetime(merged_df['Event.Date'])
merged_df['Year'] = merged_df['Event.Date'].dt.year

yearly_counts = merged_df['Year'].value_counts().sort_index()

plt.figure(figsize=(10, 5))
plt.bar(yearly_counts.index.astype(str), yearly_counts.values)
plt.title("Aviation Incidents per Year")
plt.xlabel("Year")
plt.ylabel("Number of Incidents")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

