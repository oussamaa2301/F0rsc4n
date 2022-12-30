from flask import Flask, request, render_template, send_file, Response, make_response
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


@app.route('/scanipfile', methods=["POST"])
def scanipfile():
    filename = request.form.get("filename")
    html = render_template('download.html', outputip=filtrer(filename))
    response = make_response(send_file('iplist_final.csv', attachment_filename='iplist_final.csv', as_attachment=True, mimetype='text/csv'))
    return response


@app.route   ('/return_file')
def return_file():
    return send_file()

@app.route('/file_downloads')
def file_downloads():
    return render_template('ipscan.html')     


if __name__ == "__main__":
    app.run(debug=True, port=5001)    
