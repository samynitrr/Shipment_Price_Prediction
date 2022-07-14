import yaml
import os
import sys
from datetime import datetime
import pandas as pd
import boto3
from shipment.exception import ShipmentException
from shipment.constant.constant import *

def read_yaml_file(yaml_file_path:str)->dict:
    """
    This function takes the yaml file path as an input,
    reads the yaml file safely and returns the content
    of the yaml file.
    --------------------------------------------------
    return: dict    
    """     
    try:
        with open(yaml_file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file) 
    except Exception as e:
        raise ShipmentException(e,sys) from e


def get_current_time_stamp():
    """
    This function return the current timestamp in the defined format
    ----------------------------------------------------------------
    return: %Y-%m-%d-%H-%M-%S
    """
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"


def get_log_dataframe(file_path):
    data=[]
    with open(file_path) as log_file:
        for line in log_file.readlines():
            data.append(line.split("^;"))

    log_df = pd.DataFrame(data)
    columns=["Time stamp","Log Level","line number","file name","function name","message"]
    log_df.columns=columns
    
    log_df["log_message"] = log_df['Time stamp'].astype(str) +":$"+ log_df["message"]

    return log_df[["log_message"]]

def generate_and_save_schema_file(data_file_path:str,
                                 target_column_name:str
                                 )->str:
        """
        Reads a data file and returns the schema as a dictionary.
        file_path: str
        """
        try:
            df = pd.read_csv(data_file_path)
            columns = df.columns
            data_types = list(map(lambda x:str(x).replace("dtype('","").replace("')",""), df.dtypes.values))
            columns_values = dict(zip(columns,data_types))
            num_columns = []
            cat_columns=[]
            domain_value = {}
            for column in columns_values:
                if columns_values[column] == 'object':
                    domain_value[column]= list(df[column].value_counts().index)
                    cat_columns.append(column)
                else:
                    num_columns.append(column)
            if target_column_name in columns_values:
                if target_column_name in num_columns:
                    num_columns.remove(target_column_name)
                else:
                    cat_columns.remove(target_column_name) 
            else:
                raise Exception(f"Target Column Name: [{target_column_name}] not in dataset."\
                     "Please ensure the spelling of the target column name is correct")
            
            schema = {
                "columns":
                    columns_values,
                
                "numerical_columns":
                    num_columns,

                "categorical_columns":
                    cat_columns,
                
                "target_column": 
                    target_column_name,

                "domain_value":
                    domain_value
                     }
            schema_dir = "schema"
            os.makedirs(schema_dir, exist_ok=True)
            schema_file_name = "schema.yaml"
            save_schema_file_path = os.path.join(
                ROOT_DIR,
                schema_dir,
                schema_file_name
                )
            with open(save_schema_file_path, "w") as schema_file:
                yaml.dump(schema, schema_file)
            return save_schema_file_path 
        except Exception as e:
            raise ShipmentException(e,sys) from e



def load_from_s3_bucket(aws_resource:str, bucket_name:str, file_name:str, file_path:str):
    try:
        connect = boto3.client(aws_resource, aws_access_key_id=AWS_ACCESS_KEY_ID,
                                           aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                                           region_name=REGION_NAME)
        connect.download_file(Bucket=bucket_name, Key=file_name, Filename=file_path)
    except Exception as e:
        raise ShipmentException(e,sys) from e

def save_to_s3_bucket(aws_resource:str, bucket_name:str, file_name:str, file_path:str):
    try:
        connect = boto3.client(aws_resource, aws_access_key_id=AWS_ACCESS_KEY_ID,
                                           aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                                           region_name=REGION_NAME)
        connect.upload_file(Bucket=bucket_name, Key=file_name, Filename=file_path)
    except Exception as e:
        raise ShipmentException(e,sys) from e

