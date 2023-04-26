import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage
from pydantic import BaseModel

# Use a service account.
cred = credentials.Certificate("serviceAccountKey.json")
app = firebase_admin.initialize_app(cred, {'storageBucket': 'robot-group5.appspot.com'})
db = firestore.client()

class MowerPath(BaseModel):
    x: int
    y: int

def getPositionData():
    try:
        pos_ref = db.collection(u'Mower').where(u"active", u"==", True)
        docs = pos_ref.stream()

        path_list = list()
        for doc in docs:
            path_list = doc.to_dict()["Path"]
        return path_list
    except:
        return {"Error": "An Error Occured Getting Position Data"}

def writeDataTest(position: MowerPath):
    pos_ref = db.collection(u'Mower').where(u"active", u"==", True)
    docs = pos_ref.stream()
    path_list = list()
    for doc in docs:
        path_list = doc.to_dict()["Path"]
    path_list.append({
        "x": position.x,
        "y": position.y
        })
    print(path_list)
    pos_ref.update({
        u'Path' : path_list,
    }, merge=True)

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

def saveImageToStorage(img, file_name):
    bucket = storage.bucket() # storage bucket
    try:
        blob = bucket.blob(file_name)
        blob.upload_from_string(img, content_type='image/jpg')
        blob.make_public()
    except:
        return {"URL": ""}
    else:
        return {"URL": blob.public_url}

def writeImage(imgUrl, imgLabel):
    try:
        doc_ref = db.collection(u'Mower').document(u'MowerSession').collection(u'Images')
        doc_ref.add({
            u'Label': imgLabel,
            u'Url': imgUrl
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
    

    