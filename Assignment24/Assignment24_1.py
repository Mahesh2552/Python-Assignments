'''
Q1: Normalize the 'Math' scores using Min-Max scaling.
data = {
  'Name': ['Amit', 'Sagar', 'Pooja'],
  'Math': [85, 90, 78],
  'Science': [92, 88, 80],
  'English': [75, 85, 82]
}

    Name  Math  Science  English  
0   Amit    85       92       75    
1  Sagar    90       88       85    
2  Pooja    78       80       82    

'''
import pandas as pd
from data import data


def main():
    df = pd.DataFrame(data)

    df['Math_normalized'] = (df['Math'] - df['Math'].min()) / (df['Math'].max() - df['Math'].min())

    print("After Normalizing the Math column: \n", df)

if __name__ == "__main__":
    main()
