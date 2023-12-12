# Importing necessary libraries for data analysis and visualization
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Setting display options for better dataframe visualization
pd.set_option("display.max_rows", 100)

# Importing custom module for data loading
from mortality_analysis import load_data

# Loading CDC data using custom Loaddata class
cdc_data = load_data.Loaddata(
    url="https://data.cdc.gov/api/views/muzy-jte6/rows.csv?accessType=DOWNLOAD"
)
cdc_data.load_cdc_data()

# Accessing the loaded CDC data
cdc_dataset = cdc_data.load_cdc_data()

# Displaying the first few rows of the dataset for inspection
cdc_dataset.head()

# Displaying dataset info to understand data types and missing values
cdc_dataset.info()

# Checking for missing values in each column
cdc_dataset.isna().sum()

# Converting 'Week Ending Date' column to datetime format for easier manipulation
cdc_dataset["Week Ending Date"] = pd.to_datetime(
    cdc_dataset["Week Ending Date"], format="%Y-%m-%d"
)

# Creating a 'Quarter' column based on the 'Week Ending Date'
cdc_dataset["Quarter"] = cdc_dataset["Week Ending Date"].dt.to_period("Q")

# Removing duplicate entries based on specific columns
cdc_dataset = cdc_dataset.drop_duplicates(
    subset=["Jurisdiction of Occurrence", "Quarter"]
)

# Importing custom data cleaning module
from mortality_analysis import data_cleaning

# Initializing the data cleaning processor
cdc_processor = data_cleaning.CDCDataProcessor(data=cdc_dataset)

# Preprocessing the CDC dataset
cdc_dataset = cdc_processor.preprocess_data()

# Displaying dataset information after preprocessing
cdc_dataset.info()

# Selecting relevant columns for further analysis
cdc_dataset = cdc_dataset[
    [
        "Jurisdiction",
        "Year",
        "Quarter",
        "Total Deaths",
        "Natural Deaths",
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
]

# Importing module for loading additional data
from mortality_analysis import load_data

# Loading BEA data using the Loaddata class
bea_data = load_data.Loaddata(
    url="https://data.cdc.gov/api/views/muzy-jte6/rows.csv?accessType=DOWNLOAD"
)
bea_data.load_population_data()

# Accessing the loaded BEA data
bea_dataset = bea_data.load_population_data()

# Displaying the first few rows of the BEA dataset
bea_dataset.head()

# Dropping unnecessary columns from the BEA dataset
bea_dataset.drop(columns="GeoFips", inplace=True)

# Melting the dataframe for easier analysis
transposed = bea_dataset.melt(
    id_vars="GeoName", var_name="Quarterly", value_name="Total_Population"
)

# Sorting the transposed data for better organization
sorted_transposed = transposed.sort_values(by="GeoName")

# Importing module for merging datasets
from mortality_analysis import merge_data

# Initializing the DataMerge class for merging CDC and population data
merge = merge_data.DataMerge(cdc_data=cdc_dataset, population_data=bea_dataset)

# Merging datasets and accessing the merged data
merged_data = merge.merge_datasets()

# Importing module for data analysis
from mortality_analysis import data_analysis

# Initializing DataAnalysis class for performing various analyses
analysis = data_analysis.DataAnalysis(merged_data)

# Displaying counts of categorical variables
analysis.display_categorical_counts()

# Displaying boxplot to identify outliers
analysis.display_boxplot_outliers()

# Displaying distribution of numerical variables
analysis.display_numerical_distribution()

# Displaying correlation matrix of variables
analysis.display_correlation_matrix()

# Importing module for data preparation
from mortality_analysis.data_preparation import DataPreparation

# Setting the target column for prediction
target_column = "Total Deaths"

# Initializing DataPreparation class for data preparation
data = DataPreparation(merged_data, target_column)

# Preparing the data and storing it
prepped_data = data.prepare_data()

# Displaying the prepared data
print("Prepared Data:")
prepped_data

# Visualizing pairplot of the first four columns of prepared data
sns.pairplot(prepped_data.iloc[:, :4])
plt.show()

# Calculating and visualizing the correlation matrix
correlation_matrix = prepped_data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.show()

# Importing module for death rate analysis
from mortality_analysis import investigate_death_rate_analysis

# Initializing DeathRateAnalyze class for analysis
deathrate = investigate_death_rate_analysis.DeathRateAnalyze(df)

# Analyzing and visualizing death rates
deathrate.analyze_and_visualize_death_rate()

# Importing module for trends analysis
from mortality_analysis import trends_analysis

# Initializing MortalityTrends class for analyzing mortality trends
trends = trends_analysis.MortalityTrends(merged_data)

# Setting the list of diseases of interest for trend analysis
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

# Exploring mortality trends for the specified diseases
trends.explore_mortality_trends(diseases_of_interest)

# Importing module for analyzing diseases with significant influence
from mortality_analysis import diseases_with_significant_influence_analysis

# Initializing DiseaseInfluence class for analysis
analysis = diseases_with_significant_influence_analysis.DiseaseInfluence(merged_data)

# Analyzing and visualizing the influence of diseases
analysis.analyze_and_visualize()

# Importing modules for predictive modeling and evaluation
from mortality_analysis import predictive_model
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Initializing DecisionTreeModel class for predictive modeling
dt_model = predictive_model.DecisionTreeModel(merged_data)

# Loading and preparing data for the model
dt_model.load_and_prepare_data()

# Splitting data into training and testing sets
dt_model.split_data()

# Building and evaluating the decision tree model
dt_model.build_and_evaluate_decision_tree()

# Printing evaluation metrics of the model
dt_model.print_evaluation_metrics()

# Visualizing the decision tree model
dt_model.visualize_decision_tree()
