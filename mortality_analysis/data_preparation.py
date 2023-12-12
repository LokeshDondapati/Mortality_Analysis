import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import SelectKBest, f_classif
from scipy.stats import zscore


class DataPreparation:
    def __init__(self, merged_data, target_column):
        """
        Initialize the DataPreparer object with input data and target column.

        Parameters:
        - merged_data (pd.DataFrame): The input dataset to be prepared.
        - target_column (str): The target column for the machine learning task.
        """
        self.merged_data = merged_data
        self.target_column = target_column

    def prepare_data(self):
        """
        Prepare the dataset for machine learning tasks by handling missing values, encoding categorical variables,
        and selecting the top k features based on correlation with the target column.

        Returns:
        - Prepared dataset ready for machine learning.
        """
        print("Data Preparation:")

        print("Number of rows in the merged dataset:", len(self.merged_data))
        print("Columns in the merged dataset:", self.merged_data.columns)

        self.handle_missing_values()
        self.encode_categorical_variables()

        k = 9
        self.select_top_k_features(k)

        return self.merged_data

    def handle_missing_values(self):
        """
        Handle missing values in the dataset using mean imputation for numerical columns
        and most frequent imputation for categorical columns.

        Note:
        - This function modifies the input dataset in-place.
        """
        # Check if there are numeric columns
        numerical_columns = self.merged_data.select_dtypes(include=["number"]).columns
        if not numerical_columns.empty:
            print("Handling missing values for numeric columns.")
            # Filter out columns with all missing values
            valid_numerical_columns = self.merged_data[numerical_columns].columns[
                self.merged_data[numerical_columns].notna().any()
            ]
            if not valid_numerical_columns.empty:
                imputer = SimpleImputer(strategy="mean")
                self.merged_data[valid_numerical_columns] = imputer.fit_transform(
                    self.merged_data[valid_numerical_columns]
                )

        # Check if there are categorical columns
        categorical_columns = self.merged_data.select_dtypes(include=["object"]).columns
        if not categorical_columns.empty:
            print("Handling missing values for categorical columns.")
            imputer = SimpleImputer(strategy="most_frequent")
            self.merged_data[categorical_columns] = imputer.fit_transform(
                self.merged_data[categorical_columns]
            )

    def handle_outliers(self, method="IQR"):
        """
        Handle outliers in the DataFrame using the specified method.

        Parameters:
        - method: str, method for handling outliers ('IQR' or 'Z-score')

        Returns:
        - data: pandas DataFrame, with outliers handled
        """
        numerical_columns = self.merged_data.select_dtypes(include=[np.number]).columns

        if method == "IQR":
            for col in numerical_columns:
                Q1 = self.merged_data[col].quantile(0.25)
                Q3 = self.merged_data[col].quantile(0.75)
                IQR = Q3 - Q1
                self.merged_data = self.merged_data[
                    ~(
                        (self.merged_data[col] < (Q1 - 1.5 * IQR))
                        | (self.merged_data[col] > (Q3 + 1.5 * IQR))
                    )
                ]
        elif method == "Z-score":
            z_scores = np.abs(zscore(self.merged_data[numerical_columns]))
            self.merged_data = self.merged_data[(z_scores < 3).all(axis=1)]
        else:
            raise ValueError("Invalid method. Please choose 'IQR' or 'Z-score'.")

    def encode_categorical_variables(self):
        """
        Encode categorical variables in the dataset using LabelEncoder.

        Note:
        - This function modifies the input dataset in-place.
        """
        label_encoder = LabelEncoder()

        categorical_columns = self.merged_data.select_dtypes(include=["object"]).columns
        for column in categorical_columns:
            self.merged_data[column] = label_encoder.fit_transform(
                self.merged_data[column]
            )

    def select_top_k_features(self, k):
        """
        Select the top k features based on their correlation with the target column.

        Parameters:
        - k (int): Number of top features to select.

        Note:
        - This function modifies the input dataset in-place.
        """
        correlation_matrix = self.merged_data.corr()
        target_correlation = (
            correlation_matrix[self.target_column].abs().sort_values(ascending=False)
        )
        selected_features = target_correlation[1 : k + 1].index
        self.merged_data = pd.concat(
            [self.merged_data[selected_features], self.merged_data[self.target_column]],
            axis=1,
        )


# Example Usage:
# Assuming 'df' is your DataFrame and 'target_col' is the target column
# preparer = DataPreparer(df, target_col)
# prepared_data = preparer.prepare_data()
