from matplotlib import pyplot as plt
import pandas as pd
#Data Visualization Library: https://seaborn.pydata.org/ 
import seaborn as sns

"""
Graph Constructor
This group of functions are created to help us create different types of visualizations
based of specific types of parameters that we want to use/share with the given datasets.
All of these vary from specific types of printing, correlation, and creation of specific
types of other types of statistical analysis. 

"""


def constructor(csv):
    """
    Simply prints out the given csv
    
    Args
    csv (String): A csv file name
    """
    data = pd.read_csv(csv)
    return data
    

def data_constructor(df, year=None, state=None):
    '''
    This function takes in a given dataframe object,
    and creates a new DataFrame based on given state and year


    Args:
    df (DataFrame Object): A given DataFrame, preferably of all data.
    year (int): Given specfic year of data, defaults to all.
    state (string): Collects specific state with data for DataFrame creation.
    '''
    filtered_data = df[(df['Indicator'] == 'Chlamydia') & 
                           (df['Year'] == year) & 
                           (df['Geography'] == state)]
    return filtered_data



def average_cases(start=None, stop=None):
    """
    Calculate and plot the average rate of Chlamydia cases between specific time periods.
    
    Args:
    start (int): Starting year (inclusive) for filtering the data.
    stop (int): Ending year (inclusive) for filtering the data.
    """
    # Read the CSV file into a DataFrame
    df = pd.read_csv('Chlamydia_by_state.csv', thousands=',', na_values=['Data not available', 'null'])
    # Filter the DataFrame based on the specified time period (start to stop years)
    if start is not None and stop is not None:
        filtered_df = df[(df['Year'] >= start) & (df['Year'] <= stop)]
    else:
        filtered_df = df
    # Grouping everything by year and calculating all of the averages of each year
    avg_rates = filtered_df.groupby('Year')['Rate'].mean().reset_index()
    # Plotting the line graph
    plt.figure(figsize=(10, 6))
    plt.plot(avg_rates['Year'], avg_rates['Rate'], marker='o', linestyle='-', color='b')
    #Main title of line graph
    plt.title('Average Rate of Chlamydia Cases in the United States')
    #Axies
    plt.xlabel('Year')
    plt.ylabel('Average Rate (per 100,000 population)')
    plt.grid(True)
    #Each iteration by 45 
    plt.xticks(avg_rates['Year'], rotation=45)
    plt.show()
    # Optionally return the DataFrame containing filtered data
    return filtered_df


def scatterplot(csv_file):
    """
   This function creates a csv file with given parameters

    Args:
        csv_file (str): Path to the CSV file.
    """
    x_column = 'Rate'
    y_column = 'Cases'
    hue_column = "Geography"

    # Load CSV into a DataFrame
    df = pd.read_csv(csv_file)

    # Convert string numbers nums
    df[x_column] = pd.to_numeric(df[x_column], errors='coerce')
    df[y_column] = pd.to_numeric(df[y_column].str.replace(',', ''), errors='coerce')

    # Plotting
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x_column, y=y_column, hue=hue_column, s=100)
    plt.title(f"{y_column} vs. {x_column} by {hue_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.grid(True)
    plt.show()

def plot_cases_by_year(csv_file, state):
    df = pd.read_csv(csv_file)

    # Filter data for the specified state
    state_data = df[df['Geography'] == state]

    # Ensure 'Year' column is treated as numeric
    state_data['Year'] = pd.to_numeric(state_data['Year'])

    # Group data by year and sum the cases
    yearly_cases = state_data.groupby('Year')['Cases'].sum()

    # Plotting the bar graph
    plt.figure(figsize=(10, 6))
    plt.bar(yearly_cases.index, yearly_cases.values, color='skyblue')
    plt.title(f"Number of Cases Over Years in {state}")
    plt.xlabel("Year")
    plt.ylabel("Number of Cases")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.show()


plot_cases_by_year('chlamydia_by_state.csv','Arizona')
average_cases()
scatterplot('chlamydia_by_state.csv')