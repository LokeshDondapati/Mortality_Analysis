import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class DeathRateAnalyze:
    def __init__(self, population_data):
        """
        Initialize the DeathRateAnalyzer.

        Parameters:
        - population_data (pd.DataFrame): DataFrame containing population data, including columns 'Total Deaths',
          'Total_Population', and 'Jurisdiction'.
        """
        self.population_data = population_data

    def analyze_and_visualize_death_rate(self):
        """
        Analyze and visualize the death rate across different states based on the provided population data.

        Output:
        - Display a scatter plot showing the relationship between death rate and total population for the top 10 states
          with the highest death rates. The size and color of the points represent different states.

        Note:
        - The function modifies the input DataFrame by adding a 'Death_Rate' column.
        - The 'Death_Rate' is calculated as the ratio of 'Total Deaths' to 'Total_Population'.
        - The function prints and returns the top 10 states with the highest average death rates.
        """
        # Calculate death rate
        self.population_data["Death_Rate"] = (
            self.population_data["Total Deaths"]
            / self.population_data["Total_Population"]
        )

        # Group by jurisdiction and calculate average death rate
        death_rate_by_state = (
            self.population_data.groupby("Jurisdiction")["Death_Rate"]
            .mean()
            .reset_index()
        )

        # Get the top 10 states with the highest death rates
        top_10_states = death_rate_by_state.nlargest(10, "Death_Rate")

        print("Top 10 States with Highest Death Rates:")
        print(top_10_states)

        sns.set(style="whitegrid")

        # Plot the scatter plot
        plt.figure(figsize=(12, 8))
        sns.scatterplot(
            x="Total_Population",
            y="Death_Rate",
            data=self.population_data.nlargest(10, "Death_Rate"),
            hue="Jurisdiction",
            palette="viridis",
            edgecolor="w",
            s=100,
        )

        plt.title("Scatter Plot of Death Rate vs. Total Population for Top 10 States")
        plt.xlabel("Total Population")
        plt.ylabel("Death Rate")

        plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")

        plt.show()

        return top_10_states
