### What is FastAPI?

- FastAPI is a modern, high-performance web framework for building APIs with Python.
- It is **asynchronous** and **extremely fast** (comparable to Node.js and Go).
- Uses **type hints** for automatic validation and documentation.
- FastAPI built on top of `Starlette(for web)` and `Pydantic (for data validation)`.
    - **Starlette**: Manages how your API receives request and sends back responses.
    - **Pydantic:** is used to check if the data coming into your API is correct and in the right format

## Path Parameters

The Path() function in FastAPI is used to provide metadata, validation rules and documentation hints for path parameters in you API endpoints.

```
Title
Description
Example:
validation(ge, gt, le)
Min_length
Max_length
regex
```

```python
from fastapi import FastAPI, Path

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='ID of the patient in the DB', example='P001')):
	pass
```

## HTTPException

HTTPException is a special built-in exception in FastAPI used to return custom HTTP error response when something goes wrong in your API.

Instead of returning a normal JSON or crashing the server,we can gracefully raise an error with:

- a proper HTTP status code (like 404, 400, 403, etc.)
- a custom error message
- (optional) extra headers

```python
from fastapi import HTTPException

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='ID of the patient in the DB', example='P001')):
    # load all the patinents
    data = load_data()
    
    if patient_id in data:
        return data[patient_id]
    
    raise HTTPException(status_code=404, detail='Patient not found.')
        
```

## Query Parameter

Query parameters are optional key-value pairs appended to the end of a URL used to pass additional data to the server in an HTTP request. They are typically employed for operations like filtering, sorting, searching, and pagination without altering the endpoint path itself.

> /patients?city=Dhaka&order_by=age
> 
- The `?` marks the start of query parameters
- Each parameter is a key-value pair . `key=value`
- Multiple parameters are separated by `&`

In this case:

- `city=Dhaka` is a query parameter for filtering
- `sort_by=age` is a query parameter for sorting

`Query()` is a utility function provided by FastAPI to declare, validate, and document query parameters in our API endpoints.

It allows us to:

- Set default values
- Enforce validation rules
- Add metadata like description, title, examples

```python
from fastapi import FastAPI, HTTPException, Query

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight, or bmi'), order: str = Query('asc', description='sort in asc or desc order')):
    
    valid_fields = ['height', 'weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from: {valid_fields}')
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
    data = load_data()
    
    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    return sorted_data
    
```

## Pydantic

Pydantic work on 3 steps:

1. Define a Pydantic model that represents the ideal schema of the data.
    - This includes the expected fields, their types and any validation constrains (e.g. gt=0 for positive number).
2. Instantiate the model with raw input data (usually a dictionary or JSON like structure).
    - Pydantic will automatically validate the data and coerce it into the correct Python types (if possible)
    - If the data doesn’t meet the model’s requirements. Pydantic raise a `validationError`
3. Pass the validated model object to function or use it throughout your codebase.
    - This ensures that every part of your program works with clean, type-safe and logically valid data.

### Type Validation:

```python
from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool = False #Set default value
    allergies: Optional[List[str]] = None #set optional not required
    contact_details: Dict[str, str]
```

### Model Wise Data Validation:

```python
from pydantic import BaseModel, EmailStr, AnyUrl

class Patient(BaseModel):
    name: str
    email: EmailStr #Email data validation
    linkedin_url: AnyUrl #url data validation
    age: int
    weight: float
 
```

### Custom Data Validation:

```python
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Optional

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
```

### Meta Data using Annotated

```python
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
 
```

### Field data validation using @field_validator decorator

```python
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
```

### Email Field Validation using @field_validator decorator

```python
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

```

### Model Validation using @model_validator decorator

```python
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
```