from pyairtable import Api
from pyairtable import utils
import requests
import json
import os
from urllib.parse import urlparse

def simplify_url(url):
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
            




api = Api(os.environ.get('API_KEY_AIRTABLE'))
table = api.table("appIQwr4DelJi0HRI", "tblxZB7j9cgrLFk7q")
requestUrl = "https://tracxn.com/api/2.2/companies"
accessToken = os.environ.get('API_KEY_TRACXN')



array = ['https://www.accelercomm.com/', 'https://amphenol-antennas.com/', 'https://www.antevianetworks.com/', 'https://www.attocore.com/', 'https://www.blackbeltdefence.com/', 'https://blackdice.io/', 'https://www.cambridgeconsultants.com/home', 'https://www.cellxica.net/'
         , 'https://cenerva.com/', 'https://www.cerillion.com/', 'https://digis2.com/', 'https://www.i6c.co.uk/', 'https://www.korewireless.com/', 'https://www.lifecycle-software.com/', 'https://m2mdataconnect.com/', 'https://mdsglobal.com/', 'https://www.mobiliseonline.co.uk/', 'https://www.worldov.com/', 'https://pangea-group.net/'
         , 'https://www.purelifi.com/', 'https://www.ranplanwireless.com/gb/', 'https://sbxgroup.com/kids/', 'https://www.sdi.co.uk/', 'https://smartroam.com/', 'https://www.speech-graphics.com/', 'https://squire-technologies.co.uk/', 'https://teletresearch.com/', 'https://www.tmtanalysis.com/', 'https://www.u-blox.com/en/', 'https://uktin.net/', 'https://www.vicinitysys.com/', 'https://wavemobile.net/', 'https://www.weaverlabs.io/', 'https://www.whptelecoms.com/', 'https://www.cablefree.net/']


for i in array:
    request_new(simplify_url(i))
