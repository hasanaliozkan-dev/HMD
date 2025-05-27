import pandas as pd 

data = pd.read_csv("synthetic_missing_data.csv")
print("Original Data:")
print(data.shape)

# Listwise deletion 
data_listwise = data.dropna()
print("Listwise Deletion:")
print(data_listwise.shape)

# Pairwise deletion
data_pairwise = data.copy()
for column in data.columns:
    data_pairwise = data_pairwise.dropna(subset=[column])
print("Pairwise Deletion:")
print(data_pairwise.shape)