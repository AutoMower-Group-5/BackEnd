from fastapi import APIRouter
from pydantic import BaseModel

import business_logic_layer as BLL
import data_access_layer as DAL

class ImageData(BaseModel):
    image_url: str

image_router = APIRouter(prefix='/image')

@image_router.post("/classification")
async def getImageClassification(image_data: ImageData):
    image_url = image_data.image_url

    labels = BLL.classifyImage(image_url)

    return {"labels": labels}

# Should be changed to a post request when hosted.
@image_router.get('/write')
def postImage():
    image = "sample_image.jpg"
    imgLabel = "automower guy"
    return DAL.writeImage(image, imgLabel)

@image_router.get('/get')
def getImages():
    return DAL.readImages()