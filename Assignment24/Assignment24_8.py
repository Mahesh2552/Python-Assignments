'''
Q8: Plot a histogram of Math marks.

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
    plt.hist(df['Math'], bins=10, color="skyblue", edgecolor = "black")

    plt.xlabel("Marks")
    plt.ylabel("Number of Students")
    plt.title("Math Marks")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()