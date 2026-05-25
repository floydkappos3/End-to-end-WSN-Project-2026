from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["wsn_database"]
collection = db["sensor_data"]

@app.route("/")
def home():

    mode = request.args.get("mode","live")

    if mode=="history":
        data = list(collection.find().sort("timestamp",-1))
        title="Full History"
    else:
        data = list(collection.find().sort("timestamp",-1).limit(100))
        title="Live (100)"

    html=f"""
    <html>
    <head>
        <meta http-equiv="refresh" content="3">
        <title>WSN Dashboard</title>
    </head>

    <body>
    <h1>WSN Sensor Dashboard</h1>

    <a href="/?mode=live">
        <button>Live (100)</button>
    </a>

    <a href="/?mode=history">
        <button>Full History</button>
    </a>

    <h3>{title}</h3>

    <table border="1">

    <tr>
    <th>ID</th>
    <th>Count</th>
    <th>Temp</th>
    <th>Humidity</th>
    <th>Photo</th>
    <th>Solar</th>
    </tr>
    """

    for d in data:

        html+=f"""
        <tr>
        <td>{d['id']}</td>
        <td>{d['count']}</td>
        <td>{d['temp']}</td>
        <td>{d['humidity']}</td>
        <td>{d['photo']}</td>
        <td>{d['solar']}</td>
        </tr>
        """

    html+="</table></body></html>"

    return html


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
