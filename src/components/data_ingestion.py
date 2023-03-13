# Read the data
# Main aim to read the data from the databases and split the data into train and test split

import os # reason to import is CustomException 
import sys # reason to import is CustomException
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass #Use to created class variable

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformerConfig

from src.components.model_trainer import ModelTrainer
from src.components.model_trainer import ModelTrainerConfig


@dataclass
# To define a class we use __init__. But with dataclass we can directly define class variable
class DataIngestionConfig: #Input for data ingestion
    # Any required input for dataingestion
    train_data_path:str = os.path.join("artifacts","train.csv")
    test_data_path:str = os.path.join("artifacts","test.csv")
    raw_data_path:str = os.path.join("artifacts","data.csv")
    # These all we give as input and dataingetsionconfig will save the data in specific path

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() # All the three path will get saved to ingestion_config variable
    
    def initiate_data_ingestion(self): # To read from the database.  Create mongo client in utils and read it from here
        # For now, we are writing simple way to read data 
        logging.info("Enter the data ingestion method or component")
        try:
            df=pd.read_csv("notebook/data/stud.csv")
            logging.info("Read the dataset as a dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True) # Getting directory name
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True) # Save to raw data path

            logging.info("Train test split inititated")
            train_set, test_set = train_test_split(df, test_size = 0.2, random_state = 42) # SPliting train and test data
            
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True) # Save to train data path
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True) # Save to test data path

            logging.info("Ingestion of the data is completed")

            # Returning train and test path to use in data transformation
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)

if __name__=="__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr, test_arr,_ = data_transformation.initiate_data_transformation(train_data, test_data)

    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr, test_arr))