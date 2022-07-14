from shipment.entity.config_entity import DataIngestionConfig
from shipment.entity.artifact_entity import DataIngestionArtifact
from shipment.logger import logging
from shipment.exception import ShipmentException
from shipment.util.util import load_from_s3_bucket
from shipment.constant.constant import RAW_FILE_NAME
import os
import sys
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit
import numpy as np
class DataIngestion:
    def __init__(self, data_ingestion_config:DataIngestionConfig ) -> None:
        try:
            logging.info(f"{'-'*20} Data Ingestion log started. {'-'*20}")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise ShipmentException(e,sys) from e
        pass

    def download_data(self):
        try:
            is_ingested = False                     
            raw_data_dir = self.data_ingestion_config.raw_data_dir
            
            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)

            os.makedirs(raw_data_dir, exist_ok=True)

            aws_resource = self.data_ingestion_config.aws_resource
            bucket_name = self.data_ingestion_config.s3_bucket_name
            aws_file_name = self.data_ingestion_config.aws_file_name
            raw_file_name = RAW_FILE_NAME
            raw_file_path = os.path.join(raw_data_dir, raw_file_name)  

            logging.info(f"Downloading file from :[{aws_resource}/{bucket_name}] into : [{raw_file_path}]")        
                      
            load_from_s3_bucket(aws_resource, bucket_name, aws_file_name, raw_file_path)            

            logging.info(f"File: [{aws_file_name}] has been downloaded successfully and is available at [{raw_file_path}]")
            is_ingested = True
            return raw_file_path, is_ingested
        except Exception as e:
            raise ShipmentException(e,sys) from e


    def split_train_test(self):

        try:            
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            raw_file_name = os.listdir(raw_data_dir)[0]

            raw_file_path = os.path.join(raw_data_dir,raw_file_name)

            logging.info(f"Reading csv file: {raw_file_path}")

            ingested_train_dir = self.data_ingestion_config.ingested_train_data_dir
            train_file_path = os.path.join(ingested_train_dir, raw_file_name)
            
            ingested_test_dir = self.data_ingestion_config.ingested_test_data_dir 
            test_file_path = os.path.join(ingested_test_dir, raw_file_name)

            df = pd.read_csv(raw_file_path)

            # We are creating a derived column which has values as 5 bins. This is
            # created because the target column (or the column to be used for split)
            # has several values which have only 1 count and it creates issue for shuffle split.
            df['derived_target'] = pd.cut(
                df['Freight Cost (USD)'],
                bins = [0.0,57930.5,115861.0,173791.5,231722.0,np.inf],
                labels = [1,2,3,4,5]
                
            )

            train_df = None
            test_df = None        

            logging.info(f"Splitting the raw data into train and test data")

            split = StratifiedShuffleSplit(n_splits=2, test_size=0.2, random_state=42)
            for train_index,test_index in  split.split(df,df['derived_target']):
                train_df = df.loc[train_index].drop(["derived_target"],axis=1)
                test_df = df.loc[test_index].drop(["derived_target"],axis=1)                     

            if train_df is not None:
                os.makedirs(train_file_path, exist_ok=True)
                logging.info(f"Exporting train file to : {train_file_path}")
                train_df.to_csv(train_file_path, index=False)

            if test_df is not None:
                os.makedirs(test_file_path, exist_ok=True)
                logging.info(f"Exporting test file to : {test_file_path}")
                test_df.to_csv(test_file_path, index=False)

            message = f"The raw data has been successfully split into train and test data"
            return train_file_path, test_file_path, message
        except Exception as e:
            raise ShipmentException(e, sys) from e      

        

    def initiate_data_ingestion(self)->DataIngestionArtifact:
        try:
            is_ingested = self.download_data()
            train_file_path, test_file_path, message = self.split_train_test() 
            data_ingestion_artifact = DataIngestionArtifact(
                train_file_path= train_file_path,
                test_file_path= test_file_path,
                is_ingested= is_ingested,
                ingestion_message=message
            )
            return data_ingestion_artifact
        except Exception as e:
            raise ShipmentException(e,sys) from e

    
