from fastapi import APIRouter
from pydantic import BaseModel

import data_access_layer as DAL

class MowerPath(BaseModel):
    xPath: float
    yPath: float
    angle: float

path_router = APIRouter(prefix='/path')

@path_router.get('/get')
def getPositionalData():
    return DAL.getPath()
 #   for doc in docs:
  #      print(f'{doc.id}: {doc.to_dict()}')
 #       return "{doc_id}: {doc}".format(doc_id = doc.id, doc = doc.to_dict())
 
@path_router.get('/get/withsession')
def getPositionalData():
    return DAL.getPathSession()
    
@path_router.post('/save')
def savePositionalData(mowerPath: MowerPath):
    DAL.postPositionData(mowerPath.xPath,mowerPath.yPath, mowerPath.angle)
    
@path_router.post('/post/withsession')
def savePositionalData(mowerPath: MowerPath):
    DAL.postPositionDataSession(mowerPath.xPath,mowerPath.yPath, mowerPath.angle)