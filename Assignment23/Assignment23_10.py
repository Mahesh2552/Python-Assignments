'''
Q10: Drop the 'English' column from the original DataFrame.

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
  print("Data before column drop")
  print(df)
  print(Line)

  df.drop('English', axis=1, inplace=True)
  print("Data after column drop")
  print(df)
  print(Line)

if __name__ == "__main__":
    main()