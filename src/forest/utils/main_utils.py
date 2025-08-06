import utils
import os.path
import numpy as np
import dill
import yaml
import sys
from src.forest.exception import ForestException
from src.forest.logging import logging

#reading yaml file 
def read_yaml_file(file_path :str) ->dict :
    try:
        with open (file_path ,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise ForestException(e,sys) from e
