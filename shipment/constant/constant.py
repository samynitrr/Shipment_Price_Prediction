import os
from dotenv import load_dotenv


#------------------- CONFIG YAML FILE related variables ---------------------#
ROOT_DIR = os.getcwd()

CONFIG_DIR = 'config'

CONFIG_FILE_NAME = 'config.yaml'
MODEL_FILE_NAME = 'model.yaml'
PROJECT_FILE_NAME = 'project.yaml'
SCHEMA_FILE_NAME = 'schema.yaml'

CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)
MODEL_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,MODEL_FILE_NAME)
PROJECT_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,PROJECT_FILE_NAME)
SCHEMA_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,SCHEMA_FILE_NAME)

#---------------------- TRAINING PIPELINE related variable -------------------#

TRAINING_PIPELINE_KEY = 'training_pipeline'
TRAINING_PIPELINE_NAME_KEY = 'pipeline'
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = 'artifact_dir'

#---------------------- DATA INGESTION related variable -------------------#

DATA_INGESTION_KEY = "data_ingestion"
DATA_INGESTION_DATASET_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INGESTION_TGZ_DATA_DIR_KEY = "tgz_data_dir"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_INGESTED_DATA_DIR_KEY = "ingested_data_dir"
DATA_INGESTION_INGESTED_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION_INGESTED_TEST_DIR_KEY = "ingested_test_dir"
DATA_INGESTION_AWS_KEY = "aws"
DATA_INGESTION_AWS_RESOURCE_KEY = "aws_resource"
DATA_INGESTION_S3_BUCKET_NAME = "s3_bucket_name"
DATA_INGESTION_AWS_FILE_NAME_KEY = "aws_file_name"
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
RAW_FILE_NAME = "shipment_prediction_data.csv"
#----------------------------- SECRETS ---------------------------------------#
load_dotenv()
AWS_ACCESS_KEY_ID=os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.getenv("AWS_SECRET_ACCESS_KEY")
REGION_NAME=os.getenv("REGION_NAME")