from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    email: EmailStr #Email data validation
    linkedin_url: AnyUrl #url data validation
    age: int
    weight: float
 

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted data")

patient_info = {
    "name": "Md. Shakil",
    "email": "abc@email.com",
    "linkedin_url": "https://linkedin.com",
    "age": 27,
    "weight": 70.5,

}

patient1 = Patient(**patient_info)
insert_patient_data(patient1)