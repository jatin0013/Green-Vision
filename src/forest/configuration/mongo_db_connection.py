import sys
from src.forest.exception import ForestException
import os
from src.forest.constants.database import DATABASE_NAME
import pymongo
import certifi      # networking concepts 
from dotenv import load_dotenv  #to load dotenv files

load_dotenv()

ca =certifi.where()
class MongoDBClient:
    client = None
    def __init__(self,database_name = DATABASE_NAME)->None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url="mongodb+srv://demo:1234@cluster0.vvpyvhw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
                if mongo_db_url is None:
                    raise Exception(f"Environment key is not set")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url,tlsCAFile=ca)
                self.client = MongoDBClient.client
                self.database = self.client[DATABASE_NAME]
                self.database_name = database_name
        except Exception as e:
            raise ForestException(e,sys)