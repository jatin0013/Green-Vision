from src.forest.configuration.mongo_db_connection import MongoDBClient
import sys
from src.forest.constants.database import DATABASE_NAME,COLLECTION_NAME
from src.forest.exception import ForestException
from src.forest.logging import logging 
import pandas as pd
from typing import Optional
import numpy as np 

class ForestData:
    def __init__(self):
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise ForestException(e,sys)
    def export_collection_as_df(self,collection_name:str,database_name:Optional[str]=None)->pd.DataFrame:
        try:
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"],axis=1)
            df.replace({"na":np.nan},inplace=True)
            return df
        except Exception as e:
            raise ForestException(e,sys)