import requests
import json
from time import sleep


    
def servers(url):
    headers = {'API-Key':'4fc263a3-f5cc-461e-aab2-d9ea57bc5b65','Content-Type':'application/json'}
    data = {"url": url, "visibility": "public"}
    response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
    #print(type(response))
    js=response.json()
    #print(type(js))
    #print(js['uuid'])
    uuid=js['uuid']
    sleep(10)
    result = requests.get("https://urlscan.io/api/v1/result/{}/".format(uuid))

    r = result.json()
    my_data=[["Servers", r['lists']['servers']],
        ["Link domains", r['lists']['linkDomains']], 
        #["Certificate", r['lists']['certificates']['0']], 
        ["Ips", r['lists']['ips']], 
        ["Countrie", r['submitter']],
        ["Screenshot", r['task']['screenshotURL']],
        ]
        
    return my_data   