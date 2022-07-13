import os

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
DATA_INGESTION_ZIP_DATA_DIR_KEY = "zip_data_dir"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_INGESTED_DATA_DIR_KEY = "ingested_data_dir"
DATA_INGESTION_INGESTED_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION_INGESTED_TEST_DIR_KEY = "ingested_test_dir"
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
