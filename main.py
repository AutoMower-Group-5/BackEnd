from fastapi import FastAPI
import firestore
from pydantic import BaseModel
from typing import Union

class MowerPath(BaseModel):
    xPath: str
    yPath: str
    xValue: str
    yValue: str

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.get('/position')

def getPositionalData():
    docs = firestore.readData()
    for doc in docs:
        print(f'{doc.id}: {doc.to_dict()}')
        return "{doc_id}: {doc}".format(doc_id = doc.id, doc = doc.to_dict())
@app.post('/createPath')
def postPositionalData(mowerPath: MowerPath):
    firestore.writeDataTest(mowerPath.xPath,mowerPath.xValue,mowerPath.yPath,mowerPath.yValue)

@app.get('/something')
def something():
    return { "Data" : "World"}