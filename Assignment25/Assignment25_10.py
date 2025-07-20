'''
Q10: Split a DataFrame with multiple features into train-test for supervised learning.

data = {
  'Age': [25, 30, 45, 35, 22],
  'Salary': [50000, 60000, 80000, 65000, 45000],
  'Purchased': [1, 0, 1, 0, 1]
}
'''
import pandas as pd
from sklearn.model_selection import train_test_split

def main():
  Line = "-"*80
  data = {
    'Age': [25, 30, 45, 35, 22],
    'Salary': [50000, 60000, 80000, 65000, 45000],
    'Purchased': [1, 0, 1, 0, 1]
  }

  df = pd.DataFrame(data)

  print(df)

  x = df.drop("Purchased", axis = "columns") 
  y = df['Purchased']

  x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=42)

  print(Line)
  print("X_train is: \n",x_train) 
  print("Dimention of X_train is: ",x_train.shape)
  print(Line)
  print("X_test is: \n",x_test) 
  print("Dimention of X_test is: ",x_test.shape) 
  print(Line)
  print("Y_train is:\n ",y_train) 
  print("Dimention of Y_train is: ",y_train.shape) 
  print(Line)
  print("Y_test is: \n",y_test) 
  print("Dimention of Y_test is: ",y_test.shape)  

if __name__ == "__main__":
    main()