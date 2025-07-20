'''
Q9: Create a DataFrame with missing values and fill them with column mean.

data2 = {
  'Name': ['Amit', 'Sagar', 'Pooja'],
  'Math': [np.nan, 76, 88],
  'Science': [91, np.nan, 85]
}
'''

import pandas as pd
from data import data2

def main():
    Line = "-"*80
    df = pd.DataFrame(data2)
    print("Before Filling with mean value")
    print(Line)
    print(df)
    print(Line)

    df['Math'] = df['Math'].fillna(df['Math'].mean())
    df['Science'] = df['Science'].fillna(df['Science'].mean())
    
    print("Before Filling with mean value")
    print(Line)
    print(df)

if __name__ == "__main__":
    main()