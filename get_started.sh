#!/usr/bin/env bash

# Creates the environment
virtualenv -p python3 env


# Activates the environment
source env/bin/activate

# pip install into environment
pip install git+https://github.com/BoseCorp/py-googletrans.git
pip install --editable .

