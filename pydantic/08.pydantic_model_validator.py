from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight:float
    married: bool
    allergies: Optional[List[str]]
    contact_details: Dict[str, str]
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        
        if model.age < 0:
            raise ValueError('Age cannot be negative')
        return model
    

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted data")

patient_info = {
    "name": "Md. Shakil",
    "email": "abc@hdfc.com",
    "age": 67,
    "weight": 70.5,
    "married": True,
    "allergies": ["Dust", "Peanuts"],
    "contact_details": {
        "phone": "+8801712345678",
        "emergency": "+12345678",
        "address": "House 12, Road 5, Dhanmondi, Dhaka"
    }

}

patient1 = Patient(**patient_info)
insert_patient_data(patient1)