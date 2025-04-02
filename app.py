from fastapi import FastAPI
from pymongo import MongoClient
from model_patient import Patient

client = MongoClient("mongodb", 27017)
db = client["banque"]
comptes = db["comptes"]

app = FastAPI()

@app.post("/patient/")
async def create_patient(patient : Patient):
    return patient