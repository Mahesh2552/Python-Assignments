'''
Q4: Plot a pie chart of subject marks for 'Sagar'.

     Name  Math  Science  English  
0   Amit    85       92       75    
1  Sagar    90       88       85    
2  Pooja    78       80       82  

'''

import pandas as pd
from data import data
import matplotlib.pyplot as plt

def main():
    df = pd.DataFrame(data)

    #Filter row for Sagar and drop the 'Name' column
    sagar_data = df[df['Name'] == 'Sagar'].drop('Name', axis=1)
    print(sagar_data)
    
    plt.figure(figsize=(6, 6))
    plt.pie(sagar_data.values.flatten(),labels=sagar_data.columns,autopct='%1.1f%%',startangle=140)

    plt.title("Sagar's Marks: ")
    plt.tight_layout()  #Adjusts spacing to prevent overlap
    plt.show()

if __name__ == "__main__":
    main()