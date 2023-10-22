# Define a function for reading a dataset from a CSV file
def Import(path):
    import pandas as pd
    data = pd.read_csv(path)
    return data
