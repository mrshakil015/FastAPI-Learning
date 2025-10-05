# FastAPI-Learning

### What is FastAPI?

- FastAPI is a modern, high-performance web framework for building APIs with Python.
- It is **asynchronous** and **extremely fast** (comparable to Node.js and Go).
- Uses **type hints** for automatic validation and documentation.
- FastAPI built on top of `Starlette(for web)` and `Pydantic (for data validation)`.
    - **Starlette**: Manages how your API receives request and sends back responses.
    - **Pydantic:** is used to check if the data coming into your API is correct and in the right format

### Path Parameters

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

### HTTPException

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

### Query Parameter

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