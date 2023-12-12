import pandas as pd


class DataMerge:
    def __init__(self, cdc_data, population_data):
        """
        Initialize the DataMerger.

        Parameters:
        - cdc_data (pd.DataFrame): The CDC data DataFrame.
        - population_data (pd.DataFrame): The Geo data DataFrame.
        """
        self.cdc_data = cdc_data
        self.population_data = population_data

    def merge_dataframes(self):
        """
        Merge CDC data and Geo data based on 'Jurisdiction', 'Quarter', 'GeoName', and 'Year'.

        Returns:
        - merged_data (pd.DataFrame): The merged DataFrame.
        """
        # Check for unique GeoName and Jurisdiction names
        unique_geo_names = self.population_data["GeoName"].unique()
        unique_jurisdiction_names = self.cdc_data["Jurisdiction"].unique()

        # Find differences between unique names
        difference1 = set(unique_jurisdiction_names) - set(unique_geo_names)
        difference2 = set(unique_geo_names) - set(unique_jurisdiction_names)

        print("Elements in array1 but not in array2:", difference1)
        print("Elements in array2 but not in array1:", difference2)

        # Ensure Quarter columns are of the same type
        self.cdc_data["Quarter"] = self.cdc_data["Quarter"].astype(str)
        self.population_data["Quaterly"] = (
            self.population_data["Quaterly"].astype(str).str.replace(":", "")
        )
        self.population_data.rename(columns={"Quaterly": "Quarter"}, inplace=True)

        # Perform the merge
        merged_data = pd.merge(
            self.cdc_data,
            self.population_data,
            left_on=["Jurisdiction", "Quarter"],
            right_on=["GeoName", "Quarter"],
            how="inner",
        )

        # Select relevant columns
        merged_data = merged_data[
            [
                "Jurisdiction",
                "Year",
                "Quarter",
                "GeoName",
                "Total_Population",
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

        return merged_data
