import requests
import json
from tabulate import tabulate
# Defining the api-endpoint
url = 'https://api.abuseipdb.com/api/v2/check'

def scanip1():
    querystring = {
        'ipAddress': '139.255.245.88',
        'maxAgeInDays': '90'
    }

    headers = {
        'Accept': 'application/json',
        'Key': 'f267b1c8c7c387337b17cb9159fe536b09101f2c7acedc696a899a4bf3e5804950858e0d61661516 '
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
  
#define header names
    col_names = ["Options", "Results"]
    #res2=r['data']['ipAddress']
    if (r['data']['abuseConfidenceScore']>0):
        return ('This IP was reported '+str(r['data']['totalReports'])+ ' times. Confidence of Abuse is '+str(r['data']['abuseConfidenceScore'])+'%'+' harmful ')
    else:
        return 'harmless '   

#display table
    #return(res2,res3)
#--------------------------------------------------------------------------------------------------------------------
#filtrer.py
from ip import scanip1
def filtrer(filename):

    with open(filename,'r') as in_file, open('iplist_out.csv','w') as out_file:
        seen = set()
        for line in in_file:
            if line in seen: continue

            seen.add(line)
            out_file.write(line)
        out_file.close()
        with open('final.csv','w') as a,open("iplist_out.csv","r") as out_file:
            for line in out_file:
                a.write(scanip1(str(line)))


    pass
#---------------------------------------------------------- Chou 
 with open('iplist_out.txt','r') as out_file: 

        for line1 in out_file:
            s = line1
            str(s)
            l.append(s)
            l.append(scanip1(str(line1)))
            with open('demo_csv1.csv', 'w') as f:
                writer = csv.writer(f) #this is the writer object
                writer.writerow(column_name) # this will list out the names of the columns which are always the first entrries
                writer.writerow(l)
            l = []





       with open('iplist_out.csv', 'a') as csv_file:

            dict_object = csv.DictWriter(csv_file, fieldnames='B') 
            #for line1 in out_file:
            
    dic = {}
    with open('iplist_out2.csv','r',newline='\n') as out_file:


        for line1 in out_file:


            dic[str(line1)] = scanip1(str(line1))
    
    with open('my_file.csv', 'w') as f:
        #dr = csv.DictReader(f, delimiter='\n')
        
        writer = csv.DictWriter(f, fieldnames= dic.keys())
        writer.writeheader()
        writer.writerow(dic)
            #scanip1(str(line))
                
            
        #out_file.close()
#*********************************urlscan.py*****************************
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

    #print(r['data']['requests'][0]['request']['requestId'])
    res1 = r['lists']['servers']
 
    return str(res1)    
    ***************************************************************filtrer**********************************
    from ip import scanip1
import csv
from csv import writer,reader


def writeCsvFile(fname, data, *args, **kwargs):
    """
    @param fname: string, name of file to write
    @param data: list of list of items
 
    Write data to file
    """
    mycsv = csv.writer(open(fname, 'w'), *args, **kwargs)
    for row in data:
        mycsv.writerow(row)


def filtrer(filename):

    with open(filename,'r') as in_file, open('iplist_out2.csv','w') as out_file:
        seen = set()
        for line in in_file:
            if line in seen: continue

            seen.add(line)
            out_file.write(line)

            #out_file.write(scanip1(str(line)))
        #with open('iplist_out2.csv','w') as out_file2, open('iplist_out.csv','r') as out_file:    
            #csv_reader=reader(out_file)
            #csv_writer=writer(out_file2)
        #with open('iplist_out.csv', 'a') as csv_file:

            #dict_object = csv.DictWriter(csv_file, fieldnames='B') 
            #for line1 in out_file:
    mydat = [
    ['IP','RESULT']
    ]
    l = []
 
    with open('iplist_out2.csv','r') as in_file:
        for line in in_file:
            l.append(line.replace("\n", ""))
            l.append(scanip1(line))
            #print(list)
            mydat.append(l)
            l = []
    writeCsvFile('half_cooked.csv', mydat)
 
 
 
    with open('half_cooked.csv', newline='') as in_file2:
        with open('iplist_final.csv', 'w', newline='') as out_file:
            writer = csv.writer(out_file)
            for row in csv.reader(in_file2):
                if row:
                    writer.writerow(row)
            
#*****************************************table 
<html>
    <style>
        table, th, td {
          border: 1px solid black;
        }
        </style>
<head>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  
</head>
<body>
  <div>
    <table class="table table-dark table-hover">
      <tr>
        {% for header in headings %}
        <th class="cell">{{header}}</th>
        {% endfor %}
        <th>IP </th>
        <th>Result </th>
      </tr>
      {% for row in outputip %}
      <tr class="row">
        
        <td>{{row[0]}}</td>
        <td>{{row[1]}}</td>
          
      </tr>
      {% endfor %}
    </table>
    <button onclick="history.back()">Go Back</button>
  </div>  
</body>
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</html>
 

                
                    ################################################""
                    from flask import Flask, request, render_template, send_file
from urlscan import servers
from ip import scanip1
from filter1 import filtrer
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html') 

@app.route('/services')
def services():
    return render_template('services.html')  

@app.route('/pricing')
def pricing():
    return render_template('pricing.html') 

@app.route('/contact')
def contact():
    return render_template('contact.html') 

@app.route('/ipscan')
def ipscan():
    return render_template('ipscan.html') 

@app.route('/scan',methods =["POST"]) 
def scan():
    url = request.form.get("url")
    #return ipscan(url)
    return render_template('resultscan.html',output=servers(url)) 
   
     

@app.route('/scanip',methods =["POST"]) 
def scanip():
    ip1 = request.form.get("ip1")
    return render_template('scanipresult.html',outputip=scanip1(ip1)) 

@app.route('/scanipfile',methods =["POST"]) 
def scanipfile():
    filename = request.form.get("filename")
    return render_template('ipscan.html',outputip=filtrer(filename)) 

@app.route   ('/return_file')
def return_file():
    return send_file()

@app.route('/file_downloads')
def file_downloads():
    return render_template('ipscan.html')     


if __name__ == "__main__":
    app.run(debug=True, port=5001)    
