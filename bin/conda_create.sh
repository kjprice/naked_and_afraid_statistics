#!/bin/bash

set -e

cd "$(dirname "$0")"
cd ..

# CONDA_ENV_NAME=naked_and_afraid
# conda create -y --name $CONDA_ENV_NAME jupyterlab matplotlib numpy pandas requests


CONDA_ENV_DIR=conda_env

conda create -y --prefix env jupyterlab matplotlib numpy pandas requests openpyxl ipykernel seaborn
./env/bin/python -m ipykernel install --prefix=env --name='naked_and_afraid'
# python -m ipykernel install --prefix=env
