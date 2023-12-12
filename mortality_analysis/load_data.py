import os
import requests
import pandas as pd

class Loaddata:
    def __init__(self, url):
        self.url = url
        self.file_name = 'Mortalities_by_different_causes.csv'

    def download_cdc_data(self):
        """
        Download CDC data from the given URL and save it to a CSV file.

        Returns:
        - file_path (str): Path to the downloaded file.
        """
        # Check if the file already exists
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
            print(f"Deleted existing file: {self.file_name}")

        # Download the data from the URL
        response = requests.get(self.url)

        if response.status_code == 200:
            with open(self.file_name, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded CDC data to: {self.file_name}")
            return self.file_name
        else:
            print(f"Failed to download CDC data. Status code: {response.status_code}")
            return None

    def load_cdc_data(self):
        """
        Load CDC data from the CSV file into a DataFrame.

        Returns:
        - cdc_dataset (pd.DataFrame): DataFrame with the downloaded CDC data.
        """
        filename=self.download_cdc_data()
        if os.path.exists(filename):
            cdc_dataset = pd.read_csv(filename)
            print(f"Loaded CDC data from: {filename}")
        else:
            print("CDC data file does not exist.")
            return "Error"
        data = pd.read_csv(self.file_name)
        return data

    def load_population_data(self):
        second_url = "https://raw.githubusercontent.com/LokeshDondapati/Mortality_Analysis/main/Datasets/BEA%20Population%20Data.csv"
        data = pd.read_csv(second_url)
        return data


# Specify the URL and file name
cdc_url = 'https://data.cdc.gov/api/views/muzy-jte6/rows.csv?accessType=DOWNLOAD'
file_name = 'cdc_data.csv'

# Create an instance of the CDCDataDownloader class
cdc_downloader = Loaddata(cdc_url)

# Download CDC data and read it into a DataFrame
cdc_dataset = cdc_downloader.load_cdc_data()
