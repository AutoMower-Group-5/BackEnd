import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage

# Use a service account.
cred = credentials.Certificate("serviceAccountKey.json")
app = firebase_admin.initialize_app(cred, {'storageBucket': 'robot-group5.appspot.com'})
db = firestore.client()

def postPositionData(xCoordinate,yCoordinate,angle):
    try:
        doc_ref = db.collection(u'Mower').document(u'MowerSession')
        doc_ref.update({
            'path': firestore.ArrayUnion([{
                'x': xCoordinate,
                'y': yCoordinate,
                'angle': angle
            }])
        })
        return {"Success": "Succesfully uploaded path coordinates"}
    except:
        return {"Error": "An error occurred uploading path coordinates"}
    
def postPositionDataSession(xCoordinate,yCoordinate, angle):
    try:
        mower_session_ref = db.collection(u'Mower').where('active', '==', True).limit(1)
        query_result = mower_session_ref.get()
        if len(query_result) > 0:
            doc_ref = query_result[0].reference # Get DocumentReference for matching document
            doc_ref.update({
                    'path': firestore.ArrayUnion([{
                        'x': xCoordinate,
                        'y': yCoordinate,
                        'angle': angle
                    }])
                })
            return {"Success": "Succesfully uploaded path coordinates"}
        else:
            return {"Error": "No active session found"}
    except:
        return {"Error": "An error occurred uploading path coordinates"}

def getPath():
    try:
        doc_ref = db.collection(u'Mower').document(u'MowerSession')
        doc = doc_ref.get()
        
        if doc.exists:
            return doc.to_dict().get('path')
        else:
            return {"Error": "Document containing path coordinates not found"}
    except:
        return {"Error": "An error occurred recieving path coordinates"}

def getPathSession():
    try:
        mower_session_ref = db.collection(u'Mower').where('active', '==', True).limit(1)
        query_result = mower_session_ref.get()
        
        for doc in query_result:
            if doc.exists:
                return doc.to_dict().get('path')
            else:
                return {"Error": "Document containing path coordinates not found"}
    except:
        return {"Error": "An error occurred recieving path coordinates"}
    
def postCollisionCoordinates(xCoordinate, yCoordinate):
    try:
        doc_ref = db.collection(u'Mower').document(u'MowerSession')
        doc_ref.update({
            'collision': firestore.ArrayUnion([{
                'x': xCoordinate,
                'y': yCoordinate
            }])
        })
        return {"Success": "Succesfully uploaded collision coordinates"}
    except:
        return {"Error": "An error occurred uploading collision coordinates"}

def getCollisionCoordinates():
    try:
        doc_ref = db.collection(u'Mower').document(u'MowerSession')
        doc = doc_ref.get()
        
        if doc.exists:
            return doc.to_dict().get('collision')
        else:
            return {"Error": "Document containing collision coordinates not found"}
    except:
        return {"Error": "An error occurred recieving collision coordinates"}
        
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
    try:
        mower_session_ref = db.collection(u'Mower').where('active', '==', True).limit(1)
        query_result = mower_session_ref.get()
        
        for doc in query_result:
            if doc.exists:
                return doc.to_dict().get('collision')
            else:
                return {"Error": "Document containing collision coordinates not found"}
    except:
        return {"Error": "An error occurred recieving collision coordinates"}
    
def saveImageToStorage(img, file_name):
    bucket = storage.bucket() # storage bucket
    try:
        blob = bucket.blob(file_name)
        blob.upload_from_string(img, content_type='image/jpg')
        blob.make_public()
    except:
        return ""
    else:
        return blob.public_url
    
def writeImage(imgUrl, imgLabel):
    try:
        doc_ref = db.collection(u'Mower').document(u'MowerSession')
        doc_ref.update({
            'images': firestore.ArrayUnion([{
                'URL': imgUrl,
                'Label': imgLabel
            }])
        })
        return {"Success": "Succesfully uploaded file"}
    except:
        return {"Error": "An Error Occured upploading file"}
    
def writeImageForSession(imgUrl, imgLabel):
    #Got help from ChatGPT with this function
    try:
        mower_session_ref = db.collection(u'Mower').where('active', '==', True).limit(1)
        query_result = mower_session_ref.get()
        if len(query_result) > 0:
            doc_ref = query_result[0].reference # Get DocumentReference for matching document
            doc_ref.update({
                    'images': firestore.ArrayUnion([{
                        u'Label': imgLabel,
                        u'Url': imgUrl
                    }])
                })
            return {"Success": "Succesfully uploaded image"}
        else:
            return {"Error": "No active sessions found"}
    except:
        return {"Error": "An error occurred uploading image"}
    
def getImagesSession():
    try:
        mower_session_ref = db.collection(u'Mower').where('active', '==', True).limit(1)
        query_result = mower_session_ref.get()
        
        for doc in query_result:
            if doc.exists:
                return doc.to_dict().get('images')
            else:
                return {"Error": "Document containing collision coordinates not found"}
    except:
        return {"Error": "An error occurred recieving collision coordinates"}
    
def readImages():
    try:    
        doc_ref = db.collection(u'Mower').document(u'MowerSession')
        doc = doc_ref.get()
        
        if doc.exists:
            print(doc.to_dict().get('images'))
            return doc.to_dict().get('images')
        else:
            return {"Error": "Document containing images not found"}
    except:
        return {"Error": "An error occurred recieving images"}

    
def startSession():
    try:
            
        # #Got help from ChatGPT with start and end session functions
        doc_ref = db.collection('Mower').document()

        # add the active attribute to the parent document
        doc_ref.set({
            'active': True
        })
        return {"Success": "Succesfully session started"}
    except:
        {"Error": "An error occurred starting session"}

def endSession():
    try:
        mowers_ref = db.collection('Mower')
        active_mower_query = mowers_ref.where('active', '==', True).limit(1)
        active_mower_docs = active_mower_query.get()

        for doc in active_mower_docs:
            doc.reference.update({'active': False})

        return {"Success": "Succesfully ended session"}
    except:
        {"Error": "An error occurred ending session"}