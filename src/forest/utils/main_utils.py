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
def write_yaml_file (file_path:str , content:object ,replace:bool = False)->None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path),exist_ok = True)
        with open (file_path, "w") as file:
            yaml.dump(content , file)
    except Exception as e:
        raise ForestException(e,sys)

def load_object(file_path:str)->object :
    logging.info("Enterd the load_object method of main utils")
    try :
        with open(file_path,"rb") as file :
            obj = dill.load(file) # de serializze the object 

        logging.info("Exited the load object of main utils")
        return obj
    except Exception as e :
        raise ForestException(e,sys) from e 

def save_numpy_array_data(file_path:str,array :np.array):
    try :
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path ,exist_ok=True)
        with open(file_path,'wb') as file:
            np.save(file,array)
    except Exception as e:
        raise ForestException(e,sys) from e 
    
def load_numpy_array_data(file_path:str)->np.array:
    try :
        with open(file_path,'rb') as file:
            return np.load(file)
    except Exception as e:
        raise ForestException(e,sys) from e 
    
def save_object(file_path , obj:object):
    logging.info("Entered the save object method of main utils")
    try :
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open (file_path,"wb") as file :
            dill.dump(obj,file)
        logging.info("Exited the save object function ")
    except Exception as e:
        raise ForestException(e,sys) from e 
def create_dir(path_to_dir:list , verbose:True):
    for path in path_to_dir:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logging.info(f"created direcotr at {path}")