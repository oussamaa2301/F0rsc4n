import requests
import json
from tabulate import tabulate
# Defining the api-endpoint
url = 'https://api.abuseipdb.com/api/v2/check'

def scanip1(ip1):
    querystring = {
        'ipAddress': ip1,
        'maxAgeInDays': '90'
    }

    headers = {
        'Accept': 'application/json',
        'Key': '754f18d2e4eb51f2ebe34bbc07c1dd26cd358a01b72ef82f1bc59d4bcc47ae7457d78e285dd12fab'
    }

    response = requests.request(method='GET', url=url, headers=headers, params=querystring)
    r = response.json()

#zeeeyeed 
#create data
    data = [["ipAddress", r['data']['ipAddress']],
            ["abuseConfidenceScore", r['data']['abuseConfidenceScore']], 
            ["countryCode", r['data']['countryCode']], 
            ["domain", r['data']['domain']], 
            ["ipVersion", r['data']['ipVersion']],
            ["isPublic", r['data']['isPublic']],
            ["isWhitelisted", r['data']['isWhitelisted']],
            ["isp", r['data']['isp']],
            ["numDistinctUsers", r['data']['numDistinctUsers']],   
            ["totalReports", r['data']['totalReports']],   
            ["usageType", r['data']['usageType']],   
            ]
    return data        
  
#define header names
    col_names = ["Options", "Results"]
    #res2=r['data']['ipAddress']
    if (r['data']['abuseConfidenceScore']>0):
        return ('This IP was reported '+str(r['data']['totalReports'])+ ' times. Confidence of Abuse is '+str(r['data']['abuseConfidenceScore'])+'%'+' harmful ')
    else:
        return 'harmless '   

#display table
    #return(res2,res3)

