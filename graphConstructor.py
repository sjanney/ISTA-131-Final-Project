from matplotlib import pyplot as plt
import pandas as pd
#Data Visualization Library: https://seaborn.pydata.org/ 
import seaborn as sns

def printer(csv):
    data = pd.read_csv(csv)
    return data
    

def data_constructor(df, year=None, state=None):
    '''
    This function takes in a given dataframe object,
    and creates a new DataFrame based on given state and year
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
        # If start or stop years are not specified, use the entire dataset
        filtered_df = df
    # Check if 'Rate' column contains numeric values
    if filtered_df['Rate'].dtype.kind in 'ifc':
        # 'Rate' column is already numeric (float/int), no need to convert
        pass
    else:
        # Convert 'Rate' column to numeric (remove commas and convert to float)
        filtered_df['Rate'] = pd.to_numeric(filtered_df['Rate'].str.replace(',', ''), errors='coerce')
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


def correlation_matrix(correlation="Age group"):
    """
    Generate and visualize the correlation matrix of Chlamydia rates based on a specified correlation parameter.
    
    Args:
    correlation (str): Column name to use for grouping and correlation analysis (e.g., 'Age group', 'Geography', etc.).
                       Default is 'Age group'.
    """
    # Load the CSV data
    df = pd.read_csv('Chlamydia_by_state.csv', thousands=',', na_values=['Data not available', 'null'])
    
    # Convert 'Rate' column to numeric (if it's not already numeric)
    if not pd.api.types.is_numeric_dtype(df['Rate']):
        df['Rate'] = pd.to_numeric(df['Rate'], errors='coerce')
    
    # Group by the specified correlation parameter and calculate average rate for each group
    avg_rates_by_param = df.groupby(correlation)['Rate'].mean().reset_index()
    
    # Display average rates by parameter
    print(f"Average Chlamydia Rates by {correlation}:\n{avg_rates_by_param}\n")
    
    # Create a pivot table to reshape the data (correlation parameter vs. Year)
    pivot_table = df.pivot_table(index=correlation, columns='Year', values='Rate', aggfunc='mean')
    print(pivot_table)
    
    # Compute the correlation matrix
    correlation_matrix = pivot_table.corr()
    
    # Plot correlation matrix as a heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title(f'Correlation Matrix of Chlamydia Rates by {correlation}')
    plt.xlabel('Year')
    plt.ylabel(correlation)
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.show()

correlation_matrix("Population")