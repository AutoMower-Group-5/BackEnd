from fastapi import APIRouter
from pydantic import BaseModel
import base64
import uuid

import business_logic_layer as BLL
import data_access_layer as DAL

class ImageData(BaseModel):
    encodedImg: str

image_router = APIRouter(prefix='/image')


@image_router.get('/get')
def getImages():
    return DAL.readImages()

# Should be changed to a post request when hosted.
@image_router.post('/post')
def postImage(img: ImageData):
    imgDecoded = base64.b64decode(img.encodedImg)
    file_name = str(uuid.uuid4()) + ".jpg"

    imgURL = DAL.uploadImageToStorage(imgDecoded, file_name)
    imgLabel = BLL.classifyImage(imgURL)

    return DAL.writeImage(imgURL, imgLabel)

# Session functions below


@image_router.get('/session/get')
def getImages():
    return DAL.readImagesSession()

@image_router.post('/session/post')
def postImage(img: ImageData):
    imgDecoded = base64.b64decode(img.encodedImg)
    file_name = str(uuid.uuid4()) + ".jpg"

    imgURL = DAL.uploadImageToStorage(imgDecoded, file_name)
    imgLabel = BLL.classifyImage(imgURL)

    return DAL.writeImageSession(imgURL, imgLabel)


