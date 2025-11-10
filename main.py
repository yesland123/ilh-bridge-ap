from fastapi import FastAPI
from ap.client import APClient

app = FastAPI()

# 1. Config temporaire des identifiants AP (on mettra propre plus tard)
AP_USERNAME = "3125460d"
AP_PASSWORD = "SvszYMUHbR"

client = APClient(AP_USERNAME, AP_PASSWORD)

@app.get("/")
def home():
    return {"message": "ILH Bridge AP - Version 1 OK ✅"}

# 2. Route test : recherche d'une référence
@app.get("/search")
def search(ref: str):
    try:
        result = client.search(ref)
        return {
            "reference": ref,
            "result": result
        }
    except Exception as e:
        return {"error": str(e)}
