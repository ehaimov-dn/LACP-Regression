show services ethernet-oam connectivity-fault-management maintenance-domains maintenance-associations meps
----------------------------------------------------------------------------------------------------------

**Minimum user role:** viewer

To display information for Connectivity Fault Management Maintenance Endpoints:


**Command syntax: show services ethernet-oam connectivity-fault-management maintenance-domains [md-name] maintenance-associations [ma-name] meps** {[mep-id] | local | remote | all}

**Command mode:** operational

..
	**Internal Note**
	
	-  

**Example**
::

	dnRouter# show services ethernet-oam connectivity-fault-management maintenanace-domains MD1 maintenance-associations MA1 meps

	Connectivity Fault Management Ethernet OAM Maintenance Endpoints:

	Maintenance Domain: MD1, MD-name: MyMD, Type: string, Level: 7
	Maintenance Association: MA1, MA-name: MyMA1, Type: string

	Defects: X - DefXconCCM, E - DefErrorCCM, L - DefRemoteCCM, M - DefMACstatus, R - DefRDICCM

	Local MEPs:
	  +--------+-------------+-------------------+-----------+-------------+--------------+---------+
	  | MEP-ID | Interface   | MAC Address       | Direction | Admin State | CCM TX State | Defects |
	  +========+=============+===================+===========+=============+==============+=========+
	  | 2      | ge100-0/0/0 | 7c:fe:90:57:73:10 | down      | enabled     | enabled      | ER      |
	  +--------+-------------+-------------------+-----------+-------------+--------------+---------+
	Remote MEPs:
	  +--------+-------------------+--------------+---------+------------------+-------------+------------------+
	  | MEP-ID | MAC Address       | CCM RX State | RDI bit | Interface Status | Port Status | Uptime/Downtime  |
	  +========+===================+==============+=========+==================+=============+==================+
	  | 1      | 7c:fe:90:57:73:11 | rmep-ok      | false   | up               | N/A         | 0 days, 00:01:30 |
	  +--------+-------------------+--------------+---------+------------------+-------------+------------------+
	Missing Remote MEPs:
	  N/A

	Total Local MEPs         : 1
	Total Remote MEPs        : 1
	Total Missing Remote MEPs: 0


	dnRouter# show services ethernet-oam connectivity-fault-management maintenanace-domains MD1 maintenance-associations MA1 meps 2

	Connectivity Fault Management Ethernet OAM Maintenance Endpoints:

	Maintenance Domain: MD1, MD-name: MyMD, Type: string, Level: 7
	Maintenance Association: MA1, MA-name: MyMA1, Type: string

	Maintenance Endpoint 2
	  Interface: ge100-0/0/0, Direction: down, Admin-state: enabled
	  MAC address: 7c:fe:90:57:73:10
	  CCM TX state: enabled, CCM interval: 1 second, CCM loss-threshold: 3 frames, auto-discovery: disabled
	  Fault Alarms:
	    Lowest priority defect threshold: mac-remote-error-xcon, alarm-timer: 2500 milliseconds, reset-timer: 10000 milliseconds
	    Active Alarm: N/A
	  PCP: 7
	  Optional TLVs:
	    Interface Status: up
	    Port Status: psUp

	  RDI bit: false
	  Defects:
	    DefXconCCM       : no
	    DefErrorCCM      : no
	    DefRemoteCCM     : no
	    DefMACstatus     : no
	    DefRDICCM        : no

	  CFM Statistics:
	    CFM PDU Statistics:
	      +--------------+-------------+-------------+
	      | CFM PDUs     | Sent        | Received    |
	      +--------------+-------------+-------------+
	      | CCM          | 2345        | 4321        |
	      | LBM          | 10          | N/A         |
	      | LBR          | N/A         | 10          |
	      | LTM          | 0           | 0           |
	      | LTR          | 0           | 0           |
	      +--------------+-------------+-------------+
	    CFM Errors:
	      +----------------------------+-------------+
	      | CFM Errors                 | Received    |
	      +----------------------------+-------------+
	      | Unknown CFM PDUs           | 0           |
	      | Wrong MD Level             | 0           |
	      | CCM Wrong Interval         | 0           |
	      | CCM Wrong Remote-MEP       | 0           |
	      | CCM Wrong MAID             | 0           |
	      | Unicast MAC Mismatch       | 0           |
	      | RX Passive Side            | 0           |
	      +----------------------------+-------------+
	    Remote MEPs count: 1
		Missing Remote MEPs count: 0


	dnRouter# show services ethernet-oam connectivity-fault-management maintenanace-domains MD1 maintenance-associations MA1 meps 3

	Connectivity Fault Management Ethernet OAM Maintenance Endpoints:

	Maintenance Domain: MD1, MD-name: MyMD, Type: string, Level: 7
	Maintenance Association: MA1, MA-name: MyMA1, Type: string

	Remote Maintenance Endpoint 3
	  CCM RX State: rmep-ok, Uptime/Downtime: 0 days, 00:01:30
	  Type: configured
	  MAC address: 7c:fe:90:57:73:13
	  RDI bit: false
	  TLVs:
	    Interface Status: up
	    Port Status: N/A


	dnRouter# show services ethernet-oam connectivity-fault-management maintenanace-domains MD1 maintenance-associations MA1 meps all

	Connectivity Fault Management Ethernet OAM Maintenance Endpoints:

	Maintenance Domain: MD1, MD-name: MyMD, Type: string, Level: 7
	Maintenance Association: MA1, MA-name: MyMA1, Type: string

	Maintenance Endpoint 2
	  Interface: ge100-0/0/0, Direction: down, Admin-state: enabled
	  MAC address: 7c:fe:90:57:73:10
	  CCM TX state: enabled, CCM interval: 1 second, CCM loss-threshold: 3 frames, auto-discovery: disabled
	  Fault Alarms:
	    Lowest priority defect threshold: mac-remote-error-xcon, alarm-timer: 2500 milliseconds, reset-timer: 10000 milliseconds
	    Active Alarm: N/A
	  PCP: 7
	  Optional TLVs:
	    Interface Status: up
	    Port Status: psUp

	  RDI bit: true
	  Defects:
	    DefXconCCM       : no
	    DefErrorCCM      : no
	    DefRemoteCCM     : no
	    DefMACstatus     : no
	    DefRDICCM        : no

	  CFM Statistics:
	    CFM PDU Statistics:
	      +--------------+-------------+-------------+
	      | CFM PDUs     | Sent        | Received    |
	      +--------------+-------------+-------------+
	      | CCM          | 2345        | 4321        |
	      | LBM          | 0           | N/A         |
	      | LBR          | N/A         | 0           |
	      | LTM          | 0           | 0           |
	      | LTR          | 0           | 0           |
	      +--------------+-------------+-------------+
	    CFM Errors:
	      +----------------------------+-------------+
	      | CFM Errors                 | Received    |
	      +----------------------------+-------------+
	      | Unknown CFM PDUs           | 0           |
	      | Wrong MD Level             | 0           |
	      | CCM Wrong Interval         | 0           |
	      | CCM Wrong Remote-MEP       | 0           |
	      | CCM Wrong MAID             | 0           |
	      | Unicast MAC Mismatch       | 0           |
	      | RX Passive Side            | 0           |
	      +----------------------------+-------------+
	    Remote MEPs count: 1
		Missing Remote MEPs count: 0

	  Remote MEPs:
	    Maintenance Endpoint 3
	      CCM RX State: rmep-ok, Uptime/Downtime: 0 days, 00:01:30
	      Type: configured
	      MAC address: 7c:fe:90:57:73:13
	      RDI bit: false
	      Optional TLVs:
	        Interface Status: up
	        Port Status: N/A

	  Missing Remote MEPs:
	    N/A


	dnRouter# show services ethernet-oam connectivity-fault-management maintenanace-domains MD1 maintenance-associations MA1 meps local

	Connectivity Fault Management Ethernet OAM Maintenance Endpoints:

	Maintenance Domain: MD1, MD-name: MyMD, Type: string, Level: 7
	Maintenance Association: MA1, MA-name: MyMA1, Type: string

	Maintenance Endpoint 2
	  Interface: ge100-0/0/0, Direction: down, Admin-state: enabled
	  MAC address: 7c:fe:90:57:73:10
	  CCM TX state: enabled, CCM interval: 1 second, CCM loss-threshold: 3 frames, auto-discovery: disabled
	  Fault Alarms:
	    Lowest priority defect threshold: mac-remote-error-xcon, alarm-timer: 2500 milliseconds, reset-timer: 10000 milliseconds
	    Active Alarm: N/A
	  PCP: 7
	  Optional TLVs:
	    Interface Status: up
	    Port Status: psUp

	  RDI bit: false
	  Defects:
	    DefXconCCM       : no
	    DefErrorCCM      : no
	    DefRemoteCCM     : no
	    DefMACstatus     : no
	    DefRDICCM        : no

	  CFM Statistics:
	    CFM PDU Statistics:
	      +--------------+-------------+-------------+
	      | CFM PDUs     | Sent        | Received    |
	      +--------------+-------------+-------------+
	      | CCM          | 2345        | 4321        |
	      | LBM          | 0           | N/A         |
	      | LBR          | N/A         | 0           |
	      | LTM          | 0           | 0           |
	      | LTR          | 0           | 0           |
	      +--------------+-------------+-------------+
	    CFM Errors:
	      +----------------------------+-------------+
	      | CFM Errors                 | Received    |
	      +----------------------------+-------------+
	      | Unknown CFM PDUs           | 0           |
	      | Wrong MD Level             | 0           |
	      | CCM Wrong Interval         | 0           |
	      | CCM Wrong Remote-MEP       | 0           |
	      | CCM Wrong MAID             | 0           |
	      | Unicast MAC Mismatch       | 0           |
	      | RX Passive Side            | 0           |
	      +----------------------------+-------------+
	    Remote MEPs count: 1
		Missing Remote MEPs count: 0


.. **Help line:** Display CFM Maintenance Endpoints

**Command History**

+---------+---------------------------+
| Release | Modification              |
+=========+===========================+
| 19.1    | Command introduced        |
+---------+---------------------------+
| 19.2    | Added additional counters |
+---------+---------------------------+
