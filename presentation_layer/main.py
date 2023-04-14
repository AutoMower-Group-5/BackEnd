from fastapi import FastAPI

import presentation_layer.routers as routers

app = FastAPI()

app.include_router(routers.image_router)
app.include_router(routers.path_router)

#welcome endpoint to our REST API
@app.get("/")
async def root():
    return {"message": "Hello World"}

#test endpoint
@app.get('/something')
def something():
    return { "Data" : "World"}