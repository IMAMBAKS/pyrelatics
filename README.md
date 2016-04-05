# relatics_api

With this API a connection can be made with the Relatics database.


#### Example RelaticsAPI

<b>Create Instance and update name</b>

```python
    from relatics_api.soap import RelaticsAPI

    relaticsapi = RelaticsAPI(username, password, company_name, environment_id, workspace_id)
    result = relaticsapi.CreateInstanceElement(CoR).Element.ID
    relaticsapi.UpdateInstanceElement(result,'name', 'nameOfResult')
```

<b>Create instance relation</b>
```python
    relaticsapi.CreateInstanceRelation((R1, R2, Relation))
```

For all methods see the SOAP API in the knowledge base.
