import json
import configparser
from flask import Flask, jsonify
from flask_cors import CORS

parser = configparser.ConfigParser()
parser.read("config.ini")
db_file_path = parser["config"]["path"]
data = ""

with open(db_file_path, "r") as f:
    data = json.loads(f.read())


app = Flask(__name__)
CORS(app)


@app.route("/emoji-report")
def emoji_report():
    return jsonify(data)



app.run(port=9823)
