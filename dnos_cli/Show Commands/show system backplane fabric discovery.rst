show system backplane fabric discovery
--------------------------------------

**Minimum user role:** viewer

To display the system backplane fabric discovery status:



**Command syntax: show system backplane fabric discovery** 

**Command mode:** operational



**Note**

- The fabric-discovery status displays both the connected fabric links and the reachability towards the expected neighbor NCEs according to pre defined system-type.

- The command is available only on AI distributed clusters.


**Parameter table**

For each fabric interface and NCE, the following information is displayed:

+--------------------------------+--------------------------------------------------------------------------------------------------------------+
| Field                          | Description                                                                                                  |
+================================+==============================================================================================================+
| System Type                    | AI-2016-800G-2                                                                                               |
|                                |                                                                                                              |
+--------------------------------+--------------------------------------------------------------------------------------------------------------+
| Fabric connectivity state      | For each NCP/F, displays which fabric port is connected to which NCF/P port                                  |
+--------------------------------+--------------------------------------------------------------------------------------------------------------+


**Example**
::

	dnRouter# show system backplane fabric discovery

	System Type: AI-2016-800G-2

	Fabric Connectivity State:

	NCP-4:
    +----------------------+---------------------------------+----------------+--------------------+------------------------+--------------------------------+
	| Interface Name       | Interface Description           | Neighbor Node  | Neighbor Node Name | Neighbor Interface     | Neighbor Interface Description |
	|======================+=================================+================+====================+========================+================================+
	| fab-ncp800-4/0/0     | FirstFabricNCP4                 | NCF-0          | dnRouter0          | fab-ncf800-0/0/0       | FirstFabricNCF0                |
	| fab-ncp800-4/0/1     |                                 |                |                    |                        |                                |
	| fab-ncp800-4/0/2     | SecondFabricNCP4                | NCF-2          | dnRouter2          | fab-ncf800-21/0/0      | FirstFabricNCF21               |
	| fab-ncp800-4/0/3     | ThirdFabricNCP4                 | NCF-3          | dnRouter3          | fab-ncf800-30/0/10     | FirstFabricNCF30               |
    +----------------------+---------------------------------+----------------+--------------------+------------------------+--------------------------------+

	dnRouter# show system backplane fabric discovery

	System Type: AI-2016-800G-2

	Fabric Connectivity State:

	NCF-2:

    +----------------------+---------------------------------+----------------+--------------------+------------------------+--------------------------------+
	| Interface Name       | Interface Description           | Neighbor Node  | Neighbor Node Name | Neighbor Interface     | Neighbor Interface Description |
    |======================+=================================+================+====================+========================+================================+
	| fab-ncf800-2/0/0     | FirstFabricNCF2                 | NCP-0          | dnRouter0          | fab-ncp800-0/0/0       | FirstFabricNCP0                |
	| fab-ncf800-2/0/1     |                                 |                |                    |                        |                                |
	| fab-ncf800-2/0/2     | SecondFabricNCF2                | NCP-2          | dnRouter2          | fab-ncp800-21/0/0      | FirstFabricNCP21               |
	| fab-ncf800-2/0/3     | ThirdFabricNCF2                 | NCP-3          | dnRouter3          | fab-ncp800-30/0/10     | FirstFabricNCP30               |
	+----------------------+---------------------------------+----------------+--------------------+------------------------+--------------------------------+

	**Command History**

+---------+---------------------------------------------------+
| Release | Modification                                      |
+=========+===================================================+
| 25.1    | Command introduced                                |
+---------+---------------------------------------------------+