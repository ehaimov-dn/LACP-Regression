show system nst advertisements
------------------------------

**Minimum user role:** viewer

Displays current node advertisements status as received from remote nodes.


**Command syntax: show system nst advertisements** advertisement-key [advertisement-key]

**Command mode:** operational



**Note**

- Supported only on NC-AI cluster formations.

**Parameter table**

+--------------------+--------------------------------------------+-----------+-----------------+
| Parameter          | Description                                | Range     | Default value   |
+====================+============================================+===========+=================+
| Advertisement Key  | The key name represents the advertisement  | /-        | /-              |
+--------------------+--------------------------------------------+-----------+-----------------+


The following information is displayed:

+---------------------------+-----------------------------------------------------------------------------------------------------------+---------------------------------------+
| Parameter                 | Description                                                                                               | Range                                 |
+===========================+===========================================================================================================+=======================================+
| Advertisement Key         | The key name represents the advertisement                                                                 | /-                                    |
+---------------------------+-----------------------------------------------------------------------------------------------------------+---------------------------------------+
| Revision                  | The advertisement revision sent to the remote node                                                        | /-                                    |
+---------------------------+-----------------------------------------------------------------------------------------------------------+---------------------------------------+
| Timestamp                 | Timestamp when the advertisement was created                                                              | /-                                    |
+---------------------------+-----------------------------------------------------------------------------------------------------------+---------------------------------------+
| Synced Nodes              | remote nodes which responded with ACK for the advertisement out of the cluster nodes number               | /-                                    |
+---------------------------+-----------------------------------------------------------------------------------------------------------+---------------------------------------+


**Example**
::

	dnRouter# show system nst advertisements

	| Advertisement Key     | Revision | Timestamp           | Synced Nodes  |
	|-----------------------+----------+---------------------+---------------|
	| wbox.oper.ge100-0/0/0 | 3        | 26-03-2025 17:45:07 | 3/4           |
	| wbox.oper.ge100-0/0/1 | 3        | 26-03-2025 17:45:07 | 3/4           |
	| wbox.config           | 3        | 26-03-2025 17:45:07 | 4/4           |


	dnRouter# show system nst advertisements advertisement-name wbox.config

	| Advertisement Key     | Revision | Timestamp           | Synced Nodes  |
	|-----------------------+----------+---------------------+---------------|
	| wbox.config            | 3        | 26-03-2025 17:45:07 | 4/4           |
    

**Command History**

+---------+-----------------------------------------------+
| Release | Modification                                  |
+=========+===============================================+
| 25.2    | Command introduced                            |
+---------+-----------------------------------------------+
