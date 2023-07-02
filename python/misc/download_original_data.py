import os
import requests

from python.config import ORIGINAL_REMOTE_URL, ORIGINAL_LOCAL_FILEPATH

def save_excel_file(data):
    print(f'Saving File to "{ORIGINAL_LOCAL_FILEPATH}"')
    with open(ORIGINAL_LOCAL_FILEPATH, 'wb') as f:
        f.write(data)

def pull_excel_file():
    response = requests.get(ORIGINAL_REMOTE_URL, allow_redirects=True)
    if not response.ok:
        raise Exception(f'Could not download file "{ORIGINAL_REMOTE_URL}" with response {response.text}')

    return response.content

def download_original_data_if_needed():
    if os.path.exists(ORIGINAL_LOCAL_FILEPATH):
        return
    print('Downloading Data')
    data = pull_excel_file()
    save_excel_file(data)
    # print('ORIGINAL_LOCAL_FILEPATH', ORIGINAL_LOCAL_FILEPATH)
    # print('NO')
    pass