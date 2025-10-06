from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool = False #Set default value
    allergies: Optional[List[str]] = None #set optional not required
    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted data")

patient_info = {
    "name": "Md. Shakil",
    "age": 27,
    "weight": 70.5,
    "married": False,
    "allergies": ["Dust", "Peanuts"],
    "contact_details": {
        "email": "shakil@example.com",
        "phone": "+8801712345678",
        "address": "House 12, Road 5, Dhanmondi, Dhaka"
    }
}

patient1 = Patient(**patient_info)
insert_patient_data(patient1)