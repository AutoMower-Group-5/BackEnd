from flask import Flask
import firestore

app = Flask(__name__)

@app.route("/")
def readData():
    docs = firestore.readData()
    for doc in docs:
        print(f'{doc.id}: {doc.to_dict()}')
        return "{doc_id}: {doc}".format(doc_id = doc.id, doc = doc.to_dict())