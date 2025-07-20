'''
Q2: Create a gender column and perform one-hot encoding.
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
from sklearn.preprocessing import OneHotEncoder


def main():
    df = pd.DataFrame(data)

    df['Gender'] = ['Male','Male','Female']

    print("After Adding the Gender column: \n", df)

    ohe = OneHotEncoder(sparse_output=False) # Use sparse_output=False for dense array, returns NumPy array instead of sparse matrix

    #Apply OneHotEncoder on 'Gender' column
    encoded_data = ohe.fit_transform(df[['Gender']])
    # print(encoded_data)

    #Create a new DataFrame for encoded columns
    encoded_df = pd.DataFrame(encoded_data, columns=ohe.get_feature_names_out(['Gender']))
    print(encoded_df)

if __name__ == "__main__":
    main()



