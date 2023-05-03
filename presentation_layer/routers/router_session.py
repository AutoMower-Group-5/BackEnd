from fastapi import APIRouter
import data_access_layer as DAL

session_router = APIRouter(prefix='/session')

@session_router.get('/startSession')
def startSession():
    DAL.startSession()

@session_router.get('/endSession')
def endSession():
    DAL.endSession()