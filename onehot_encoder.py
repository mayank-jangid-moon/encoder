import pandas as pd
import numpy as np

data = pd.read_csv("melb_data.csv")

categorical_cols = [col for col in data.columns if data[col].dtype == "object"  and data[col].nunique() < 10]

one_hot_encoded_data = {}
hotted = []
for col in categorical_cols:
    unique_values = data[col].unique()
    for value in unique_values:
        hotted.append(col + '_' + str(value))
        one_hot_encoded_data[col + '_' + str(value)] = np.where(data[col] == value, 1, 0)


data = pd.concat([data, pd.DataFrame(one_hot_encoded_data)], axis=1)

data = data.drop(columns=categorical_cols)

print(data[hotted])
