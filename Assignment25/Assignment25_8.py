'''
Q8: Fill missing values in a numeric column using interpolation.

data = {'Marks': [85, np.nan, 90, np.nan, 95]}

'''

import pandas as pd
import numpy as np

def main():
    data = {'Marks': [85, np.nan, 90, np.nan, 95]}

    df = pd.DataFrame(data)

    print("\nDataFrame before interpolation:\n",df)

    df['Marks'] = df['Marks'].interpolate()

    print("\nDataFrame after interpolation:\n")
    
    print(df)

if __name__ == "__main__":
    main()