import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def explore_mortality_trends(data, diseases):
    """
    Explore and visualize mortality rate trends for specific diseases across states over time.

    Parameters:
    - data (pd.DataFrame): DataFrame containing mortality data, including columns for each specified disease,
      'Total_Population', 'Year', and 'Quarter'.
    - diseases (list): List of strings representing the diseases to analyze.

    Output:
    - Display a line plot showing the trends in mortality rates for each specified disease over the years,
      aggregated by quarters.

    Note:
    - The function modifies the input DataFrame by adding new columns for each disease's mortality rate.
    - Mortality rates are calculated as the ratio of the specific disease count to the total population.
    - The function groups the data by 'Year' and 'Quarter' and calculates the mean for each quarter.
    - The line plot depicts the mortality rate trends for each disease across the specified time period.
    """
    for disease in diseases:
        data[f'{disease}_Mortality_Rate'] = data[disease] / data['Total_Population']

    quarterly_data = data.groupby(['Year', 'Quarter']).mean().reset_index()

    plt.figure(figsize=(15, 8))
    for disease in diseases:
        sns.lineplot(x='Year', y=f'{disease}_Mortality_Rate', data=quarterly_data, label=disease, marker='o')

    plt.title('Mortality Rate Trends for Specific Diseases Across States (Q1 2020 to Q4 2023)')
    plt.xlabel('Year')
    plt.ylabel('Mortality Rate')

    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.show()