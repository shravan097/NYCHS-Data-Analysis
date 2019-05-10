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
SAT_LINK_2012 = "https://data.cityofnewyork.us/resource/f9bf-2cp4.csv"
SAT_LINK_2010 = 'https://data.cityofnewyork.us/resource/rt5r-ie69.csv'
SAT_LINK_2015 = 'https://drive.google.com/uc?export=download&id=1v9R8nSZ5wnzFMt7i2AFk0qPw7tuPmXwZ'
def get_SATScores(year): 
	if year == '2010':
		return pd.read_csv(SAT_LINK_2010)
	if year == '2012':
		return pd.read_csv(SAT_LINK_2012)
	if year =='2015':
		return pd.read_csv(SAT_LINK_2015)

# Demographic Data by Zip Code
DEMOGRAPHIC_LINK = "https://data.cityofnewyork.us/resource/kku6-nxdu.csv"
def get_Demographic():
	return pd.read_csv(DEMOGRAPHIC_LINK)



def get_Graduation(filterBy):
	"""
		filterBy:
			-district
			-borough
			-school
			-demographic
	"""
	if filterBy=='district':
		return pd.read_csv('https://data.cityofnewyork.us/api/views/fq9e-fd84/rows.csv?accessType=DOWNLOAD')
	elif filterBy=='borough':
		return pd.read_csv('https://data.cityofnewyork.us/api/views/k2ic-km9j/rows.csv?accessType=DOWNLOAD')
	elif filterBy=='school':
		return pd.read_csv('https://data.cityofnewyork.us/api/views/35ey-ieq4/rows.csv?accessType=DOWNLOAD')
	elif filterBy=='demographic':
		return pd.read_csv('https://data.cityofnewyork.us/api/views/qk7d-gecv/rows.csv?accessType=DOWNLOAD')
	else:
		raise NameError("filterBy types invalid\nfilterby can be 'district','borough' or 'school'")


def get_SchoolsByDistrict(districtNumber):
	schools = get_SATScores()
	schools['dbn'] = list(map(lambda x: int(x[:2]),schools['dbn']))
	return list(schools[schools['dbn']==districtNumber]['school_name'])

def get_SchoolGrade():
	df = pd.read_csv('https://data.cityofnewyork.us/api/views/ffnc-f3aa/rows.csv?accessType=DOWNLOAD')
	return df[df['SCHOOL LEVEL*']=='High School'][['DBN','DISTRICT','SCHOOL','2009-2010 OVERALL GRADE']]



