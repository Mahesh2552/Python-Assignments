'''
Q3: Group students by gender and calculate average marks.

     Name  Math  Science  English  Gender
0   Amit    85       92       75    Male
1  Sagar    90       88       85    Male
2  Pooja    78       80       82  Female

'''

import pandas as pd
from data import data

def main():
    df = pd.DataFrame(data)
    df['Gender'] = ['Male','Male','Female']

    average_by_gender = df.groupby('Gender')[['Math','Science','English']].mean()

    print("Average marks of students group by gender:\n ",average_by_gender)

if __name__ == "__main__":
    main()

