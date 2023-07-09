
from flask import Flask

app = Flask(__name__)
regions = {"uk":"London","nigeria":"Lagos","southafrica":"Johannesburg", "usa":"DC"}

@app.route("/getregion/<country>")
def lookup(country):
    value ="N/A"
    try:
        value = regions [country]
    except:
        pass
    return value 