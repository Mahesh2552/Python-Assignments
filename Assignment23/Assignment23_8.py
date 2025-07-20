'''
Q8: Plot a line chart of marks for 'Amit' across all subjects.

data = {
  'Name': ['Amit', 'Sagar', 'Pooja'],
  'Math': [85, 90, 78],
  'Science': [92, 88, 80],
  'English': [75, 85, 82]
}
'''

import pandas as pd
from data import data
import matplotlib.pyplot as plt

def main():
    df = pd.DataFrame(data)
    print(df)
    Amit_row = df[df['Name'] == 'Amit'].drop('Name', axis=1)
    Amit_row_transposed = Amit_row.T

    print(Amit_row_transposed)
    Amit_row_transposed.plot(kind='line', title='Amit\'s Marks')
    plt.show()


if __name__ == "__main__":
    main()