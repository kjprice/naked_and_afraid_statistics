import os

from python.misc.download_original_data import download_original_data_if_needed
from python.misc.compile_original_to_csv import compile_to_csv



if __name__ == "__main__":
    download_original_data_if_needed()
    compile_to_csv()
