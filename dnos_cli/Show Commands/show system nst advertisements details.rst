show system nst advertisements details
--------------------------------------

**Minimum user role:** viewer

Displays detailed node advertisement status as received from remote nodes.


**Command syntax: show system nst advertisements details advertisement-key [advertisement-key]**

**Command mode:** operational



**Note**

- Supported only on NC-AI cluster formations.

- Advertisements Status
    - Unavailable - local NCP advertisement status on a remote NCP is unknown.
    - Received - local NCP advertisement was received by remote node and is pending to be processed.
    - Succeeded - local NCP advertisement was successfully applied on remote node.
    - Failed - local NCP advertisement failed to be applied by remote node. When advertisememnt status is failed, reason for the failure sould be added also.

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
| Node Type                 | The type of the remote node. Currently only supported for NCP                                             | NCP, NCF                              |
+---------------------------+-----------------------------------------------------------------------------------------------------------+---------------------------------------+
| Remote Node ID            | The ID of the remote node                                                                                 | /-                                    |
+---------------------------+-----------------------------------------------------------------------------------------------------------+---------------------------------------+
| Revision                  | The advertisement revision sent to the remote node                                                        | /-                                    |
+---------------------------+-----------------------------------------------------------------------------------------------------------+---------------------------------------+
| Timestamp                 | Timestamp when the advertisement was sent to the first remote NCP                                         | /-                                    |
+---------------------------+-----------------------------------------------------------------------------------------------------------+---------------------------------------+
| Synced Nodes              | remote nodes which responded with ACK for the advertisement out of the cluster nodes number               | /-                                    |
+---------------------------+-----------------------------------------------------------------------------------------------------------+---------------------------------------+
| Advertisement Status      | The status of the remote transaction on the remote node                                                   | Succeeded, Failed, Unknown, Received  |
+---------------------------+-----------------------------------------------------------------------------------------------------------+---------------------------------------+


**Example**
::

	dnRouter# show system nst advertisements details wbox.config

	Revision: 3
	Timestamp: 123123123
	Synched nodes: 4/4

	| Remote Node Type   | Remote Node ID   | Timestamp           | Advertisement status   |
	|--------------------+------------------+---------------------+------------------------|
	| NCP                | 1                | 26-03-2025 17:45:07 | Succeeded              |
	| NCP                | 2                | 26-03-2025 17:45:07 | Unavailable            |
	| NCP                | 3                | 26-03-2025 17:45:07 | Unavailable            |
	| NCP                | 4                | 26-03-2025 17:45:07 | Unavailable            |
    

**Command History**

+---------+-----------------------------------------------+
| Release | Modification                                  |
+=========+===============================================+
| 25.2    | Command introduced                            |
+---------+-----------------------------------------------+
