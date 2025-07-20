'''
Q10: Plot a boxplot for English marks to check distribution and outliers.

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

    df.boxplot(column='English')

    plt.title("Boxplot for English marks")

    plt.show()

if __name__ == "__main__":
    main()