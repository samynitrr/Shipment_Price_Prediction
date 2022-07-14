from distutils.command.config import config
from shipment.constant.constant import *
from shipment.entity.config_entity import *
from shipment.util.util import get_current_time_stamp, read_yaml_file
from shipment.logger import logging
from shipment.exception import ShipmentException
import sys

class GetConfiguration:
    def __init__(self, config_file_path:str = CONFIG_FILE_PATH, current_time_stamp:str = get_current_time_stamp()):
        try:
            self.config_info = read_yaml_file(yaml_file_path=config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.current_time_stamp = current_time_stamp
            
        except Exception as e:
            raise ShipmentException(e,sys) from e
    
    def get_training_pipeline_config(self)->TrainingPipelineConfig:
        try:

            training_pipeline_info =  self.config_info[TRAINING_PIPELINE_KEY]
            artifact_dir =  os.path.join(
                ROOT_DIR,
                training_pipeline_info[TRAINING_PIPELINE_NAME_KEY],
                training_pipeline_info[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            )

            training_pipeline_config = TrainingPipelineConfig(
                artifact_dir= artifact_dir
            )
            logging.info(f"Training Pipeline Configuration: {training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise ShipmentException(e,sys) from e
        
    def get_data_ingestion_config(self)->DataIngestionConfig:
        try:  

            artifact_dir = self.training_pipeline_config.artifact_dir

            data_ingestion_info =  self.config_info[DATA_INGESTION_KEY]
            
            data_artifact_dir =  os.path.join(
                artifact_dir,
                self.current_time_stamp,
                DATA_INGESTION_ARTIFACT_DIR
                )
            
            aws = data_ingestion_info[DATA_INGESTION_AWS_KEY]

            aws_resource = aws[DATA_INGESTION_AWS_RESOURCE_KEY]

            s3_bucket_name = aws[DATA_INGESTION_S3_BUCKET_NAME]

            aws_file_name =  aws[DATA_INGESTION_AWS_FILE_NAME_KEY]                       

            raw_data_dir = os.path.join(
                data_artifact_dir,
                data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY]
                )
            ingested_data_dir = os.path.join(
                data_artifact_dir,
                data_ingestion_info[DATA_INGESTION_INGESTED_DATA_DIR_KEY]
                )
            ingested_train_data_dir = os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_INGESTED_TRAIN_DIR_KEY]
                )
            ingested_test_data_dir = os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_INGESTED_TEST_DIR_KEY]
                )

            data_ingestion_config = DataIngestionConfig(
                aws_resource = aws_resource,
                aws_file_name= aws_file_name,
                s3_bucket_name=s3_bucket_name,
                raw_data_dir= raw_data_dir,
                ingested_data_dir=ingested_data_dir,
                ingested_train_data_dir= ingested_train_data_dir,
                ingested_test_data_dir= ingested_test_data_dir
                
            )
            logging.info(f"Data Ingestion Configuration: {data_ingestion_config}")
            return data_ingestion_config
        except Exception as e:
            raise ShipmentException(e,sys) from e

    

    
