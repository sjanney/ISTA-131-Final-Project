import pandas as pd
import datetime
import matplotlib.pyplot
import datetime

def data_parse(csv):
    data = pd.read_csv(csv)
    print(data)

def main():
    input_file = "chlamydia_by_state.csv"
    data_parse(input_file)

if __name__ == "__main__":
    main()
