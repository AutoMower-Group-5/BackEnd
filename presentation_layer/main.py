from fastapi import FastAPI

import presentation_layer.routers as routers

app = FastAPI()

app.include_router(routers.image_router)
app.include_router(routers.path_router)
app.include_router(routers.session_router)
#welcome endpoint to our REST API
@app.get("/")
async def root():
    return {"Welcome to our API": "add /docs to the url to access the swagger documentation"}