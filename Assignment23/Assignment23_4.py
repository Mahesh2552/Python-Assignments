'''
Q4: Display students who scored more than 85 in Science.

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

    condition = df['Science'] > 85

    # Filter the DataFrame based on the condition
    filtered_df = df[condition]

    print(Line)
    print(filtered_df)
    
if __name__ == "__main__":
    main()