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

def writeImage():
    file_path = "sample_image.jpg"
    bucket = storage.bucket() # storage bucket
    try:
        blob = bucket.blob(file_path)
        blob.upload_from_filename(file_path)
    except:
        return {"Error": "An Error Occured upploading file"}
    else:
        return {"Success": "Succesfully uploaded file"}
    
def readImage():
    file_path = "sample_image.jpg"
    bucket = storage.bucket() # storage bucket
    try:
        blob = bucket.blob(file_path)
        # blob.make_public()
        return {"Download Url", blob.public_url}
    except:
        return {"Error": "An Error Occured upploading file"}