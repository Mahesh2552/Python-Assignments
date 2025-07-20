'''
Q9: Replace values in 'Marks' less than 50 with 'Fail' using where().

data = {'Marks': [45, 67, 88, 32, 76]}

'''
import pandas as pd

def main():
    data = {'Marks': [45, 67, 88, 32, 76]}

    df = pd.DataFrame(data)

    print("Data before replacement: \n",df)

    df.loc[df['Marks'] < 50, 'Marks'] = "Fail"

    print("Data after replacement: \n",df)

if __name__ == "__main__":
    main()