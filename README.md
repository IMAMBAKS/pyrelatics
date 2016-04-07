# Relatics_api

With this API a connection can be made to the Relatics database.

# Changelog

- **Version: 0.15**
    - Python 2 support deprecated
    

### Example: RelaticsAPI ###

<b>Create Instance and update name</b>

```python
    from relatics_api.soap import RelaticsAPI


    relaticsapi = RelaticsAPI(company_name: str, environment_id: str,
                 workspace_id: str)
                 
    # first login
    relaticeapi.login(username:str, password:str)

    result = relaticsapi.CreateInstanceElement(CoR).Element.ID
    relaticsapi.UpdateInstanceElement(result,'name', 'nameOfResult')
```

<b>Create instance relation</b>
```python
    relaticsapi.CreateInstanceRelation((R1, R2, Relation))
```




<b>Get data from relatics db (webservice)</b>
```python
    
    relaticsapi.GetResult(self, operation_name: str, entry_code: str, parameters: str = 'None', retxml: bool = False) -> object


```


<b>Import data to relatics db (webservice)</b>
```python
    from relatics_api.soap import import_data


    relaticsapi.Import(operation_name: str, entry_code: str, data: Sequence[Mapping], retxml=False) -> object


```


For all methods see the SOAP API in the knowledge base