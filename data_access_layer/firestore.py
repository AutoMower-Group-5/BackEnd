import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage

# Use a service account.
cred = credentials.Certificate("serviceAccountKey.json")
app = firebase_admin.initialize_app(cred, {'storageBucket': 'robot-group5.appspot.com'})
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

def writeImage(img, imgLabel):

    bucket = storage.bucket() # storage bucket
    try:
        blob = bucket.blob(img)
        blob.upload_from_filename(img)
        blob.make_public()
        blob.public_url

        doc_ref = db.collection(u'Mower').document(u'MowerSession').collection(u'Images')
        doc_ref.add({
            u'Label': imgLabel,
            u'Url': blob.public_url
        })
    except:
        return {"Error": "An Error Occured upploading file"}
    else:
        return {"Success": "Succesfully uploaded file"}

def readImages():
    try:
        users_ref = db.collection(u'Mower').document(u'MowerSession').collection(u'Images')
        docs = users_ref.stream()

        dict = {}
        for doc in docs:
            dict[doc.id] = doc.to_dict()
        return dict
    except:
        return {"Error": "An Error Occured reading images"}