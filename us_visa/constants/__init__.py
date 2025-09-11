import os                                    #ceated while writing data ingestion code
from datetime import date                    #ceated while writing data ingestion code

DATABASE_NAME = "US_VISA"                    #ceated while writing data ingestion code

COLLECTION_NAME = "visa_data"                #ceated while writing data ingestion code

MONGODB_URL_KEY = "MONGODB_URL"              #ceated while writing data ingestion code          #created in enviromental variable

PIPELINE_NAME: str = "usvisa"                #ceated while writing data ingestion code
ARTIFACT_DIR: str = "artifact"               #ceated while writing data ingestion code
            
TRAIN_FILE_NAME: str = "train.csv"           #ceated while writing data ingestion code
TEST_FILE_NAME: str = "test.csv"             #ceated while writing data ingestion code

FILE_NAME: str = "usvisa.csv"                #ceated while writing data ingestion code
MODEL_FILE_NAME = "model.pkl"                #ceated while writing data ingestion code

TARGET_COLUMN = "case_status"                                      #created while writing data validation code
CURRENT_YEAR = date.today().year                                   #created while writing data validation code
PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"                #created while writing data validation code
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")           #created while writing data validation code    


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "visa_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2


"""
Data Validation realted contant start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"


"""
Data Transformation ralated constant start with DATA_TRANSFORMATION VAR NAME
"""
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"