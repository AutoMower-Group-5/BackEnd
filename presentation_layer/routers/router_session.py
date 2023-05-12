from fastapi import APIRouter
import data_access_layer as DAL

session_router = APIRouter(prefix='/session')

@session_router.get('/start')
def startSession():
    return DAL.startSession()

@session_router.get('/end')
def endSession():
    return DAL.endSession()