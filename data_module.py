import pandas as pd
import matplotlib.pyplot as plt

def display_dataset():
    dataset = pd.read_csv('dataset.csv')
    print(dataset)

def filter_dataset():
    dataset = pd.read_csv('dataset.csv')

    filter_years = input("\nDo you wish to filter by year? ")
    years = ""
    years_list = []
    if filter_years.lower() == "yes":
        while years.lower() != "finish":
            years = input("\nPlease input all years you wish to see data for, or type 'finish' once you have entered all years: ")
            if years.isdigit() == True and 2018 <= int(years) <= 2025:
                years_list.append(int(years))
            elif years.lower() == "finish":
                years_list = [x - 2018 for x in years_list]
            else:
                print("\nPlease enter a year between 2018 and 2025, or type 'finish' if you are done.")
    elif filter_years.lower() == "no":
        pass
    else:
        print("\nPlease input yes or no.")

    filter_column = input("\nDo you wish to filter by column? ")
    columns = ""
    columns_list = []
    if filter_column.lower() == "yes":
        while columns.lower() != "finish":
                columns = input("\nPlease input all columns you wish to see data for, or type 'finish once you have entered all columns: ")
                if columns.isdigit() == True and 0 <= int(columns) <= 21:
                    columns_list.append(int(columns))
                elif columns.lower() == "finish":
                    print("\nHere is your filtered dataset:")
                    if filter_years.lower() == "yes":
                        print(dataset.iloc[years_list,columns_list])
                    elif filter_years.lower() == "no":
                        print(dataset.iloc[:,columns_list])
                else:
                    print("\nPlease enter a column number between 0 and 21, or type 'finish' if you are done.")
    elif filter_column.lower() == "no":
        if filter_years == "no":
            print("\nThen what DO you want to filter?")
        elif filter_years == "yes":
            print("\nHere is your filtered dataset:")
            print(dataset.iloc[years_list,:])
    else:
        print("\nPlease input yes or no.")

def show_visualisation():
    dataset = pd.read_csv('dataset.csv')
    dataset.plot.line(x='Year',
                      y=['Estimated Jobs Eliminated by AI (millions)','Estimated New Jobs Created by AI (millions)'],
                      color=['blue','red'],
                      alpha=0.3,
                      title='Jobs Eliminated by AI vs. Jobs Created by AI',
                      style=".-"
                      )
    plt.show()