import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from logger import logging
import pandas as pd
from src.exception import CustomException  # Custom exception class for handling errors
from src.logger import logging  # Logger for recording process information
import pandas as pd  # Library for data manipulation and analysis
from sklearn.model_selection import train_test_split  # Utility to split data into training and testing sets
from dataclasses import dataclass  # Dataclass to create configuration objects easily

@dataclass
class DataIngestionConfig:
    """
    Configuration class for data ingestion paths.
    Defines default paths for raw, training, and testing data.
    """
    train_data_path: str = os.path.join('artifacts', "train.csv")  # Path to save the training data
    test_data_path: str = os.path.join('artifacts', 'test.csv')   # Path to save the testing data
    raw_data_path: str = os.path.join('artifacts', 'data.csv')    # Path to save the raw data

class DataIngestion:
    """
    Class to handle the data ingestion process:
    1. Reading raw data from a source file.
    2. Splitting the data into training and testing sets.
    3. Saving the split data to predefined paths.
    """
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()  # Initialize with default configuration

    def initiate_data_ingestion(self):
        """
        Perform the data ingestion process:
        - Read raw data from a CSV file.
        - Save the raw data.
        - Split the data into training and testing sets.
        - Save the split datasets.
        """
        logging.info("Enter the data ingestion method or component")  # Log entry to the method
        try:
            # Step 1: Read the dataset
            df = pd.read_csv('notebook/data/stud.csv')  # Read raw data into a DataFrame
            logging.info('Read the dataset as a DataFrame')

            # Step 2: Ensure the output directory exists
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Step 3: Save the raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # Step 4: Perform train-test split
            logging.info('Train-test split initiated')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Step 5: Save the training and testing datasets
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Ingestion of data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            # Log any exceptions that occur and raise a custom exception
            logging.error(f"Error during data ingestion: {e}")
            raise CustomException(e, sys)
        
        if __name__ == "main":
            obj = DataIngestion()
            obj.initiate_data_ingestion()

