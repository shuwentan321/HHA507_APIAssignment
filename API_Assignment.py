# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 19:29:20 2021

@author: ikima
"""

#Importing packages
import requests


##We will be connecting to an API that provides the Latest Covid-19 Data 
##This COVID-19 data consists of information regarding to number of cases, recoveries, and death by regions

##GET Request to pull data from API
response = requests.get("https://coronavirus.m.pipedream.net/")

#Printing a status code to ensure the data is correctly accessed
response.status_code
print(response.status_code)

#Viewing the data in a JSON format
CovidData = response.json()
print(CovidData)

#Viewing the raw data column 
CovidRawData = CovidData['rawData']

