from matplotlib import pyplot as plt 
import pandas as pd 

"""
This whole code reads the given csv file and prints out the bar chart from 
the given data 
""" 
df = pd.DataFrame('chlamydia_by_state.csv')
plt.style.use('ggplot') #plot style 

plt.figure(figsize = (12,8)) #setting figure size

#Creating Bars for year and cases
plt.bar(df['Year'], df['Cases'], label = 'Case #', color = 'r') 

#Creating a stacked bar chart for the amount of cases vs Population
plt.bar(df['Year'], df['Population'], bottom = df['Cases'], label = 'Population #', color = 'b')

#labeling x and y axis and title
plt.xlabel('Years')
plt.ylabel('Case Number')
plt.title('Case Number of Chlamdia Rates Each Year')
plt.show()
