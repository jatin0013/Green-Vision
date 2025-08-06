import logging
import os
from from_root import from_root
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

LOG_FILE = f"{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log"
logs_path = os.path.join(from_root(),"logs",LOG_FILE)

os.mkdir(logs_path ,exits_ok = True)
LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s] %(name)s - %(level)s - %(message)s"
    level = logging.DEBUG,

)

# S string formatting it is a placeholder that python logging module fills automatically
