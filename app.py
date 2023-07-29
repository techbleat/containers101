
from flask import Flask
import redis

app = Flask(__name__)
version = "1.7.1"

r = redis.Redis(host="cache-server", port=6379)

@app.route("/getregion/<country>")
def lookup(country):
    value ="N/A"
    try:
        value = r.get (country)
    except:
        pass
    return value 

@app.route("/version")
def getversion():
    return version

@app.route("/saveregion/<country>/<city>")
def savedata(country,city):
    value ="pass"
    try:
        r.set(country,city)
    except:
        value = "fail"
    return value 


