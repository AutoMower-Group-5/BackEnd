from fastapi import APIRouter
from pydantic import BaseModel

import data_access_layer as DAL

class CollisionCoordinates(BaseModel):
    xCoordinate: int
    yCoordinate: int

collision_router = APIRouter(prefix='/collision')

@collision_router.get('/get')
def getCollisionCoordinate():
    return DAL.getCollisionCoordinates()

@collision_router.get('/getWithSession')
def getCollisionCoordinate():
    return DAL.getCollisionCoordinatesSession()
    
@collision_router.post('/post')
def postCollisionCoordinate(collisionCoordinates: CollisionCoordinates):
    DAL.postCollisionCoordinates(collisionCoordinates.xCoordinate, collisionCoordinates.yCoordinate)

@collision_router.post('/postWithSession')
def postCollisionCoordinate(collisionCoordinates: CollisionCoordinates):
    DAL.postCollisionCoordinatesSession(collisionCoordinates.xCoordinate, collisionCoordinates.yCoordinate)