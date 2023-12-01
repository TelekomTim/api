from pyairtable import Api
from pyairtable import utils
import requests
import json
import os
from urllib.parse import urlparse

def simplify_url(url):
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

def request_new(furl):
    requestBody = {
        "filter":{
            "domain":[
                furl
                ]
        }
    }

    res = requests.post(requestUrl, headers={'accessToken': accessToken}, json=requestBody)
    result = res.json()
    # Ist die Anfrage leer? Dann nur url drucken
    if result=="":
        table.create({
            "URL": furl,
        })
    else:
        for company in result.get("result", []):
            name = company.get('name', '')
            url = company.get('domain', '')
    
            try:
                desc_l = company['description']['long']
            except (KeyError, TypeError):
                desc_l = ''

            try:
                desc_s = company['description']['short']
            except (KeyError, TypeError):
                desc_s = ''

            try:
                moneyraised = company['totalMoneyRaised']['totalAmount']['amount']
            except (KeyError, TypeError):
                moneyraised = 0
            try:
                foundedYear = company['foundedYear']
            except(KeyError, TypeError):
                foundedYear = '1000'

            companyStage = company.get('stage', '')

            try:
                img = company['logos']['imageUrl']
            except (KeyError, TypeError):
                img = ''

            try:
                country = company['location']['country']
            except (KeyError, TypeError):
                country = ''
            
            try:
                tracxn_score = company['tracxnScore']
            except (KeyError, TypeError):
                tracxn_score = 0    

            categories = []
            for businessModels in company.get("businessModelList", []):
                try:
                    categories.append(businessModels['name'])
                except(KeyError, TypeError):
                    test = ''
        
            table.create({
            
            "Name": name,
            "URL": url,
            "Description (long)": desc_l,
            "Description (short)": desc_s,
            "Money raised": moneyraised,
            "Founded year": str(foundedYear) + "-01-01",
            "Company Stage": companyStage,
            "Logo": [utils.attachment(img)] if img else [],
            "Country": country,
            "Tracxn Score": tracxn_score
            })

            print(name)

def update():
    result = table.all(fields=['URL'])
    

    for url in result:
        requestBody = {
        "filter":{
            "domain":[
                url["fields"]["URL"]
                ]
            }
        } 
        tracxn_res = requests.post(requestUrl, headers={'accessToken': accessToken}, json=requestBody)
        tracxn_result = tracxn_res.json()
        for company in tracxn_result.get("result", []):
            try:
                country = company['location']['country']
            except (KeyError, TypeError):
                country = ''
            
            try:
                tracxn_score = company['tracxnScore']
            except (KeyError, TypeError):
                tracxn_score = 0
            
        table.update(url["id"], {
            "Country": country,
            "Tracxn Score": tracxn_score
        })
            



if os.environ.get('API_KEY_AIRTABLE') != "none":  
    api = Api(os.environ.get('API_KEY_AIRTABLE'))
    # Currently this is the MWC'24 Scouting Base
    table = api.table("appIQwr4DelJi0HRI", "tblxZB7j9cgrLFk7q")
else:
    print("No Airtable API key found")

if os.environ.get('API_KEY_TRACXN') != "none":  
    accessToken = os.environ.get('API_KEY_TRACXN')
    requestUrl = "https://tracxn.com/api/2.2/companies"
else:
    print("No Tracxn API key found")



array = ['https://www.adtran.com/', 'https://www.allot.com', 'amplication.com', 'www.auto-talks.com', 'http://beamshaping.io/', 'https://www.ceragon.com', 'https://www.ceva-dsp.com', 
         'https://www.d-id.com', 'https://drivenets.com', 'edgehawk.io', 'https://edgilityos.com/', 'https://www.everysight.com/', 'https://flolive.net', 'flycomm.co',
            'www.friendly-tech.com', 'https://hiskysat.com/homepage/', 'https://www.is.com', 'https://mce.systems','https://mindcti.com','https://www.mtiwe.com','https://www.nexuce.com/',
            'onelayer.com','https://www.pentenetworks.com','http://www.phinergy.com/','www.quantlr.com','https://roamability.com/','https://www.runel.net','sensorz.io',
            'https://www.shieldiot.io/','www.sqreamtech.com','http://www.techsee.me/','https://www.telco.com','https://tupaia-pos.com/','https://www.wearabledevices.co.il/']


for i in array:
   request_new(simplify_url(i))

   
