'''
Q1: Create a DataFrame for student marks and print basic information like shape, columns, and data types.

data = {
  'Name': ['Amit', 'Sagar', 'Pooja'],
  'Math': [85, 90, 78],
  'Science': [92, 88, 80],
  'English': [75, 85, 82]
}
'''
import pandas as pd
from data import data

def main():
    Line = "-"*80

    df = pd.DataFrame(data)

    print(Line)
    print("Shape of DataFrame:",df.shape)  
    print(Line)
    print(df.head())
    print(Line)

    print("Columns are : ")
    print(df.columns)
    print(Line)

    print("Data types: ")
    print(df.dtypes)
    print(Line)

if __name__ == "__main__":
    main()