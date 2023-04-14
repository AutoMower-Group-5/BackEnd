from fastapi import APIRouter
from pydantic import BaseModel

import data_access_layer as DAL

class MowerPath(BaseModel):
    xPath: str
    yPath: str
    xValue: str
    yValue: str

path_router = APIRouter(prefix='/path')

@path_router.get('/position')
def getPositionalData():
    docs = DAL.readData()
    for doc in docs:
        print(f'{doc.id}: {doc.to_dict()}')
        return "{doc_id}: {doc}".format(doc_id = doc.id, doc = doc.to_dict())
    
@path_router.post('/create')
def postPositionalData(mowerPath: MowerPath):
    DAL.writeDataTest(mowerPath.xPath,mowerPath.xValue,mowerPath.yPath,mowerPath.yValue)