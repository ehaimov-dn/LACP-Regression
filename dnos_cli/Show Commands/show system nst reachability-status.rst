show system nst reachability-status
-----------------------------------

**Minimum user role:** viewer

Displays the nst reachability status and the connected nodes.


**Command syntax: show system nst reachability-status**

**Command mode:** operational


**Note**

- Supported only on NC-AI cluster formations.

- Reachability Status
	- Reachable - have fabric reachability, without NST heartbeats
	- Connected - have both fabric reachability and NST heartbeats
	- Unreachable - stale state after loosing fabric reachability and before being deleted
	- Disconnected - stale state after loosing NST heartbeats and before being deleted

- If the downtime exeeds it's max value, it will be displayed as "over ...".

- All the reachability data is displayed from the NCP connectivity perspective of the cluster.

**Parameter table**

+---------------------+----------------------------------------------------------------------------------------------------------+----------------------------------+
| Parameter           | Description                                                                                              | Range                            |
+=====================+==========================================================================================================+==================================+
| Node Type           | The type of the node used to filter the output to a specific NCE type. Currently only supported for NCP  | NCP, NCF                         |
+---------------------+----------------------------------------------------------------------------------------------------------+----------------------------------+
| Node ID             | The ID of the node used to filter the output to a specific cluster element                               | /-                               |
+---------------------+----------------------------------------------------------------------------------------------------------+----------------------------------+

The following information is displayed:

+---------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------+
| Parameter                 | Description                                                                                               | Range                             |
+===========================+===========================================================================================================+===================================+
| Node Type                 | The type of the remote node. Currently only supported for NCP                                             | NCP, NCF                          |
+---------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------+
| Node ID                   | The ID of the remote node                                                                                 | /-                                |
+---------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------+
| IP Address                | The IP address of the node within the ICE network                                                         | /-                                |
+---------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------+
| Reachability Status       | Reachability status of the remote node                                                                    | Reachable, Connected,             |
|                           |                                                                                                           | Unreachable, Disconnected         |
+---------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------+
| Downtime                  | Remote node's downtime if that node is not connected                                                      | /-                                |
+---------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------+

**Example**
::

	dnRouter# show system nst reachability-status

	NST Status for NCP 5:

	| Node Type | Node ID | IP Address | Reachability Status | Downtime |
	|-----------+---------+------------+---------------------+----------|
	| NCP       | 0       | 1.2.3.1    | Connected           | -        |
	| NCP       | 1       | 1.2.3.2    | Connected           | -        |
	| NCP       | 2       | 1.2.3.3    | Connected           | -        |
	| NCP       | 3       | 1.2.3.4    | Reachable           | 00:00:23 |
	| NCP       | 4       | 1.2.3.5    | Connected           | -        |
	| NCP       | 6       | 1.2.3.7    | Disconnected        | 00:00:23 |


	dnRouter# show system nst reachability-status
	Error: Command not supported by current system.

**Command History**

+---------+-----------------------------------------------+
| Release | Modification                                  |
+=========+===============================================+
| 25.2    | Command introduced                            |
+---------+-----------------------------------------------+

