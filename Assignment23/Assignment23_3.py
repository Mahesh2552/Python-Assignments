'''
Q3: Add a new column 'Total' to the DataFrame as the sum of all subject marks.

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
    Line = "-" * 80
    df = pd.DataFrame(data)
    df_new = df.drop('Name', axis=1) # axis=1 specifies column
    print(df_new)
    df['Total'] = df_new.sum(axis=1)
    print(Line)
    print(df.head())
    print(Line)

if __name__ == "__main__":
    main()