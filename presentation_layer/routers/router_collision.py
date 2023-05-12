from fastapi import APIRouter
from pydantic import BaseModel

import data_access_layer as DAL

class CollisionCoordinates(BaseModel):
    xCoordinate: float
    yCoordinate: float

collision_router = APIRouter(prefix='/collision')

@collision_router.get('/get')
def getCollision():
    return DAL.readCollision()
    
@collision_router.post('/post')
def postCollision(collisionCoordinates: CollisionCoordinates):
    return DAL.writeCollision(collisionCoordinates.xCoordinate, collisionCoordinates.yCoordinate)


# Session functions below


@collision_router.get('/session/get')
def getCollision():
    return DAL.readCollisionSession()

@collision_router.post('/session/post')
def postCollision(collisionCoordinates: CollisionCoordinates):
    return DAL.writeCollisionSession(collisionCoordinates.xCoordinate, collisionCoordinates.yCoordinate)
