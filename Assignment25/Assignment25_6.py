'''
Q6: Replace multiple values in a column using a dictionary.

data = {'Grade': ['A+', 'B', 'A', 'C', 'B+']}

# Replace as:
# 'A+': 'Excellent'
# 'A': 'Very Good'
# 'B+': 'Good'
# 'B': 'Average'
# 'C': 'Poor'

'''

import pandas as pd

def main():
    data = {'Grade': ['A+', 'B', 'A', 'C', 'B+']}

    df = pd.DataFrame(data)

    print("data before values replacemet: \n", df)

    replacement_dict = {
        'A+': 'Excellent',
        'A': 'Very Good',
        'B+': 'Good',
        'B': 'Average',
        'C': 'Poor'
    }

    df['Grade'] = df['Grade'].replace(replacement_dict)

    print("\nDataFrame after replacement:")
    print(df)

if __name__ == "__main__":
    main()