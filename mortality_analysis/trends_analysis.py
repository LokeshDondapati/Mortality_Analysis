import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class MortalityTrends:
    def __init__(self, data):
        """
        Initialize the MortalityTrendsExplorer object with mortality data.

        Parameters:
        - data (pd.DataFrame): DataFrame containing mortality data, including columns for each specified disease,
          'Total_Population', 'Year', and 'Quarter'.
        """
        self.data = data

    def explore_mortality_trends(self, diseases):
        """
        Explore and visualize mortality rate trends for specific diseases across states over time.

        Parameters:
        - diseases (list): List of strings representing the diseases to analyze.

        Output:
        - Display a line plot showing the trends in mortality rates for each specified disease over the years,
          aggregated by quarters.

        Notes:
        - The function modifies the input DataFrame by adding new columns for each disease's mortality rate.
        - Mortality rates are calculated as the ratio of the specific disease count to the total population.
        - The function groups the data by 'Year' and 'Quarter' and calculates the mean for each quarter.
        - The line plot depicts the mortality rate trends for each disease across the specified time period.
        """
        # Calculate and add mortality rate columns for each specified disease
        for disease in diseases:
            self.data[f"{disease}_Mortality_Rate"] = (
                self.data[disease] / self.data["Total_Population"]
            )

        # Group data by 'Year' and 'Quarter' and calculate mean for each quarter
        quarterly_data = self.data.groupby(["Year", "Quarter"]).mean().reset_index()

        # Plot mortality rate trends for each disease
        plt.figure(figsize=(15, 8))
        for disease in diseases:
            sns.lineplot(
                x="Year",
                y=f"{disease}_Mortality_Rate",
                data=quarterly_data,
                label=disease,
                marker="o",
            )

        # Set plot title and labels
        plt.title(
            "Mortality Rate Trends for Specific Diseases Across States (Q1 2020 to Q4 2023)"
        )
        plt.xlabel("Year")
        plt.ylabel("Mortality Rate")

        # Display legend outside the plot for better visibility
        plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")

        # Show the plot
        plt.show()


# Example Usage:
# Assuming 'df' is your DataFrame
# explorer = MortalityTrendsExplorer(df)
# explorer.explore_mortality_trends(['Disease1', 'Disease2'])
