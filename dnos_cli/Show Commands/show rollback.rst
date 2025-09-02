show rollback
-------------

**Minimum user role:** viewer

To view the configuration of the transaction file:

**Command syntax: show rollback [rollback-id]**

**Command mode:** operational

.. **Note**

	- This command is aliased with "show file rollback".

**Parameter table**

+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------+-------+
| Parameter   | Description                                                                                                                                   | Range |
+=============+===============================================================================================================================================+=======+
| rollback-id | The rollback-id of the commit transaction file.                                                                                               | 0..49 |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------+-------+

**Example**
::

	dnRouter# show rollback 1
	#dnRouter config-start [27-Jun-2017 22:11:00]
	# version 6
	# user ADMIN
	# user logged something for this rollback
	system name dnRouter
	system login user RootUser 
	system login user RootUser description MyrootUser
	.
	.
	.
	#dnRouter config-end

.. **Help line:** view the configuration of the transaction file

**Command History**

+---------+------------------------------------------------------------------------+
| Release | Modification                                                           |
+=========+========================================================================+
| 6.0     | Command introduced                                                     |
+---------+------------------------------------------------------------------------+
| 11.0    | Command added to recovery mode                                         |
+---------+------------------------------------------------------------------------+
| 13.1    | Added display of the transaction's origin (CLI/netconf) to the output  |
+---------+------------------------------------------------------------------------+
