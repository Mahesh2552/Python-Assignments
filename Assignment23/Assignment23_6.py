'''
Q6: Sort the DataFrame by 'Total' marks in descending order

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
    df['Total'] = df_new.sum(axis=1)
    sorted_df = df.sort_values(by='Total', ascending=False)
    print(Line)
    print(sorted_df)
    print(Line)    


if __name__ == "__main__":
    main()