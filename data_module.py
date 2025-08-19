import pandas as pd

def display_dataset():
    dataset = pd.read_csv('dataset.csv')
    print(dataset)

def filter_dataset():
    start_range = 0
    print("\n1. Filter by row (year)")
    print("2. Filter by column")
    choice = input("Select an option: ").strip()
    if choice == "1":
        print("\n1. Filter by range")
        print("2. Filter by specific years")
        choice == input("Select an option: ").strip()
        if choice == "1":
            while start_range < 2018:
                start_range = int(input("\nEnter a starting year between 2017 and 2025: "))
                if start_range < 2018: