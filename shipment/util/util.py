import yaml
import os
import sys
from datetime import datetime
import pandas as pd
from shipment.exception import ShipmentException

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

