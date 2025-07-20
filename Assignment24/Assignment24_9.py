'''
Q9: Rename 'Math' column to 'Mathematics'.

    Name  Math  Science  English  
0   Amit    85       92       75    
1  Sagar    90       88       85    
2  Pooja    78       80       82  

'''

import pandas as pd
from data import data

def main():
    df = pd.DataFrame(data)
    print("Before renaming column name: \n", df)
    
    df.rename(columns={'Math': 'Mathematics'}, inplace=True)
    print("After renaming column name: \n", df)

if __name__ == "__main__":
    main()