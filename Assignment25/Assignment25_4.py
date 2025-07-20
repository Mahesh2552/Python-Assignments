'''
Q4: Apply One-Hot Encoding to a 'Department' column.

data = {'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']}

'''
import pandas as pd
from sklearn.preprocessing import OneHotEncoder


def main():
    data = {'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']}

    df = pd.DataFrame(data)

    ohe = OneHotEncoder(sparse_output=False) # Use sparse_output=False for dense array, returns NumPy array instead of sparse matrix (sparse martrix => matrix with multiple zero entries)

    # Apply OneHotEncoder on 'Gender' column
    encoded_data = ohe.fit_transform(df[['Department']])
    print(encoded_data)

    #Create a new DataFrame for encoded columns
    encoded_df = pd.DataFrame(encoded_data, columns=ohe.get_feature_names_out(['Department']))
    print(encoded_df)

if __name__ == "__main__":
    main()