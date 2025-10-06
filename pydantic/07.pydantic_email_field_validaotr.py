from pydantic import BaseModel, EmailStr, field_validator

class Patient(BaseModel):
    name: str
    email: EmailStr

    
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]
        
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        
        return value

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print("inserted data")

#--------valid patient info
valid_patient_info = {
    "name": "Md. Shakil",
    "email": "abc@hdfc.com",
	}
patient2 = Patient(**valid_patient_info )
insert_patient_data(patient2)

#-----invalid patient info
invalid_patient_info = {
    "name": "Md. Shakil",
    "email": "abc@gmail.com",
	}

	
patient1 = Patient(**invalid_patient_info)
insert_patient_data(patient1)

