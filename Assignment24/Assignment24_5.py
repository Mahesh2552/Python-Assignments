'''
Q5: Add a new column 'Status' where students with total >= 250 are 'Pass', else 'Fail'.

     Name  Math  Science  English  
0   Amit    85       92       75    
1  Sagar    90       88       85    
2  Pooja    78       80       82  

'''

import pandas as pd
from data import data

def main():
    df = pd.DataFrame(data)
    df_new = df.drop('Name', axis=1) # axis=1 specifies column
    print(df_new)

    df['Total'] = df_new.sum(axis=1)
    df['Status'] = "Fail"

    df.loc[df['Total'] >= 250, 'Status'] = 'Pass'
    df.loc[df['Total'] < 250, 'Status']  = 'Fail'

    print("Data after adding Status Column: \n",df)

if __name__ == "__main__":
    main()