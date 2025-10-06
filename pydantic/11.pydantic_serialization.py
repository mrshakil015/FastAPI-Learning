from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address
    
address_dict = {'city': 'Savar', 'state':'Dhaka', 'zip_code': '1340'}
address1 = Address(**address_dict)

patient_dict = {'name': 'Shakil', 'gender': 'Male', 'age': 26, 'address': address1}
patient1 = Patient(**patient_dict)

convert_dict = patient1.model_dump() #convert model object to python dictionary
print(convert_dict)
print(type(convert_dict))

convert_json = patient1.model_dump_json() #convert model object to json
print(convert_json)
print(type(convert_json))

#Export specific field
convert_included_data = patient1.model_dump(include=['name', 'gender'])
print(convert_included_data)

convert_exclude_data = patient1.model_dump(exclude=['name', 'gender'])
print(convert_exclude_data)
