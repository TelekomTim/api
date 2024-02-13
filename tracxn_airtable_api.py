'''
TRACXN-AIRTABLE INTERFACE 1.0.0
This programm allows you to import company profiles into your Airtable base.

To run the programm properly you need to:
- 

Features:
1. 
2.
3.
4.

To be implemented:
1.
2.
3.
'''
#Airtables library for Python requests
from pyairtable import Api, utils
# HTTP-library to make the calls to the tracxn API
import requests 
#Recieves the API token, which should be stored in the system variables
import os
#Formats the response from tracxn 
import json
#Helps to format each company-URL into a format Traxcn takes to search for the company
from urllib.parse import urlparse


def getAirtableAPI():
    #TODO: Wie speichert man typischerweise Keys (lokal/webbasiert)
    airtable_key = os.environ.get("API_KEY_AIRTABLE")
    #TODO: Ist die Rückgabe wenn leer immer None? 
    if airtable_key != "none": 
        return Api(airtable_key)
    else:
        #TODO: (1) Als Error-log ausgeben und programm abbrechen?
        print("No Airtable API token found in OS. Please save the token under 'API_KEY_AIRTABLE'")
        return False

def getAirtableTable(fBaseKey, fTableKey):
    try:
        return airtable_api.table(fBaseKey, fTableKey)
    #TODO: Siehe (1)
    except():
        pass #Error log + Programmabbruch. Entweder viele IF empty abfragen oder Programmabbruch -> ChatGPT

def getTraxcnToken():
    tracxn_token = os.environ.get("API_KEY_TRACXN")
    if tracxn_token != "none":
        return tracxn_token
    else:
        print("No Traxcn API token found in OS. Please save the token under 'API_KEY_AIRTABLE'")
        return False

def requestData(fUrl):
    url = fUrl
    requestBody = {
        "filter":{
            "domain":[
                simplifyUrl(url)
                ]
        }
    }
    #Actual Traxcn request happeninghere
    #NOTE: Explain the request library and why we use this to make the request
    result = requests.post("https://tracxn.com/api/2.2/companies", headers={'accessToken': tracxn_token}, json=requestBody)
    #TODO: Look at JSON Files and how to formate them
    return result.json()

#TODO: Check if this is bullet proof for Tracxn API
def simplifyUrl(fUrl):
    url = fUrl
    # Check if the URL has a scheme. If not, prepend 'http://'.
    if not urlparse(url).scheme:
        url = 'http://' + url

    parsed_url = urlparse(url)
    domain = parsed_url.netloc

    # Remove 'www.' if it exists
    if domain.startswith('www.'):
        domain = domain[4:]

    # Remove port number if it exists
    domain = domain.split(':')[0]

    return domain


'''
The dictionary (fFieldNames) is used to track:
1. What data should be added to the table
2. In which field the data should be stored

For this:
1. The data where there is no field provided or available will not be filled in
2. The data that is not provided from Tracxn will be empty (?)

The structure should look like the following:
TODO: Check how dicts work -,- and define the to-be structure



'''
#TODO: How to make check for URL (existence) a boolean?
def addDataToTable(fFieldNames, checkForURL):
    pass

#TODO: Check the structure Traxcn uses for its data. Can it be different with different companies?
def extractData(jsonFile):
    pass

#TODO: Wie bennent man Parameter nochmal vernünftig?
#TODO: Kann man nicht über den Link einfach den Base und Table Key herausfinden?
#TODO: Gibt es eine Main-Funktion in Python? Vor allem mit Parametern
'''def tracxn_airtable_api_main(fCompanyUrl, fBaseKey, fTableKey):
    company_url = fCompanyUrl
    baseKey = fBaseKey
    tableKey = fTableKey
'''
airtable_api = getAirtableAPI()
airtable_table = getAirtableTable(baseKey, tableKey)
tracxn_token = getTraxcnToken()