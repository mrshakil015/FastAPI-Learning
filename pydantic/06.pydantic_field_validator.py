from pydantic import BaseModel, EmailStr, field_validator
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight:float
    married: bool
    allergies: Optional[List[str]]
    contact_details: Dict[str, str]
    
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]
        
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator('age')
    @classmethod
    def validate_age(cls, value):
        if value < 0:
            raise ValueError('Age cannot be negative')
        return value

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted data")

patient_info = {
    "name": "Md. Shakil",
    "email": "abc@hdfc.com",
    "age": -27,
    "weight": 70.5,
    "married": True,
    "allergies": ["Dust", "Peanuts"],
    "contact_details": {
        "phone": "+8801712345678",
        "address": "House 12, Road 5, Dhanmondi, Dhaka"
    }

}

patient1 = Patient(**patient_info)
insert_patient_data(patient1)