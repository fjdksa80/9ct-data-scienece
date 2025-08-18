import pandas as pd

def display_dataset():
    dataset = pd.read_csv('dataset.csv')
    print(dataset)