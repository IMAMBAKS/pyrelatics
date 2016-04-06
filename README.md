# relatics_api

With this API a connection can be made to the Relatics database.

The following is supported:

   * [Invoke the RelaticsAPI](#example-relaticsapi)
   * [Get data from relatics (webservice)](#example-get-data-from-relatics-db-webservice)
   * [Import data to relatics (webservice)](#example-import-data-to-relatics-db-webservice)

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

For all methods see the SOAP API in the knowledge base.

### Example: Get data from relatics db (webservice)

```python
    from relatics_api.soap import read_data


    read_data(company_name: str, workspace: str, operation: str, entry_code: str, retxml: bool = True)


```

### Example: Import data to relatics db (webservice)

```python
    from relatics_api.soap import import_data


    import_data(company_name: str, workspace: str, operation: str, entry_code: str, data)


```