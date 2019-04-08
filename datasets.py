"""
You can import this file as:
from datasets import *
to get the datsets in pandas dataframe.

Functions:
	- get_SATScores()
	- get_Demographic()

"""



#######################################
#######################################
# These can be helpful if our dataset is not CSV 
# I didn't know you can get csv format from nyc open data
# So i wrote the download script manually without using pandas


# import requests
# import os


# # PATH
# PATH = '/Users/shravan/Desktop/NYCHS-Data-Analysis/datasets'

# # Create a folder to save dataset
# directory = os.path.dirname("datasets")
# if not os.path.exists(directory):
#     os.makedirs(PATH)

# response = requests.get(SAT_LINK)
# with open(PATH+'/satScores.xlsx','wb') as handle:
# 	handle.write(response.content)

#######################################
#######################################

import pandas as pd


## Download and save if does not exist
## Return panda data frame

# SAT Score of 2012 form nyc open data
SAT_LINK = "https://data.cityofnewyork.us/resource/f9bf-2cp4.csv"
def get_SATScores():
	return pd.read_csv(SAT_LINK)

# Demographic Data by Zip Code
DEMOGRAPHIC_LINK = "https://data.cityofnewyork.us/resource/kku6-nxdu.csv"
def get_Demographic():
	return pd.read_csv(DEMOGRAPHIC_LINK)










