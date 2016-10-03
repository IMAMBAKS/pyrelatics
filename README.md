# PyRelatics

PyRelatics an API for Relatics DB connection. 

# Installation

Install via pip:

    pip install pyrelatics

# Getting started
PyRelatics allows you to get data from Relatics,
import data into relatics and invoke relatics_api methods.
   
## Example

Prime connection to DB:
```python
from pyrelatics import RelaticsAPI

# Create a RelaticeAPI instance (prime connection)
relaticsapi = RelaticsAPI('company_name', 'environment_id', 'workspace_id')
```

Get data from Relatics:

```python
from pyrelatics import RelaticsAPI

# Create a RelaticeAPI instance (prime connection)
relaticsapi = RelaticsAPI('company_name', 'environment_id', 'workspace_id')

# Prepare (optional) parameters
parameters=('dummy_parameter_name', 'dummy_parameter_value')

# Get data (if there are no parameters don't pass it to the function)
relaticsapi.GetResult('dummy_operation_name', 'dummy_entry_code', parameters=parameters)
```
Import data into Relatics:

```python
from pyrelatics import RelaticsAPI

# Create a RelaticeAPI instance (prime connection)
relaticsapi = RelaticsAPI('company_name','environment_id', 'workspace_id')

# Prepare data
data= [{'name': 'test', 'description':'descrtest'},{'name': 'test2', 'description':'descrtest2'}]

# Import data
relaticsapi.Import('dummy_operation_name', 'dummy_entry_code', data=data)
```

Create an instance of an Element, Update its name and create a relation
with another instance Element:

```python
from pyrelatics import RelaticsAPI

# Create a RelaticeAPI instance (prime connection)
relaticsapi = RelaticsAPI('company_name', 'environment_id', 'workspace_id')
              
# Login to your environment
relaticsapi.login('username', 'password')
 
# Create element and update it's name
cor_element ='dummy_element_ID'
result = relaticsapi.CreateInstanceElement(cor_element).Element.ID
relaticsapi.UpdateInstanceElement((result, 'name', 'nameOfResult'))
 
R1=result
R2='dummy_R2'
Relation ='dummy_relation'
relaticsapi.CreateInstanceRelation((R1, R2, Relation))
```
For all methods see the SOAP API in the knowledge base


# Changelog

**Version 0.21:**

- Warning will shop up if user login fails
- Wheel package now available

**Version 0.20:**

- Rename package to PyRelatics
- 100% test coverage 
- Python 3+ only