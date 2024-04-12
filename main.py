import pandas as pd
import datetime
import matplotlib.pyplot
import datetime

def data_parse(csv):
    data = pd.read_csv(csv)
    return data


def data_constructor(df,year=None,state=None):
    '''
    This function takes in a given dataframe object,
    and creates a new DataFrame based on specific types
    of inputs give
    '''
    filtered_data = df[(df['Indicator'] == 'Chlamydia') & (df['Year'] == year) & (df['Geography']==state)]
    return filtered_data



def main():
    input_file = "chlamydia_by_state.csv"
    df = data_parse(input_file)
    for i in range(2000,2016):
        print(data_constructor(df,i,"California"))

if __name__ == "__main__":
    main()

