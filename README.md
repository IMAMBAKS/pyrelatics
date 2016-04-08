# PyRelatics

With this API a connection can be made to the Relatics database.

## Changelog

**Version 0.20:**

- Rename package to PyRelatics
- 100% test coverage 
- Python 3+ only
   
   
## Examples

**1. Get data (webservice)**
```python
from pyrelatics import RelaticsAPI

# Create a RelaticeAPI instance (prime connection)
relaticsapi = RelaticsAPI('company_name','environment_id', 'workspace_id')

# Prepare parameters
parameters=('dummy_parameter_name','dummy_parameter_value')

# Get data (if there are no parameters don't pass it to the function)
relaticsapi.GetResult('dummy_operation_name', 'dummy_entry_code', parameters=parameters)
```

**2. Create Instance Element, Update name and Create relation**

```python
from pyrelatics import RelaticsAPI

# Create a RelaticeAPI instance (prime connection)
relaticsapi = RelaticsAPI('company_name','environment_id', 'workspace_id')
              
# Login to your environment
relaticsapi.login('username', 'password')
 
# Create element and update it's name
cor_element = 'dummy_element_ID'
result = relaticsapi.CreateInstanceElement(cor_element).Element.ID
relaticsapi.UpdateInstanceElement(result,'name', 'nameOfResult')
 
R1=result
R2='dummy_R2'
Relation = 'dummy_relation'
relaticsapi.CreateInstanceRelation((R1, R2, Relation))
```


**3. Import data (webservice)**

```python
from pyrelatics import RelaticsAPI

# Create a RelaticeAPI instance (prime connection)
relaticsapi = RelaticsAPI('company_name','environment_id', 'workspace_id')

# Prepare data
data= [{'name': 'test', 'description':'descrtest'},{'name': 'test2', 'description':'descrtest2'}]

# Import data
relaticsapi.Import('dummy_operation_name','dummy_entry_code', data=data)
```



For all methods see the SOAP API in the knowledge base