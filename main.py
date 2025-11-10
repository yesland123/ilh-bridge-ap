from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ILH Bridge AP – Version 1 OK ✅"}
