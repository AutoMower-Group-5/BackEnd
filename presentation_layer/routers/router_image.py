from fastapi import APIRouter
from pydantic import BaseModel
import base64
import uuid

import business_logic_layer as BLL
import data_access_layer as DAL

class ImageData(BaseModel):
    encodedImg: str

image_router = APIRouter(prefix='/image')

# @image_router.post("/classification")
# async def getImageClassification(image_data: ImageData):
#     image_url = image_data.image_url

#     labels = BLL.classifyImage(image_url)

#     return {"labels": labels}

# Should be changed to a post request when hosted.
@image_router.post('/write')
def saveImage(img: ImageData):
    imgDecoded = base64.b64decode(img.encodedImg)
    file_name = str(uuid.uuid4()) + ".jpg"

    imgURL = DAL.saveImageToStorage(imgDecoded, file_name)
    imgLabel = BLL.classifyImage(imgURL['URL'])

    return DAL.writeImageArray(imgURL, imgLabel)

@image_router.get('/get')
def getImages():
    return DAL.readImagesArray()
