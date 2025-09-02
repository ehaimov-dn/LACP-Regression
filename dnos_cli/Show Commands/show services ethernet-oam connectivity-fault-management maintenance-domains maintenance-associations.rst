show services ethernet-oam connectivity-fault-management maintenance-domains maintenance-associations
-----------------------------------------------------------------------------------------------------

**Minimum user role:** viewer

To display information for Connectivity Fault Management Maintenance Associations:


**Command syntax: show services ethernet-oam connectivity-fault-management maintenance-domains [md-name] maintenance-associations** {[ma-name] | all}

**Command mode:** operational

..
	**Internal Note**

	-

**Example**
::

	dnRouter# show services ethernet-oam connectivity-fault-management maintenanace-domains MD1 maintenance-associations

	Connectivity Fault Management Ethernet OAM Maintenance Associations:

	Maintenance Domain: MD1, MD-name: MyMD, Type: string, Level: 7

	Maintenance Associations:
	+-------------------------+------------------------------+-----------+------------+------------+-------------+---------------------+--------------+
	| Maintenance Association | Maintenance Association name | Type      | Local MEPs | Local MIPs | Remote MEPs | Missing Remote MEPs | Active Alarm |
	+=========================+==============================+===========+============+============+=============+=====================+==============+
	| MA1                     | MyMA1                        | string    | 3          | 1          | 4           | 2                   | def-xcon-ccm |
	| MA2                     | 127                          | VLAN-ID   | 1          | 0          | 1           | 0                   | none         |
	| MA3                     | MA3                          | string    | 1          | 0          | 1           | N/A                 | none         |
	+-------------------------+------------------------------+-----------+------------+------------+-------------+---------------------+--------------+

	Total Maintenance Associations: 3
	Total Local MEPs              : 5
	Total Local MIPs              : 1
	Total Remote MEPs             : 6
	Total Missing Remote MEPs     : 2


	dnRouter# show services ethernet-oam connectivity-fault-management maintenanace-domains MD1 maintenance-associations MA1

	Connectivity Fault Management Ethernet OAM Maintenance Associations:

	Maintenance Domain: MD1, MD-name: MyMD, Type: string, Level: 7

	Maintenance Association MA1
	  MA-name: MyMA1, Type: string
	  CCM TX state: enabled, CCM interval: 1 second, CCM loss-threshold: 3 frames, auto-discovery: disabled
	  Fault Alarms:
	    Lowest priority defect threshold: mac-remote-error-xcon, alarm-timer: 2500 milliseconds, reset-timer: 10000 milliseconds
		Active Alarm: def-xcon-ccm

	  Defects: X - DefXconCCM, E - DefErrorCCM, L - DefRemoteCCM, M - DefMACstatus, R - DefRDICCM

	  Local MEPs:
	    +--------+-----------------+-------------------+-----------+-------------+--------------+---------+
	    | MEP-ID | Interface       | MAC Address       | Direction | Admin State | CCM TX State | Defects | 
	    +========+=================+===================+===========+=============+==============+=========+
	    | 2      | ge100-0/0/0.200 | 7c:fe:90:57:73:10 | down      | enabled     | enabled      |         |
	    | 3      | ge100-0/0/0.300 | 7c:fe:90:57:73:10 | down      | enabled     | enabled      | XR      |
	    | 6      | ge100-0/0/0.600 | 7c:fe:90:57:73:10 | up        | disabled    | enabled      | MR      |
	    +--------+-----------------+-------------------+-----------+-------------+--------------+---------+
	  Remote MEPs:
	    +--------+-------------------+--------------+---------+------------------+-------------+------------------+
	    | MEP-ID | MAC Address       | CCM RX State | RDI bit | Interface Status | Port Status | Uptime/Downtime  |
	    +========+===================+==============+=========+==================+=============+==================+
	    | 1      | 7c:fe:90:57:73:11 | rmep-ok      | false   | up               | N/A         | 0 days, 00:01:30 |
	    | 7      | 7c:fe:90:57:73:12 | rmep-start   | false   | up               | N/A         |                  |
	    | 8      | 7c:fe:90:57:73:13 | rmep-ok      | true    | N/A              | N/A         | 0 days, 00:01:30 |
	    | 9      | 7c:fe:90:57:73:14 | rmep-failed  |         | N/A              | N/A         | 0 days, 00:01:30 |
	    +--------+-------------------+--------------+---------+------------------+-------------+------------------+
	  Missing Remote MEPs:
	    4, 5
	  Local MIPs:
	    +--------+-----------------+-------------------+-------------+
	    | MIP    | Interface       | MAC Address       | Admin State |
	    +========+=================+===================+=============+
	    | MyMIP1 | ge100-0/0/0.400 | 7c:fe:90:57:73:10 | disabled    |
	    +--------+-----------------+-------------------+-------------+

	  Total Local MEPs         : 3
	  Total Local MIPs         : 1
	  Total Remote MEPs        : 4
	  Total Missing Remote MEPs: 2



	dnRouter# show services ethernet-oam connectivity-fault-management maintenanace-domains MD1 maintenance-associations all

	Connectivity Fault Management Ethernet OAM Maintenance Associations:

	Maintenance Domain: MD1, MD-name: MyMD, Type: string, Level: 7

	Maintenance Association MA1
	  MA-name: MyMA1, Type: string
	  CCM TX state: enabled, CCM interval: 1 second, CCM loss-threshold: 3 frames, auto-discovery: enabled
	  Fault Alarms:
	    Lowest priority defect threshold: mac-remote-error-xcon, alarm-timer: 2500 milliseconds, reset-timer: 10000 milliseconds
		Active Alarm: def-xcon-ccm

	  Defects: X - DefXconCCM, E - DefErrorCCM, L - DefRemoteCCM, M - DefMACstatus, R - DefRDICCM

	  Local MEPs:
	    +--------+-----------------+-------------------+-----------+-------------+--------------+---------+
	    | MEP-ID | Interface       | MAC Address       | Direction | Admin State | CCM TX State | Defects |
	    +========+=================+===================+===========+=============+==============+=========+
	    | 2      | ge100-0/0/0.200 | 7c:fe:90:57:73:10 | down      | enabled     | enabled      |         |
	    | 3      | ge100-0/0/0.300 | 7c:fe:90:57:73:10 | down      | enabled     | enabled      | XR      |
	    | 6      | ge100-0/0/0.600 | 7c:fe:90:57:73:10 | up        | disabled    | enabled      | MR      |
	    +--------+-----------------+-------------------+-----------+-------------+--------------+---------+
	  Remote MEPs:
	    +--------+-------------------+--------------+---------+------------------+-------------+------------------+
	    | MEP-ID | MAC Address       | CCM RX State | RDI bit | Interface Status | Port Status | Uptime/Downtime  |
	    +========+===================+==============+=========+==================+=============+==================+
	    | 1      | 7c:fe:90:57:73:11 | rmep-ok      | false   | up               | N/A         | 0 days, 00:01:30 |
	    | 7      | 7c:fe:90:57:73:12 | rmep-start   | false   | up               | N/A         |                  |
	    | 8      | 7c:fe:90:57:73:13 | rmep-ok      | true    | N/A              | N/A         | 0 days, 00:01:30 |
	    | 9      | 7c:fe:90:57:73:14 | rmep-failed  |         | N/A              | N/A         | 0 days, 00:01:30 |
	    +--------+-------------------+--------------+---------+------------------+-------------+------------------+
	  Missing Remote MEPs:
	    4, 5
	  Local MIPs:
	    +--------+-----------------+-------------------+-------------+
	    | MIP    | Interface       | MAC Address       | Admin State |
	    +========+=================+===================+=============+
	    | MyMIP1 | ge100-0/0/0.400 | 7c:fe:90:57:73:10 | disabled    |
	    +--------+-----------------+-------------------+-------------+

	  Total Local MEPs         : 3
	  Total Local MIPs         : 1
	  Total Remote MEPs        : 4
      Total Missing Remote MEPs: 2

	Maintenance Association MA2
	  MA-ID: 127, Type: VLAN-ID
	  CCM TX state: enabled, CCM interval: 1 second, CCM loss-threshold: 3 frames, auto-discovery: disabled
	  Fault Alarms: 
	    Lowest priority defect threshold: mac-remote-error-xcon, alarm-timer: 2500 milliseconds, reset-timer: 10000 milliseconds
	    Active Alarm: none

	  Defects: X - DefXconCCM, E - DefErrorCCM, L - DefRemoteCCM, M - DefMACstatus, R - DefRDICCM

	  Local MEPs:
	    +--------+-----------------+-------------------+-----------+-------------+--------------+---------+
	    | MEP-ID | Interface       | MAC Address       | Direction | Admin State | CCM TX State | Defects |
	    +========+=================+===================+===========+=============+==============+=========+
	    | 1      | ge100-0/0/0.100 | 7c:fe:90:57:73:10 | down      | enabled     | enabled      |         |
	    +--------+-----------------+-------------------+-----------+-------------+--------------+---------+
	  Remote MEP IDs:
	    +--------+-------------------+--------------+---------+------------------+-------------+------------------+
	    | MEP-ID | MAC Address       | CCM RX State | RDI bit | Interface Status | Port Status | Uptime/Downtime  |
	    +========+===================+==============+=========+==================+=============+==================+
	    | 2      | 7c:fe:90:57:73:12 | rmep-start   | false   | up               | N/A         |                  |
	    +--------+-------------------+--------------+---------+------------------+-------------+------------------+
	  Missing Remote MEPs:
	    N/A
	  Local MIPs:
	    N/A

	  Total Local MEPs : 1
	  Total Local MIPs : 0
	  Total Remote MEPs: 1
      Total Missing Remote MEPs: 0


.. **Help line:** Display CFM Maintenance Associations

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.1    | Command introduced |
+---------+--------------------+
