from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str = Field(max_length=50) #custom data validation
    email: EmailStr 
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120) #custom data validation
    weight: float = Field(gt=0) #custom data validation
    allergies: Optional[List[str]] = Field(max_length=5) #custom data validation
 

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted data")

patient_info = {
    "name": "Md. Shakil",
    "email": "abc@gmail.com",
    "linkedin_url": "https://linkedin.com",
    "age": 27,
    "weight": 70.5,
    "allergies": ["Dust", "Peanuts"],

}

patient1 = Patient(**patient_info)
insert_patient_data(patient1)