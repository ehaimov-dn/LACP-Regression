show system nst advertisements
------------------------------

**Minimum user role:** viewer

Displays advertisements list received from remote ncp.


**Command syntax: show system nst remote-advertisements [ncp-id]**

**Command mode:** operational



**Note**

- Supported only on NC-AI cluster formations.

- Remote Advertisements Status
    - Succeeded - advertisement was successfully applied on current node and success status was sent back to the origin node.
    - Failed - failed to apply the advertisement on current node and failure status was sent back to the origin node.
    - Unknown - current node didn't respond with any status to the origin node.
    - Received - advertisement was received by current node and is pending to be processed. Received status was sent back to the origin node.

**Parameter table**

+-------------+----------------------------------------------------------+
| ncp-id      | Displays information from a specific NCP.                |
+-------------+----------------------------------------------------------+


The following information is displayed:

+-------------------------------+-----------------------------------------------------------------------------------------------------------+--------------------------------------+
| Parameter                     | Description                                                                                               | Range                                |
+===============================+===========================================================================================================+======================================+
| Advertisement Name            | The key name represents the advertisement received from remote NCP                                        | /-                                   |
+-------------------------------+-----------------------------------------------------------------------------------------------------------+--------------------------------------+
| Revision                      | The advertisement revision received from the remote node                                                  | /-                                   |
+-------------------------------+-----------------------------------------------------------------------------------------------------------+--------------------------------------+
| Timestamp                     | Timestamp when the advertisement was received by current node                                             | /-                                   |
+-------------------------------+-----------------------------------------------------------------------------------------------------------+--------------------------------------+
| Remote Advertisement Status   | The status sent back to the advertisement originator                                                      | Succeeded, Failed, Received, Unknown |
+-------------------------------+-----------------------------------------------------------------------------------------------------------+--------------------------------------+


**Example**
::

	dnRouter# show system nst remote-advertisements ncp-0

	| Advertisement Name    | Revision | Timestamp | Remote Advertisement Status  |
	|-----------------------+----------+-----------+------------------------------+
	| wbox.oper.ge100-0/0/0 | 3        | 123123123 | Succeeded                    |
	| wbox.oper.ge100-0/0/1 | 3        | 123123123 | Received                     |
	| wbox.oper.ge100-0/0/2 | 3        | 123123123 | Succeeded                    |
	| wbox.config           | 3        | 123123123 | Failure (Out of resources)   |

	dnRouter# show system nst advertisements
    Error: Command not supported by current system.

**Command History**

+---------+-----------------------------------------------+
| Release | Modification                                  |
+=========+===============================================+
| 25.2    | Command introduced                            |
+---------+-----------------------------------------------+
