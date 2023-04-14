from fastapi import FastAPI
import firestore
from pydantic import BaseModel
import cloudvision
from typing import Union

class MowerPath(BaseModel):
    xPath: str
    yPath: str
    xValue: str
    yValue: str

class ImageData(BaseModel):
    image_url: str

app = FastAPI()

@app.post("/imageClassification")
async def getImageClassification(image_data: ImageData):
    image_url = image_data.image_url

    labels = cloudvision.classifyImage(image_url)

    return {"labels": labels}

@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.get('/position')

def getPositionalData():
    docs = firestore.readData()
    for doc in docs:
        print(f'{doc.id}: {doc.to_dict()}')
        return "{doc_id}: {doc}".format(doc_id = doc.id, doc = doc.to_dict())
    
@app.post('/createPath')
def postPositionalData(mowerPath: MowerPath):
    firestore.writeDataTest(mowerPath.xPath,mowerPath.xValue,mowerPath.yPath,mowerPath.yValue)

@app.get('/something')
def something():
    return { "Data" : "World"}

# Should be changed to a post request when hosted.
@app.get('/writeImage')
def postImage():
    image = "sample_image.jpg"
    imgLabel = "automower guy"
    return firestore.writeImage(image, imgLabel)

@app.get('/getImages')
def getImages():
    return firestore.readImages()