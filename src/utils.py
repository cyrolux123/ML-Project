import os
import sys
import dill
import numpy as np
import pandas as pd
import logging

from src.exception import CustomException

logging.basicConfig(level=logging.INFO)

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        logging.info(f"Directory created or already exists: {dir_path}")

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
            logging.info(f"Object saved successfully at: {file_path}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise CustomException(e, sys)