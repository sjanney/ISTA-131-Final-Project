from matplotlib import pyplot as plt
import pandas as pd

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


import pandas as pd
import matplotlib.pyplot as plt

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

    # Group by Year and calculate the average rate of Chlamydia cases per year
    avg_rates = filtered_df.groupby('Year')['Rate'].mean().reset_index()

    # Plotting the line graph
    plt.figure(figsize=(10, 6))
    plt.plot(avg_rates['Year'], avg_rates['Rate'], marker='o', linestyle='-', color='b')
    plt.title('Average Rate of Chlamydia Cases in the United States')
    plt.xlabel('Year')
    plt.ylabel('Average Rate (per 100,000 population)')
    plt.grid(True)
    plt.xticks(avg_rates['Year'], rotation=45)
    plt.show()

    # Optionally return the DataFrame containing filtered data
    return filtered_df



average_cases()