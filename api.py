from flask import Flask, jsonify, request
from .webcrawler import checkhyperlink
from .readsuccess import checkdatabase
import readsuccess
import webcrawler

app = Flask(__name__)
@app.route('/')
def home():
    return "service on"

@app.route('/submit', methods = ['POST'])
def submit():
    url = request.json
    url = url["var"]
    
    # print(url)
    status = readsuccess.checkdatabase(url)
    
    if status == "yes":
        return "phishing"
    else :
        lanjut = webcrawler.checkhyperlink(url)

    if lanjut == "phishing":
        readsuccess.insertdata(url)
        return "phishing" 
    else :
        return "legitimate"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')