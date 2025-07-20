'''
Q5: Replace 'Pooja' with 'Puja' in the 'Name' column.

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

    df['Name'] = df['Name'].replace('Pooja', 'Puja')

    print(df)


if __name__ == "__main__":
    main()