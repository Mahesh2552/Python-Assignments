'''
Q3: Apply Label Encoding to a 'City' column.

data = {'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi']}

'''
import pandas as pd
from sklearn.preprocessing import LabelEncoder


def main():
    data = {'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi']}

    df = pd.DataFrame(data)
    print(f"Data before encoding: \n",df)
    le = LabelEncoder()
    df['city_encoded'] = le.fit_transform(df['City'])
    print(f"Data after encoding: \n",df)

if __name__ == "__main__":
    main()