import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate("serviceAccountKey.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

def writeDataTest(a,b,c,d):
    doc_ref = db.collection(u'Robot').document(u'Position')
    doc_ref.set({
        a : b,
        c : d
    })

def writeData():
    doc_ref = db.collection(u'Robot').document(u'Position')
    doc_ref.set({
        u'X': u'5',
        u'Y': u'10'
    })

def readData():
    users_ref = db.collection(u'Robot')
    docs = users_ref.stream()

    # for doc in docs:
    #     print(f'{doc.id} => {doc.to_dict()}')
    return docs

readData()