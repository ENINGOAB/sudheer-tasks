from flask import Flask
#from pymongo import MongoClient
import os,socket
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://eup-test:e31nKQyd7f8Oys0j@uc-testing-cluster.byiujgf.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

app = Flask(__name__)
@app.route("/")
def get_workorders():
    WOCaseId_data = []
    WorkOrders_data = []
    DataBase_data = []
    new=client.list_database_names()
    for i in new:
        db = client[i]
        db1 = db.list_collection_names()
        for j in db1:
            if j == "WorkOrders":
                db2 = db[j]
                documents = db2.find({},{"WOCaseId":1, "_id":0})
                for doc in documents:
                    if doc != {}:
                        doc['database']=i
                        doc['collection']=j
                        WOCaseId_data.append(doc)
    table_html = "<table>\n"
    table_html += "<tr><th>WOCaseId</th><th>Database</th><th>Collection</th></tr>\n"
    for doc in WOCaseId_data:
        row_html = "<tr>"
        row_html += "<td>{}</td>".format(doc['WOCaseId'])
        row_html += "<td>&nbsp;&nbsp;&nbsp;{}</td>".format(doc['database'])
        row_html += "<td>&nbsp;&nbsp;{}</td>".format(doc['collection'])
        row_html += "</tr>\n"
        table_html += row_html
    table_html += "</table>"

# Print the HTML table
#print(table_html)
    return table_html
