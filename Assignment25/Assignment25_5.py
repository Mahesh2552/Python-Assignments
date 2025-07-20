'''
Q5: Create a DataFrame with 'Age' and 'Purchased' columns and split into train/test sets.

data = {'Age': [22, 25, 47, 52, 46, 56], 'Purchased': [0, 1, 1, 0, 1, 0]}

'''

import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    data = {'Age': [22, 25, 47, 52, 46, 56], 'Purchased': [0, 1, 1, 0, 1, 0]}

    df = pd.DataFrame(data)

    x = df.drop("Purchased", axis = "columns") 
    y = df['Purchased']

    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=42)

    print("Dimention of X_train is: ",x_train.shape) 
    print("Dimention of X_test is: ",x_test.shape) 
    print("Dimention of Y_train is: ",y_train.shape) 
    print("Dimention of Y_test is: ",y_test.shape)  

if __name__ == "__main__":
    main()