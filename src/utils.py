# Common functionality code
# Read a data from database
# Save a model into cloud 
# Whenever requirement is there we write function here

import os
import sys

import numpy as np
import pandas as pd
import dill

from src.logger import logging
from src.exception import CustomException

def save_object(file_path, obj):    
    try:
        dir_path = os.path.dirname(file_path)
        # Create directory
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path,"wb") as file_obj:
            # Library which will help to create pickle file
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)