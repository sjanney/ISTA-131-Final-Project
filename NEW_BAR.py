import matplotlib.pyplot as plt 
import pandas as pd 

"""
This whole code reads the given csv file and prints out the bar chart from 
the given data 
""" 

# Load data
df = pd.read_csv('chlamydia_by_state.csv')

# Convert data types for safety
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
df['Population'] = pd.to_numeric(df['Population'], errors='coerce')
df['Geography'] = df['Geography']

# Create pivot tables
pivot_df = df.pivot_table(index='Geography', columns='Year', values='Population', aggfunc='sum').fillna(0)
cases_pivot = df.pivot_table(index='Geography', columns='Year', values='Cases', aggfunc='sum').fillna(0)

# Set plot style
plt.style.use('ggplot')
plt.figure(figsize=(12, 8))

# Plotting population data
ax = pivot_df.plot(kind='bar', stacked=True, figsize=(12,8), ax=plt.gca())

# Adding cases data
for year in cases_pivot.columns:
    ax.bar(cases_pivot.index, cases_pivot[year], bottom=pivot_df[year], label=f'Cases in {year}')

# Handle legend to show each year only once
handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))  # Eliminates duplicate labels
plt.legend(by_label.values(), by_label.keys(), title='Year')

# Labeling
plt.xlabel('State')
plt.ylabel('Population and Case Numbers')
plt.title('Population and Number of Chlamydia Cases by State and Year')

# Show the plot
plt.show()
