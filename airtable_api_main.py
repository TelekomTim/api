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
    result = table.all(view="TBU", fields=['URL'])

    for url in result:
        requestBody = {
            "filter":{
                "domain":[
                    simplify_url(url["fields"]["URL"])
                    ]
                }
            } 
        print("--------------RequestBody: ", url["fields"]["URL"],requestBody, sep=' : ')
        tracxn_res = requests.post(requestUrl, headers={'accessToken': accessToken}, json=requestBody)
        tracxn_result = tracxn_res.json()
        print("--------------Result:", url["fields"]["URL"],tracxn_result, sep=' : ' )
        tracxn_result
        for company in tracxn_result.get("result", []):
            name = company.get('name', '')
            url_c = company.get('domain', '')
        
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
                
            table.update(url["id"], {
                "Name": name,
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



array = ['http://www.acentury.co/','http://adtrackmedia.com/','http://www.ahead.io/','http://www.asigra.com/','http://www.avariwireless.com/',
         'http://blinqnetworks.com/','http://www.canarymedical.com/','http://cemworks.com/','http://colonynetworks.com/',
         'https://daanaa.com/','https://www.dejero.com/','http://www.earthsight.net/','https://www.expeto.io/','https://www.ferrotechnics.com/',
         'https://www.fledge.health/','https://fx.land/','http://www.galtronics.com/','https://www.geotab.com/','https://www.incognito.com/',
         'http://www.kloudville.com/','http://www.latencetech.com/','http://www.limegroup.ca/','http://www.linkwavewireless.com/','http://www.makahealth.com/',
         'https://mantisxr.com/','http://www.mimik.com/','https://www.myndtx.com/','https://www.netskrt.io/','http://www.netsweeper.com/','https://novapex.ca/',
         'https://www.noviflow.com/','https://www.one37id.com/','https://www.planethoster.com/','http://www.pxrlabs.com/','https://www.redoaktechnologies.ca/',
         'http://www.rigstar.ca/','https://www.shabodi.com/','https://www.shapeimmersive.com/','https://simplyask.ai/','http://www.sinctech.com/','http://www.smoothtalker.com/',
         'http://www.solace.ca/','http://www.sparkgeo.com/','https://www.starsolutions.com/','https://symend.com/','https://tektelic.com/','https://www.telesat.com/',
         'https://thinkrf.com/','http://www.tieroneoss.com/','http://trulioo.com/','https://www.veltris.com/','http://viewpoint.ai/','https://www.viionsystems.com/',
         'http://warrantylife.com/','http://www.wedgenetworks.com/']


for i in array:
   request_new(simplify_url(i))
