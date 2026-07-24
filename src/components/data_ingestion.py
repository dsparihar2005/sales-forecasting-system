from src.utils.exception import CustomException
from src.utils.logger import logging
from pymongo.mongo_client import MongoClient
from dataclasses import dataclass
from dotenv import load_dotenv
import pandas as pd
import os


@dataclass
class DataIngestionConfig:
    artifacts_dir:str = os.path.join(os.getcwd(), "artifacts")
    raw_data:str = os.path.join("artifacts", "raw_data.csv")
    oil:str = os.path.join("artifacts", "oil.csv")
    stores:str = os.path.join("artifacts", "stores.csv")
    holidays:str = os.path.join("artifacts", "holidays.csv")
    env_file_path:str = os.path.join("secrets.env")

class DataIngestion:
    def __init__(self):
        self.dataingestionconfig = DataIngestionConfig()
        logging.info(">>> DATA INGESTION STARTED <<<")

    def load_dataset(self):
        """
        Load dataset from local CSV files instead of MongoDB
        """
        logging.info("Loading dataset from local CSV files")

        try:

            train = pd.read_csv("data/train.csv")
            oil = pd.read_csv("data/oil.csv")
            stores = pd.read_csv("data/stores.csv")
            holidays = pd.read_csv("data/holidays_events.csv")

            os.makedirs(self.dataingestionconfig.artifacts_dir, exist_ok=True)

            train.to_csv(self.dataingestionconfig.raw_data, index=False)
            oil.to_csv(self.dataingestionconfig.oil, index=False)
            stores.to_csv(self.dataingestionconfig.stores, index=False)
            holidays.to_csv(self.dataingestionconfig.holidays, index=False)

            logging.info("Local CSV files copied successfully.")
            logging.info(">>> DATA INGESTION COMPLETE <<<")

        except Exception as e:
            logging.error(CustomException(e))
            raise CustomException(e)