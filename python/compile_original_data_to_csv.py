import os

from python.misc.download_original_data import download_original_data_if_needed

print('yay')

print(os.getcwd())

download_original_data_if_needed()

# if not os.path.exists(ORIGINAL_LOCAL_FILEPATH):
#     print('oh no')