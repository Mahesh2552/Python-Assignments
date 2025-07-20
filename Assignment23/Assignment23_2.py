'''
Q2: Use the DataFrame from Q1 and print descriptive statistics using .describe().

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

    print("Data Statistics is : ")
    print(Line)
    print(df.describe())
    print(Line)

if __name__ == "__main__":
    main()