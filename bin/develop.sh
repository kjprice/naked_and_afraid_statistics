#!/bin/bash

cd "$(dirname "$0")"
cd ..

nodemon -e py -x 'python -m python.compile_original_data_to_csv'