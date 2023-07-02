import os

from python.config import ORIGINAL_REMOTE_URL, ORIGINAL_LOCAL_FILEPATH

def download_original_data_if_needed():
    if not os.path.exists(ORIGINAL_LOCAL_FILEPATH):
        print('NO')
    pass