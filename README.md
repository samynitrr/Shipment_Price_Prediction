# Shipment_Price_Prediction

# Problem Statement:
The market for supply chain analytics is expected to develop at a CAGR of 17.3 percent
from 2019 to 2024, more than doubling in size. This data demonstrates how supply
chain organizations are understanding the advantages of being able to predict what will
happen in the future with a decent degree of certainty. Supply chain leaders may use
this data to address supply chain difficulties, cut costs, and enhance service levels all at
the same time.

```
The main goal is to predict the supply chain shipment pricing based on the available
factors in the dataset.
```

# Approach: 
This is a case of Supervised Machine Learning Regression Algorithm. The classical machine learning tasks 
like Data Exploration, Data Cleaning, Feature Engineering, Model Building and Model Testing will be 
performed as a part of this project. This project is an end-to-end solution driven approach from acquiring
the data to API creation and deployment to cloud with a frontend for ease of end-user.

# Project Structure
```
|-- Project
    |-- config
        |-- config.yaml
        |-- schema.yaml
        |-- model.yaml
    |-- shipment (Project folder)
        |-- __init__.py
        |--constant (All the hardcoded values)
            |--__init__.py
        |-- component (pipeline stages)
            |-- __init__.py
            |-- data_ingestion.py
            |-- data_validation.py
            |-- data_transformation.py
            |-- model_train.py
            |-- model_evaluation.py
            |-- model_push.py
        |-- get_config
            |-- __init__.py
            |-- configuration.py
        |-- entity
            |-- __init__.py
            |-- config_entity.py
            |-- artifact_entity.py
        |-- exception
            |-- __init__.py
        |-- logger
            |-- __init__.py
        |-- pipeline
            |-- __init__.py
            |-- pipeline.py
        |-- util (Helper function)
            |--__init__.py
            |-- util.py
    |-- .gitignore
    |-- app.py (Entry Point to the Project)
    |-- requirements.txt
    |-- LICENSE
    |-- README.md
```