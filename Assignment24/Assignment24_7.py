'''

Q7: Export the final DataFrame to a CSV file.

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

    df['Total'] = df_new.sum(axis=1)
    df['Status'] = "Fail"

    df.loc[df['Total'] >= 250, 'Status'] = 'Pass'
    df.loc[df['Total'] < 250, 'Status']  = 'Fail'

    print("Data after adding Status Column: \n",df)

    df.to_csv('final_data.csv', index=False)

if __name__ == "__main__":
    main()