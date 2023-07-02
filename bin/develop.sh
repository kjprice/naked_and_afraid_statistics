#!/bin/bash

cd "$(dirname "$0")"
cd ..

nodemon -e py -x 'python -m python.download_and_compile_original_data_to_csv'