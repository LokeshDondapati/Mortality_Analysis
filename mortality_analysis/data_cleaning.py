import pandas as pd

class CDCDataProcessor:
    def __init__(self, data):
        """
        Initialize the CDCDataProcessor.

        Parameters:
        - data (pd.DataFrame): The input DataFrame containing CDC data.
        """
        self.data = data

    def preprocess_data(self):
        """
        Preprocess the CDC data by performing various transformations.

        Returns:
        - preprocessed_data (pd.DataFrame): The preprocessed DataFrame.
        """
        # Convert 'Week Ending Date' to datetime format and add 'Quarter' column
        self.data['Week Ending Date'] = pd.to_datetime(self.data['Week Ending Date'], format='%Y-%m-%d')
        self.data['Quarter'] = self.data['Week Ending Date'].dt.to_period("Q")

        # Drop duplicates based on 'Jurisdiction of Occurrence' and 'Quarter'
        self.data = self.data.drop_duplicates(subset=['Jurisdiction of Occurrence', 'Quarter'])

        # Drop specified columns
        columns_to_drop = [
            'flag_allcause', 'flag_natcause', 'flag_sept', 'flag_neopl', 'flag_diab',
            'flag_alz', 'flag_inflpn', 'flag_clrd', 'flag_otherresp', 'flag_nephr',
            'flag_otherunk', 'flag_hd', 'flag_stroke', 'flag_cov19mcod', 'flag_cov19ucod'
        ]
        self.data.drop(columns=columns_to_drop, inplace=True)

        # Rename columns
        new_column_names = {
            'Data As Of': 'Date',
            'Jurisdiction of Occurrence': 'Jurisdiction',
            'MMWR Year': 'Year',
            'MMWR Week': 'Week',
            'Week Ending Date': 'Ending Date',
            'All Cause': 'Total Deaths',
            'Natural Cause': 'Natural Deaths',
            'Septicemia (A40-A41)': 'Septicemia',
            'Malignant neoplasms (C00-C97)': 'Malignant Neoplasms',
            'Diabetes mellitus (E10-E14)': 'Diabetes',
            'Alzheimer disease (G30)': 'Alzheimer',
            'Influenza and pneumonia (J09-J18)': 'Influenza and Pneumonia',
            'Chronic lower respiratory diseases (J40-J47)': 'Chronic Respiratory Diseases',
            'Other diseases of respiratory system (J00-J06,J30-J39,J67,J70-J98)': 'Other Respiratory Diseases',
            'Nephritis, nephrotic syndrome and nephrosis (N00-N07,N17-N19,N25-N27)': 'Nephritis',
            'Symptoms, signs and abnormal clinical and laboratory findings, not elsewhere classified (R00-R99)': 'Abnormal Findings',
            'Diseases of heart (I00-I09,I11,I13,I20-I51)': 'Heart Diseases',
            'Cerebrovascular diseases (I60-I69)': 'Cerebrovascular Diseases',
            'COVID-19 (U071, Multiple Cause of Death)': 'COVID-19 (Multiple Cause)',
            'COVID-19 (U071, Underlying Cause of Death)': 'COVID-19 (Underlying Cause)'
        }
        self.data.rename(columns=new_column_names, inplace=True)

        # Convert 'Ending Date' column to datetime format
        self.data['Ending Date'] = pd.to_datetime(self.data['Ending Date'])

        # Extract year, month, and day into separate columns
        self.data['Year'] = self.data['Ending Date'].dt.year
        self.data['Month'] = self.data['Ending Date'].dt.month
        self.data['Day'] = self.data['Ending Date'].dt.day

        return self.data

