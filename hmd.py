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

# Mean imputation
data_mean_imputed = data.copy()
for column in data_mean_imputed.columns:
    if data_mean_imputed[column].isnull().any():
        mean_value = data_mean_imputed[column].mean()
        data_mean_imputed[column].fillna(mean_value, inplace=True)
print("Mean Imputation:")
print(data_mean_imputed.shape)

# Median imputation
data_median_imputed = data.copy()
for column in data_median_imputed.columns:
    if data_median_imputed[column].isnull().any():
        median_value = data_median_imputed[column].median()
        data_median_imputed[column].fillna(median_value, inplace=True)
print("Median Imputation:")
print(data_median_imputed.shape)

# Mode imputation
data_mode_imputed = data.copy()
for column in data_mode_imputed.columns:
    if data_mode_imputed[column].isnull().any():
        mode_value = data_mode_imputed[column].mode()[0]
        data_mode_imputed[column].fillna(mode_value, inplace=True)
print("Mode Imputation:")
print(data_mode_imputed.shape)


