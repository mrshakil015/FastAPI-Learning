from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open('../patients.json','r') as f:
        data = json.load(f)
    return data

@app.get('/all_patients')
def view_all():
    data = load_data()
    return data