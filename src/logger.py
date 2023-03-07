# We will use this for logging
# ALl the information and execution should be logged to track the process
import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs",LOG_FILE) # Log file will be created in current working directory
os.makedirs(logs_path, exist_ok=True) # Keep appendig log file in the folder

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO, #wherever we write logging.info, all these info will get printed
)


# Testing  code of logger.py file 
# if __name__=="__main__":
#     logging.info("Logging has started")