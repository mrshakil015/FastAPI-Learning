from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight:float #kg
    height: float #mtr
    married: bool
    allergies: Optional[List[str]]
    contact_details: Dict[str, str]
    
    @computed_field
    @property
    def bmi(self) -> float:
        # bmi = weight / (height*height)
        bmi = round(self.weight / (self.height**2),2)
        return bmi

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('BMI: ', patient.bmi)
    print("inserted data")

patient_info = {
    "name": "Md. Shakil",
    "email": "abc@hdfc.com",
    "age": 67,
    "weight": 70.5,
    "height": 1.72,
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