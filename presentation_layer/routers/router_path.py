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
 
@path_router.get('/get/withsession')
def getPositionalData():
    return DAL.getPathSession()
    
@path_router.post('/save')
def savePositionalData(mowerPath: MowerPath):
    return DAL.postPositionData(mowerPath.xPath,mowerPath.yPath, mowerPath.angle)

    
@path_router.post('/post/withsession')
def savePositionalData(mowerPath: MowerPath):
    return DAL.postPositionDataSession(mowerPath.xPath,mowerPath.yPath, mowerPath.angle)
