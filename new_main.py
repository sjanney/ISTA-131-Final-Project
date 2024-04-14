import pandas as pd
import datetime
import matplotlib.pyplot
import datetime
import graphConstructor as graph

#Main area for creating specific graphs, correlations,etc
def main():
    input_file = input("Please enter the given csv file: ")
    df = graph.constructor(input_file)
    for i in range(2000,2016):
        print(graph.data_constructor(df,i,"California"))

if __name__ == "__main__":
    main()

