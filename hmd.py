import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.impute import KNNImputer

from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
"""
Columns:
ID -> Unique identifier for each customer: integer
Age -> Age of the customer: integer
Gender -> Gender of the customer: categorical
Education Level -> Education level of the customer : categorical
Income -> Income of the customer: float
Satisfaction Rating -> Customer satisfaction rating: float
Purchased Product -> Product purchased by the customer: categorical
"""
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
# Note: Mean imputation will only work for numerical columns
data_mean_imputed = data.copy()
for column in data_mean_imputed.select_dtypes(include=['float64', 'int64']).columns:
    if data_mean_imputed[column].isnull().any():
        mean_value = data_mean_imputed[column].mean()
        data_mean_imputed[column] = data_mean_imputed[column].fillna(mean_value)
print("Mean Imputation:")
print(data_mean_imputed.shape)  


# Median imputation
# Note: Median imputation will only work for numerical columns
data_median_imputed = data.copy()
for column in data_median_imputed.select_dtypes(include=['float64', 'int64']).columns:
    if data_median_imputed[column].isnull().any():
        median_value = data_median_imputed[column].median()
        data_median_imputed[column] = data_median_imputed[column].fillna(median_value)
print("Median Imputation:")
print(data_median_imputed.shape)    

# Mode imputation
# Note: Mode imputation will only work for categorical columns
data_mode_imputed = data.copy()
for column in data_mode_imputed.select_dtypes(include=['object']).columns:
    if data_mode_imputed[column].isnull().any():
        mode_value = data_mode_imputed[column].mode()[0]
        data_mode_imputed[column] = data_mode_imputed[column].fillna(mode_value)
print("Mode Imputation:")
print(data_mode_imputed.shape)




# Regression imputation

data_regression_imputed = data.copy()
for column in data_regression_imputed.select_dtypes(include=['float64', 'int64']).columns:
    if data_regression_imputed[column].isnull().any():
        # Identify categorical columns
        categorical_cols = data_regression_imputed.select_dtypes(include=['object']).columns

        # One-hot encode categorical columns
        data_encoded = pd.get_dummies(data_regression_imputed, columns=categorical_cols, dummy_na=False)

        # Prepare data for regression
        # Combine X and y, then dropna, then split
        data_subset = data_encoded[[column] + list(data_encoded.columns.drop(column))]
        data_subset = data_subset.dropna()
        X = data_subset.drop(columns=[column])
        y = data_subset[column]

        # Train the model
        model = LinearRegression()
        model.fit(X, y)

        # Predict the missing values
        missing_mask = data_regression_imputed[column].isnull()
        missing_indices = data_regression_imputed[missing_mask].index

        # Prepare the missing data for prediction
        missing_data = data_regression_imputed.loc[missing_indices].copy()

        # One-hot encode the missing data
        missing_data_encoded = pd.get_dummies(missing_data, columns=categorical_cols, dummy_na=False)

        # Ensure that the columns in the missing data match the columns used for training
        X_train_cols = X.columns
        for col in X_train_cols:
            if col not in missing_data_encoded.columns:
                missing_data_encoded[col] = 0  # Add missing columns with 0
        missing_data_encoded = missing_data_encoded[X_train_cols]  # Ensure correct order

        X_missing = missing_data_encoded.drop(columns=[column], errors='ignore')

        # Predict the missing values
        predicted_values = model.predict(X_missing)

        # Fill the missing values
        data_regression_imputed.loc[missing_mask, column] = predicted_values

print("Regression Imputation:")
print(data_regression_imputed.shape)

# kNN imputation

numerical_data = data.select_dtypes(include=['number'])
knn_imputer = KNNImputer(n_neighbors=5)
data_knn_imputed = knn_imputer.fit_transform(numerical_data)
data_knn_imputed = pd.DataFrame(data_knn_imputed, columns=numerical_data.columns)
print("KNN Imputation:")
print(data_knn_imputed.shape)




# Expectation-Maximization (EM) imputation
numerical_data = data.select_dtypes(include=['number'])
em_imputer = IterativeImputer(max_iter=10, random_state=0)
data_em_imputed = em_imputer.fit_transform(numerical_data)
data_em_imputed = pd.DataFrame(data_em_imputed, columns=numerical_data.columns)
print("Expectation-Maximization Imputation:")
print(data_em_imputed.shape)

# Display the final imputed datasets
print("\nFinal Imputed Datasets:")
print("Listwise Deletion Shape:", data_listwise.shape)
print("Pairwise Deletion Shape:", data_pairwise.shape)
print("Mean Imputation Shape:", data_mean_imputed.shape)
print("Median Imputation Shape:", data_median_imputed.shape)
print("Mode Imputation Shape:", data_mode_imputed.shape)
print("Regression Imputation Shape:", data_regression_imputed.shape)
print("KNN Imputation Shape:", data_knn_imputed.shape)
print("Expectation-Maximization Imputation Shape:", data_em_imputed.shape)      

