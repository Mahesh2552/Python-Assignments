'''
Q7: Create a bar plot of student names vs total marks.

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
    Line = "-" * 80
    df = pd.DataFrame(data)
    df_new = df.drop('Name', axis=1) # axis=1 specifies column
    df['Total'] = df_new.sum(axis=1)
    df.plot.bar(x="Name",y="Total")
    plt.show()

if __name__ == "__main__":
    main()