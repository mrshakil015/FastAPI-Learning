from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str,Field(max_length=50, title='Patient Name', description='Give the name of the patient in less than 50 chars', examples=['Shakil','Nitish'])]
    email: EmailStr 
    married: Annotated[bool, Field(description='Is the patient married or not')]=False
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0)]
    allergies: Optional[List[str]]
 

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