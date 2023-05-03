import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage

# Use a service account.
cred = credentials.Certificate("serviceAccountKey.json")
app = firebase_admin.initialize_app(cred, {'storageBucket': 'robot-group5.appspot.com'})
db = firestore.client()

def postPositionData(xCoordinate,yCoordinate):
    
    doc_ref = db.collection(u'Mower').document(u'MowerSession')
    doc_ref.update({
        'path': firestore.ArrayUnion([{
            'x': xCoordinate,
            'y': yCoordinate
        }])
    })
    
def postPositionDataSession(xCoordinate,yCoordinate):
    try:
        mower_session_ref = db.collection(u'Mower').where('active', '==', True).limit(1)
        query_result = mower_session_ref.get()
        if len(query_result) > 0:
            doc_ref = query_result[0].reference # Get DocumentReference for matching document
            doc_ref.update({
                    'path': firestore.ArrayUnion([{
                        'x': xCoordinate,
                        'y': yCoordinate
                    }])
                })
            return {"Success": "Succesfully uploaded path coordinates"}
        else:
            return {"Error": "No active sessions found"}
    except:
        return {"Error": "An error occurred uploading path coordinates"}

def getPath():
    doc_ref = db.collection(u'Mower').document(u'MowerSession')
    doc = doc_ref.get()
    
    if doc.exists:
        print(doc.to_dict().get('path'))
        return doc.to_dict().get('path')
    else:
        print('No such document!')
        return None

def getPathSession():
    mower_session_ref = db.collection(u'Mower').where('active', '==', True).limit(1)
    query_result = mower_session_ref.get()
    
    for doc in query_result:
        if doc.exists:
            return doc.to_dict().get('path')
        else:
            return None
    
def postCollisionCoordinates(xCoordinate, yCoordinate):
    doc_ref = db.collection(u'Mower').document(u'MowerSession')
    doc_ref.update({
        'collision': firestore.ArrayUnion([{
            'x': xCoordinate,
            'y': yCoordinate
        }])
    })

def getCollisionCoordinates():
    doc_ref = db.collection(u'Mower').document(u'MowerSession')
    doc = doc_ref.get()
    
    if doc.exists:
        return doc.to_dict().get('collision')
    else:
        print('Document does not exist.')
        return None
    
def postCollisionCoordinatesSession(xCoordinate, yCoordinate):
    #Got help from ChatGPT with this function
    try:
        mower_session_ref = db.collection(u'Mower').where('active', '==', True).limit(1)
        query_result = mower_session_ref.get()
        if len(query_result) > 0:
            doc_ref = query_result[0].reference # Get DocumentReference for matching document
            doc_ref.update({
                    'collision': firestore.ArrayUnion([{
                        'x': xCoordinate,
                        'y': yCoordinate
                    }])
                })
            return {"Success": "Succesfully uploaded collision coordinates"}
        else:
            return {"Error": "No active sessions found"}
    except:
        return {"Error": "An error occurred uploading collision coordinates"}
    
def getCollisionCoordinatesSession():
    mower_session_ref = db.collection(u'Mower').where('active', '==', True).limit(1)
    query_result = mower_session_ref.get()
    
    for doc in query_result:
        if doc.exists:
            return doc.to_dict().get('collision')
        else:
            return None

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
        doc_ref = db.collection(u'Mower').document(u'MowerSession')
        doc_ref.update({
            'images': firestore.ArrayUnion([{
                'URL': imgUrl,
                'Label': imgLabel
            }])
        })
    except:
        return {"Error": "An Error Occured upploading file"}
    else:
        return {"Success": "Succesfully uploaded file"}
    
def writeImageForSession(imgUrl, imgLabel):
    #Got help from ChatGPT with this function
    try:
        mower_session_ref = db.collection(u'Mower').where('active', '==', True).limit(1)
        query_result = mower_session_ref.get()
        if len(query_result) > 0:
            doc_ref = query_result[0].reference # Get DocumentReference for matching document
            doc_ref.update({
            'images': firestore.ArrayUnion([{
                'URL': imgUrl,
                'Label': imgLabel
            }])

            })
            return {"Success": "Succesfully uploaded file"}
        else:
            return {"Error": "No active sessions found"}
    except:
        return {"Error": "An error occurred uploading file"}
    
def readImages():
    doc_ref = db.collection(u'Mower').document(u'MowerSession')
    doc = doc_ref.get()
    
    if doc.exists:
        print(doc.to_dict().get('images'))
        return doc.to_dict().get('images')
    else:
        print('No such document!')
        return None

def readImagesForSession():
    doc_ref = db.collection(u'Mower').where('active', '==', True).limit(1).get()
    
    if len(doc_ref) > 0:
        doc = doc_ref[0].reference.get()
        print(doc.to_dict().get('images'))
        return doc.to_dict().get('images')
    else:
        print('No such document!')
        return None
    
def startSession():
    # #Got help from ChatGPT with start and end session functions
    # doc_ref = db.collection('Mower').document()

    doc_ref = db.collection('Mower').document()

    doc_ref.set({
        'images': [],
        'path': [],
        'collision': [],
        'active': True
    })

def endSession():
    mowers_ref = db.collection('Mower')
    active_mower_query = mowers_ref.where('active', '==', True).limit(1)
    active_mower_docs = active_mower_query.get()

    for doc in active_mower_docs:
        doc.reference.update({'active': False})