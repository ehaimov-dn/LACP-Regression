show system hardware cpu
------------------------

**Minimum user role:** viewer

Displays detailed information on the system's CPU resources, per node or all nodes in a cluster.

Detailed information includes per-core scaling governor policy, current clock frequency, and maximum supported clock frequency.



**Command syntax: show system hardware cpu** [node-name] [node-id]

**Command mode:** operational



**Parameter table**

+-----------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| Parameter | Description                                                                                                                                | Range               |
+===========+============================================================================================================================================+=====================+
| node-name | The name of the node used to filter the output to a specific cluster element. If no name is provided, all cluster nodes will be displayed. | NCP, NCF, NCC, NCM  |
+-----------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| node-id   | The ID of the node used to filter the output to a specific cluster element.                                                                | NCP: 0..249         |
|           |                                                                                                                                            | NCC: 0..1           |
|           |                                                                                                                                            | NCF: 0..611         |
|           |                                                                                                                                            | NCM: A0-1, B0-1     |
+-----------+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------+



**Example**
::

	dnRouter# show system hardware cpu

	ncc 0 (dn-ncc-0)

	Hardware Information:

	  | Item          | Value                                      |
	  |---------------+--------------------------------------------|
	  | CPU Model     | Intel(R) Xeon(R) Silver 4216 CPU @ 2.10GHz |
	  | Hyper-Threads | 64 (2 per Core)                            |

	CPU Usage:

	  | CPU   | Use %   | Scaling Policy     | Current Frequency [MHz]   | Max Frequency [MHz]   |
	  |-------+---------+--------------------+---------------------------+-----------------------|
	  | 0     | 4       | performance        | 2903                      | 4000                  |
	  | 1     | 2       | performance        | 1733                      | 4000                  |
	  | 2     | 1       | performance        | 2900                      | 4000                  |
	  | 3     | 1       | performance        | 4000                      | 4000                  |
	  | 4     | 1       | performance        | 2903                      | 4000                  |
	  | 5     | 2       | performance        | 800                       | 4000                  |
	  | 6     | 1       | performance        | 2901                      | 4000                  |
	  | 7     | 2       | performance        | 4000                      | 4000                  |
	  | 8     | 2       | performance        | 2901                      | 4000                  |
	  | 9     | 0       | performance        | 4000                      | 4000                  |
	  | 10    | 2       | performance        | 2899                      | 4000                  |
	  | 11    | 2       | performance        | 2900                      | 4000                  |
	  | 12    | 1       | performance        | 4000                      | 4000                  |
	  | 13    | 1       | performance        | 4000                      | 4000                  |
	  | 14    | 2       | performance        | 4000                      | 4000                  |
	  | 15    | 2       | performance        | 2899                      | 4000                  |

	  Last 1 minute CPU load average: 80%
	  Last 5 minutes CPU load average: 70%

	ncp 0 (dn-ncp-0)

	Hardware Information:

	  | Item          | Value                                 |
	  |---------------+---------------------------------------|
	  | CPU Model     | Intel(R) Xeon(R) CPU D-1548 @ 2.00GHz |
	  | Hyper-Threads | 16 (2 per Core)                       |

	CPU Usage:
	  | CPU   | Use %   | Scaling Policy     | Current Frequency [MHz]   | Max Frequency [MHz]   |
	  |-------+---------+--------------------+---------------------------+-----------------------|
	  | 0     | 4       | performance        | 2903                      | 4000                  |
	  | 1     | 2       | performance        | 1733                      | 4000                  |
	  | 2     | 1       | performance        | 2900                      | 4000                  |
	  | 3     | 1       | performance        | 4000                      | 4000                  |
	  | 4     | 1       | performance        | 2903                      | 4000                  |
	  | 5     | 2       | performance        | 800                       | 4000                  |
	  | 6     | 1       | performance        | 2901                      | 4000                  |
	  | 7     | 2       | performance        | 4000                      | 4000                  |
	  | 8     | 2       | performance        | 2901                      | 4000                  |
	  | 9     | 0       | performance        | 4000                      | 4000                  |
	  | 10    | 2       | performance        | 2899                      | 4000                  |
	  | 11    | 2       | performance        | 2900                      | 4000                  |
	  | 12    | 1       | performance        | 4000                      | 4000                  |
	  | 13    | 1       | performance        | 4000                      | 4000                  |
	  | 14    | 2       | performance        | 4000                      | 4000                  |
	  | 15    | 2       | performance        | 2899                      | 4000                  |

	  Last 1 minute CPU load average: 80%
	  Last 5 minutes CPU load average: 70%
	
	ncf 0 (dn-ncf-0)

	Hardware Information:

	  | Item          | Value                                  |
	  |---------------+----------------------------------------|
	  | CPU Model     | Intel(R) Xeon(R) D-2712T CPU @ 1.90GHz |
	  | Hyper-Threads | 8 (2 per Core)                         |
	
	CPU Usage:
	  | CPU   | Use %   | Scaling Policy     | Current Frequency [MHz]   | Max Frequency [MHz]   |
	  |-------+---------+--------------------+---------------------------+-----------------------|
	  | 0     | 6       | performance        | 2328                      | 2600                  |
	  | 1     | 6       | performance        | 2330                      | 2600                  |
	  | 2     | 9       | performance        | 2303                      | 2600                  |
	  | 3     | 10      | performance        | 2323                      | 2600                  |
	  | 4     | 24      | performance        | 2600                      | 2600                  |
	  | 5     | 7       | performance        | 2316                      | 2600                  |
	  | 6     | 10      | performance        | 2301                      | 2600                  |
	  | 7     | 9       | performance        | 2321                      | 2600                  |

	  Last 1 minute CPU load average: 80%
	  Last 5 minutes CPU load average: 70%


	dnRouter# show system hardware cpu ncp 5

	ncp 5 (dn-ncp-5)

	Hardware Information:

	  | Item          | Value                                 |
	  |---------------+---------------------------------------|
	  | CPU Model     | Intel(R) Xeon(R) CPU D-1548 @ 2.00GHz |
	  | Hyper-Threads | 16 (2 per Core)                       |
	
	CPU Usage:
	  | CPU   | Use %   | Scaling Policy     | Current Frequency [MHz]   | Max Frequency [MHz]   |
	  |-------+---------+--------------------+---------------------------+-----------------------|
	  | 0     | 10      | performance        | 2334                      | 2600                  |
	  | 1     | 10      | performance        | 2325                      | 2600                  |
	  | 2     | 13      | performance        | 2338                      | 2600                  |
	  | 3     | 34      | performance        | 2340                      | 2600                  |
	  | 4     | 11      | performance        | 2323                      | 2600                  |
	  | 5     | 17      | performance        | 2394                      | 2600                  |
	  | 6     | 42      | performance        | 2347                      | 2600                  |
	  | 7     | 15      | performance        | 2353                      | 2600                  |
	  | 8     | 11      | performance        | 2332                      | 2600                  |
	  | 9     | 12      | performance        | 2314                      | 2600                  |
	  | 10    | 7       | performance        | 2320                      | 2600                  |
	  | 11    | 24      | performance        | 2313                      | 2600                  |
	  | 12    | 14      | performance        | 2300                      | 2600                  |
	  | 13    | 42      | performance        | 2327                      | 2600                  |
	  | 14    | 13      | performance        | 2325                      | 2600                  |
	  | 15    | 10      | performance        | 2348                      | 2600                  |

	  Last 1 minute CPU load average: 80%
	  Last 5 minutes CPU load average: 70%

	
	

.. **Help line:** show system hardware cpu information

**Command History**

+---------+-----------------------------------------------------+
| Release | Modification                                        |
+=========+=====================================================+
| 25.3    | Command introduced                                  |
+---------+-----------------------------------------------------+
