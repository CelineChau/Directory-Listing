import os 

"""
Python Directory tree`

Author : Celine CHAU
Start date : 16/02/20

STEP 1 - Retrieve all folders and files
STEP 2 - Build Tree function
STEP 3 - Display Tree function
STEP 4 - Code Main
"""

# STEP 1 - Retrieve all folders and files

cwd = os.getcwd() # get current dir
entries = os.listdir(cwd)
