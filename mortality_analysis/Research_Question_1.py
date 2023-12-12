import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def investigate_death_rate(population_data):
    """
    Analyze and visualize the death rate across different states based on the provided population data.

    Parameters:
    - population_data (pd.DataFrame): DataFrame containing population data, including columns 'Total Deaths',
      'Total_Population', and 'Jurisdiction'.

    Output:
    - Display a scatter plot showing the relationship between death rate and total population for the top 10 states
      with the highest death rates. The size and color of the points represent different states.

    Note:
    - The function modifies the input DataFrame by adding a 'Death_Rate' column.
    - The 'Death_Rate' is calculated as the ratio of 'Total Deaths' to 'Total_Population'.
    - The function prints and returns the top 10 states with the highest average death rates.
    """
    population_data['Death_Rate'] = population_data['Total Deaths'] / population_data['Total_Population']

    death_rate_by_state = population_data.groupby('Jurisdiction')['Death_Rate'].mean().reset_index()

    top_10_states = death_rate_by_state.nlargest(10, 'Death_Rate')

    print(top_10_states)

    sns.set(style="whitegrid")

    population_data['Death_Rate'] = population_data['Total Deaths'] / population_data['Total_Population']

    top_10_states = population_data.nlargest(10, 'Death_Rate')

    plt.figure(figsize=(12, 8))
    sns.scatterplot(x='Total_Population', y='Death_Rate', data=top_10_states, hue='Jurisdiction', palette='viridis', edgecolor='w', s=100)

    plt.title('Scatter Plot of Death Rate vs. Total Population for Top 10 States')
    plt.xlabel('Total Population')
    plt.ylabel('Death Rate')

    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.show()

