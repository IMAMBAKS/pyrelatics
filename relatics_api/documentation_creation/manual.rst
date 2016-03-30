Manual
======

The following will be further elaborated:

    * Read data
    * Create/Update an Element
    * Delete an Element


============
Reading data
============

Reading data from Relatics is done with it's Webservice through an Import definition. First the Relatics part will be eluded then the function.

Relatics Webservice import definition
-------------------------------------
Create a **Servers for providing data** webservice in Relatics. In the Authentication Type select **Entry code validation**

The Relatics part is done.

.. warning:: For now only **Entry code validation** is supported

Read function
-------------

The following function can be used to read data in Relatics

.. automodule:: soap
    :members: read_data


Example
+++++++
//TODO

====================
Create/Updating Data
====================
Sending data is done by an Import definition. If the data does not exist, new data will be created; otherwise updated.

.. automodule:: soap
    :members: send_data


Example
+++++++
//TODO


=============
Deleting Data
=============
Deleting data can be done with the relatics API.

.. automodule:: soap
    :members: delete_data


Example
+++++++
//TODO




