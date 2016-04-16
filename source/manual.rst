Manual
======

The following will be further elaborated:

    * Get data
    * Import data
    * Using the Relatics API

============
Installation
============
Install via pip:

.. code-block:: python

    pip install pyrelatics

========
Get data
========

.. automodule:: pyrelatics

The following function can be used to read data in Relatics

.. autoclass:: RelaticsAPI
    :members: GetResult

Example
-------
.. code-block:: python

    from pyrelatics import RelaticsAPI

    # Create a RelaticeAPI instance (prime connection)
    relaticsapi = RelaticsAPI('company_name','environment_id', 'workspace_id')

    # Prepare (optional) parameters
    parameters=('dummy_parameter_name','dummy_parameter_value')

    # Get data (if there are no parameters don't pass it to the function)
    relaticsapi.GetResult('dummy_operation_name', 'dummy_entry_code', parameters=parameters)

===========
Import data
===========
Sending data is done by an Import definition. If the data does not exist, new data will be created; otherwise updated.

.. autoclass:: RelaticsAPI
    :members: Import

Example
-------
.. code-block:: python

    from pyrelatics import RelaticsAPI

    # Create a RelaticeAPI instance (prime connection)
    relaticsapi = RelaticsAPI('company_name','environment_id', 'workspace_id')

    # Prepare data
    data= [{'name': 'test', 'description':'descrtest'},{'name': 'test2', 'description':'descrtest2'}]

    # Import data
    relaticsapi.Import('dummy_operation_name', 'dummy_entry_code', data=data)


=======================
Relatics API Operations
=======================


Example
-------
.. code-block:: python

    from pyrelatics import RelaticsAPI

    # Create a RelaticeAPI instance (prime connection)
    relaticsapi = RelaticsAPI('company_name', 'environment_id', 'workspace_id')

    # Login to your environment
    relaticsapi.login('username', 'password')

    # Create element and update it's name
    cor_element = 'dummy_element_ID'
    result = relaticsapi.CreateInstanceElement(cor_element).Element.ID
    relaticsapi.UpdateInstanceElement(result,'name', 'nameOfResult')

    R1=result
    R2='dummy_R2'
    Relation ='dummy_relation'
    relaticsapi.CreateInstanceRelation((R1, R2, Relation))


