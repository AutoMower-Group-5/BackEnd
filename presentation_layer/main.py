from fastapi import FastAPI

import presentation_layer.routers as routers

app = FastAPI()

app.include_router(routers.image_router)
app.include_router(routers.path_router)
app.include_router(routers.session_router)
app.include_router(routers.collision_router)

@app.get("/")
async def root():
    return {"Welcome to our API": "add /docs to the url to access the swagger documentation"}