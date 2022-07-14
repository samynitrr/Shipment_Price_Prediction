from collections import namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig",["aws_resource","aws_file_name",
"s3_bucket_name","raw_data_dir","ingested_data_dir", "ingested_train_data_dir",
"ingested_test_data_dir"])

TrainingPipelineConfig = namedtuple("TrainingPipelineConfig",["artifact_dir"])