import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


class Eda:
    def __init__(self, data):
        """
        Initialize the DataExplorer object with the input DataFrame.

        Parameters:
        - data (pd.DataFrame): The input DataFrame to be explored.
        """
        self.data = data

    def display_basic_statistics(self):
        """
        Display basic statistics of the dataset.

        Returns:
        - pd.DataFrame: Basic statistics of the dataset.
        """
        stats = self.data.describe()
        print("Basic Statistics:")
        print(stats)
        return stats

    def display_missing_values(self):
        """
        Display missing values in the dataset.

        Returns:
        - pd.Series: Missing values count for each column.
        """
        missing_values = self.data.isnull().sum()
        print("\nMissing Values:")
        print(missing_values)
        return missing_values

    def display_data_types(self):
        """
        Display data types of columns in the dataset.

        Returns:
        - pd.Series: Data types of each column.
        """
        data_types = self.data.dtypes
        print("\nData Types:")
        print(data_types)
        return data_types

    def display_correlation_matrix(self):
        """
        Display the correlation matrix for numerical columns in the dataset.

        Returns:
        - pd.DataFrame: Correlation matrix for numerical columns.
        """
        numerical_columns = self.data.select_dtypes(include=[np.number]).columns
        if len(numerical_columns) > 0:
            correlation_matrix = self.data[numerical_columns].corr()
            plt.figure(figsize=(12, 8))
            sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
            plt.title("Correlation Matrix")
            plt.show()
            return correlation_matrix
        else:
            print("No numerical columns for correlation matrix.")
            return None

    def display_numerical_distribution(self):
        """
        Display histograms for the distribution of numerical columns in the dataset.

        Returns:
        - Histogram
        """
        numerical_columns = self.data.select_dtypes(include=[np.number]).columns
        for col in numerical_columns:
            plt.figure(figsize=(10, 6))
            self.data[col].hist(bins=20)
            plt.title(f"Distribution of {col}")
            plt.xlabel(col)
            plt.ylabel("Frequency")
            plt.show()

    def display_boxplot_outliers(self):
        """
        Display a boxplot for outlier detection in numerical columns.

        Returns:
        - Histogram of boxplot
        """
        numerical_columns = self.data.select_dtypes(include=[np.number]).columns
        plt.figure(figsize=(15, 8))
        sns.boxplot(data=self.data[numerical_columns].tail(100))
        plt.title("Boxplot for Outlier Detection")
        plt.show()

    def display_categorical_counts(self):
        """
        Display count plots for categorical columns in the dataset.

        Returns:
        - Histogram of count plot
        """
        categorical_columns = self.data.select_dtypes(include=["object"]).columns
        for col in categorical_columns:
            plt.figure(figsize=(10, 6))
            sns.countplot(x=col, data=self.data.tail(100))
            plt.title(f"Count plot for {col}")
            plt.show()
