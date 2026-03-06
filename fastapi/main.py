from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello!"}

app.mount("/", StaticFiles(directory="static", html=True), name="static")