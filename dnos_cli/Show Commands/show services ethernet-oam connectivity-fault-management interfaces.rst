show services ethernet-oam connectivity-fault-management interfaces
-------------------------------------------------------------------

**Minimum user role:** viewer

To display information for Connectivity Fault Management interfaces:


**Command syntax: show services ethernet-oam connectivity-fault-management interfaces** {[interface-name]}

**Command mode:** operational

..
	**Internal Note**
	
	-  

**Example**
::

	dnRouter# show services ethernet-oam connectivity-fault-management interfaces

	Connectivity Fault Management Ethernet OAM interfaces summary:

	Defects: X - DefXconCCM, E - DefErrorCCM, L - DefRemoteCCM, M - DefMACstatus, R - DefRDICCM

	Local MEPs:
	  +---------------+----------+--------------+---------------------+-----------+-------------------+-----------+-------------+--------------+-----------+
	  | Interface     | MD level | MD name      | MA name             | MEP-ID    | MAC Address       | Direction | Admin State | CCM TX State | Defects   |
	  +===============+==========+==============+=====================+===========+===================+===========+=============+==============+===========+
	  | bundle-1.2001 | 0        | MD0_LEVEL0   | BD_CFM2001_PE-to-CE | 1         | 7c:fe:90:57:73:10 | down      | enabled     | enabled      | R         |
	  |               | 4        | MD4_LEVEL4   | BD_CFM2001_PE-to-PE | 38        | 7c:fe:90:57:73:13 | up        | enabled     | enabled      | L         |
	  +---------------+----------+--------------+---------------------+-----------+-------------------+-----------+-------------+--------------+-----------+
	
	Local MIPs:
	  +---------------+----------+--------------+---------------------+-----------+-------------+-------------------+
	  | Interface     | MD level | MD name      | MA name             | MIP name  | Admin State |  MAC Address      |
	  +===============+==========+==============+=====================+===========+===========+=====================+
	  | bundle-1.2001 | 0        | MD0_LEVEL0   | BD_CFM2001_PE-to-CE | My_MIP1   | enabled     | 7c:fe:90:57:73:10 |
	  |               | 4        | MD4_LEVEL4   | BD_CFM2001_PE-to-PE | My_MIP2   | enabled     | 7c:fe:90:57:73:13 |
	  +---------------+----------+--------------+---------------------+-----------+-------------+-------------------+


	dnRouter# show services ethernet-oam connectivity-fault-management interfaces bundle-1.2001

	Connectivity Fault Management Ethernet OAM interface bundle-1.2001:

	Maintenance Domain: MD0_LEVEL0, MD-name: MD0_LEVEL0, Type: string, Level: 0
	Maintenance Association: BD_CFM2001_PE-to-CE, MA-name: BD_CFM2001_PE-to-CE, Type: string

	Defects: X - DefXconCCM, E - DefErrorCCM, L - DefRemoteCCM, M - DefMACstatus, R - DefRDICCM

	Local MEPs:
	  +--------+-----------------+-------------------+-----------+-------------+--------------+---------+
	  | MEP-ID | Interface       | MAC Address       | Direction | Admin State | CCM TX State | Defects | 
	  +========+=================+===================+===========+=============+==============+=========+
	  | 1      | bundle-1.2001   | 7c:fe:90:57:73:10 | down      | enabled     | enabled      |         |
	  +--------+-----------------+-------------------+-----------+-------------+--------------+---------+
	Local MIPs:
	  +--------+-----------------+-------------------+-------------+
	  | MIP    | Interface       | MAC Address       | Admin State |
	  +========+=================+===================+=============+
	  | MyMIP1 | bundle-1.2001   | 7c:fe:90:57:73:10 | disabled    |
	  +--------+-----------------+-------------------+-------------+

	Total Local MEPs : 1
	Total Local MIPs : 1

	Maintenance Domain: MD4_LEVEL4, MD-name: MD4_LEVEL4, Type: string, Level: 4
	Maintenance Association: BD_CFM2001_PE-to-PE, MA-name: BD_CFM2001_PE-to-PE, Type: string

	Defects: X - DefXconCCM, E - DefErrorCCM, L - DefRemoteCCM, M - DefMACstatus, R - DefRDICCM

	Local MEPs:
	  +--------+---------------+-------------------+-----------+-------------+--------------+-------------+
	  | MEP-ID | Interface     | MAC Address       | Direction | Admin State | CCM TX State | Defects     |
	  +========+===============+===================+===========+=============+==============+=============+
	  | 38     | bundle-1.2001 | 7c:fe:90:57:73:b8 | up        | enabled     | enabled      | L           |
	  +--------+---------------+-------------------+-----------+-------------+--------------+-------------+
	Local MIPs:
	  N/A

	Total Local MEPs : 1
	Total Local MIPs : 0


.. **Help line:** Display CFM information per interface

**Command History**

+---------+---------------------------+
| Release | Modification              |
+=========+===========================+
| 19.2    | Command introduced        |
+---------+---------------------------+