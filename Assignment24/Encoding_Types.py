'''LabelEncoder and OneHotEncoder are two distinct methods in Python's scikit-learn library used for converting categorical data into numerical formats, which is a necessary step for most machine learning algorithms.



1. LabelEncoder:
Purpose:
LabelEncoder is used to convert categorical labels into numerical labels. It assigns a unique integer to each unique category in a single column.

Application:
It is typically used for target variables (labels) in classification problems, where the numerical representation does not imply any ordinal relationship. For example, if you have categories "Red", "Green", "Blue", LabelEncoder might assign them 0, 1, 2 respectively.

Considerations:
When applied to features, LabelEncoder can introduce an artificial ordinal relationship between categories, which might mislead models if no such order exists in the data. 

'''


from sklearn.preprocessing import LabelEncoder
import pandas as pd

data = {'color': ['Red', 'Green', 'Blue', 'Red', 'Green']}
df = pd.DataFrame(data)

le = LabelEncoder()
df['color_encoded'] = le.fit_transform(df['color'])
print(df)


'''
2. OneHotEncoder:
Purpose:
OneHotEncoder converts categorical variables into a binary vector representation. For each category, it creates a new binary column, where a '1' indicates the presence of that category and '0' indicates its absence.

Application:
It is generally preferred for features (predictor variables) when the categorical data is nominal (i.e., there is no inherent order between categories). This prevents the model from assuming an ordinal relationship.

Considerations:
OneHotEncoder can increase the dimensionality of the dataset significantly, especially when dealing with categorical features that have a large number of unique categories.

'''

from sklearn.preprocessing import OneHotEncoder
import pandas as pd

data = {'city': ['New York', 'London', 'Paris', 'New York']}
df = pd.DataFrame(data)

ohe = OneHotEncoder(sparse_output=False) # Use sparse_output=False for dense array
encoded_data = ohe.fit_transform(df[['city']])
encoded_df = pd.DataFrame(encoded_data, columns=ohe.get_feature_names_out(['city']))
print(encoded_df)

'''
LabelEncoder: Use for ordinal categorical features where the order of categories has meaning (e.g., ratings like "Good", "Better", "Best"). Use with caution for non-ordinal features, as it can mislead models into assuming an order where none exists.

OneHotEncoder: Use for nominal categorical features where there is no inherent order between categories (e.g., colors like "Red", "Green", "Blue"). 

'''