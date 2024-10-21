import pandas as pd
import numpy as np


data = pd.read_csv("melb_data.csv")

categorical_cols = [col for col in data.columns if data[col].dtype == "object" and data[col].nunique() < 10]
print("\n\nBefore Encoding -\n")
print(data[categorical_cols])

for col in categorical_cols:
    ordinal_dict = {}
    ordinal_num = 1
    for category in set(data[col]):
        ordinal_dict[category] = ordinal_num
        ordinal_num +=1
    data[col] = [ordinal_dict[x] for x in data[col]]

print("\n\nAfter Encoding -\n")
print(data[categorical_cols])