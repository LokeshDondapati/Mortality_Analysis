import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class DiseaseInfluence:
    def __init__(self, data):
        """
        Initialize the DiseaseInfluenceAnalyzer object with mortality data.

        Parameters:
        - data (pd.DataFrame): DataFrame containing mortality data, including columns for diseases of interest and
          'Total Deaths'.
        """
        self.data = data

    def analyze_and_visualize(self):
        """
        Analyze and visualize the correlation between specific diseases and overall death rates.

        Returns:
        - pd.Series: Correlation coefficients between each specified disease and overall death rates.
        """
        diseases_of_interest = [
            "Septicemia",
            "Malignant Neoplasms",
            "Diabetes",
            "Alzheimer",
            "Influenza and Pneumonia",
            "Chronic Respiratory Diseases",
            "Other Respiratory Diseases",
            "Nephritis",
            "Abnormal Findings",
            "Heart Diseases",
            "Cerebrovascular Diseases",
            "COVID-19 (Multiple Cause)",
            "COVID-19 (Underlying Cause)",
        ]

        correlations = (
            self.data[diseases_of_interest + ["Total Deaths"]]
            .corr()["Total Deaths"]
            .drop("Total Deaths")
        )

        plt.figure(figsize=(12, 8))
        sns.barplot(x=correlations.index, y=correlations.values, color="skyblue")
        plt.title("Correlation Between Diseases and Overall Death Rates")
        plt.xlabel("Diseases")
        plt.ylabel("Correlation Coefficient")
        plt.xticks(rotation=45, ha="right")
        plt.show()

        print("Correlation Coefficients:")
        return correlations


# Example Usage:
# Assuming 'df' is your DataFrame
# analyzer = DiseaseInfluenceAnalyzer(df)
# correlations = analyzer.analyze_and_visualize()
