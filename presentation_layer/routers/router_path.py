from fastapi import APIRouter
from pydantic import BaseModel

import data_access_layer as DAL

class MowerPath(BaseModel):
    xCoordinate: float
    yCoordinate: float
    angle: float

path_router = APIRouter(prefix='/path')

@path_router.get('/get')
def getPosition():
    return DAL.readPath()

@path_router.post('/post')
def postPosition(mowerPath: MowerPath):
    return DAL.writePath(mowerPath.xCoordinate, mowerPath.yCoordinate, mowerPath.angle)

# Session functions below
 
@path_router.get('/session/get')
def getPosition():
    return DAL.readPathSession()

@path_router.post('/session/post')
def postPosition(mowerPath: MowerPath):
    return DAL.writePathSession(mowerPath.xCoordinate, mowerPath.yCoordinate, mowerPath.angle)
