show bgp summary
----------------

**Minimum user role:** viewer

The following command displays a summary of the BGP neighbor status.

**Command syntax: show bgp** {instance vrf [vrf-name]} [address-family] [sub-address-family] **summary**

**Command mode:** operational


..
	**Internal Note**

	- AdjOut - number of prefixes in the adjacency-out table that speaker advertise to neighbor

	- PfxAccepted - number of prefixes in the adjacency-in table post in policy processing

	- use vrf to display information for a non-default vrf

	- for non-default instance vrf support only "unicast" sub-address-family

	- address-family sub-address-family are optional, if not specified display for all sub-address-families

	- for "link-state" address-family there's no [sub-address-family]

**Parameter table**

+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
| Parameter          | Description                                                                                                                                             | Range                    |
+====================+=========================================================================================================================================================+==========================+
| vrf-name           | Display routing information for a non-default VRF                                                                                                       | 1..255 characters        |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
| address-family     | Display routing information for a specific address-family (AFI)                                                                                         | IPv4                     |
|                    |                                                                                                                                                         | IPv6                     |
|                    |                                                                                                                                                         | Link-state               |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
| sub-address-family | Display routing information for a specific subsequent address-family (safi). Only unicast is supported with a non-default VRF.                          | unicast                  |
|                    | N/A for link-state address-family                                                                                                                       | multicast                |
|                    |                                                                                                                                                         | vpn                      |
|                    |                                                                                                                                                         | flowspec                 |
|                    |                                                                                                                                                         | rt-constrains            | 
|                    |                                                                                                                                                         | l2vpn evpn               |
|                    |                                                                                                                                                         | labeled-unicast          |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+

**Example**
::

	dnRouter# show bgp summary

	IPv4 Unicast
	---------------------
	BGP router identifier 20.20.20.20, local AS number 100
	BGP table node count 1367995
	Table route limit: 759999
	Table route count: 683998
	Routes over limit: 0

	Neighbor        V         AS MsgRcvd    MsgSent    InQ  OutQ  AdjOut  Up/Down   State/PfxAccepted
	10.10.10.10     4        100          0          0    0     0       0 never     Idle (Admin)
	12.12.12.12     4        100          0          0    0     0       0 never     Idle (Admin)
	30.30.30.30     4        100          0          0    0     0       0 never     Idle (Admin)
	33.20.101.2     4        102          0          0    0     0       0 never     Idle (Admin)
	80.80.80.80     4        100          0          0    0     0       0 never     Idle (Admin)
	10:10:10::10    4        100      19789        353    0     0       0 03:05:34             683998
	33:20:101::2    4        102        196      10190    0     0       0 00:45:17  Idle (Admin)

	Total number of established neighbors with IPv4 Unicast 1/7

	Total number of NSR capable BGP sessions 0

	IPv4 Multicast
	-----------------------
	BGP router identifier 20.20.20.20, local AS number 100
	BGP table node count 0

	Neighbor        V         AS MsgRcvd    MsgSent    InQ  OutQ  AdjOut  Up/Down   State/PfxAccepted
	30.30.30.30     4        100          0          0    0     0       0 never     Idle (Admin)
	33.20.101.2     4        102          0          0    0     0       0 never     Idle (Admin)
	80.80.80.80     4        100          0          0    0     0       0 never     Idle (Admin)

	Total number of established neighbors with IPv4 Multicast 0/3

	Total number of NSR capable BGP sessions 0

	IPv4 Vpn
	-------------------------
	BGP router identifier 20.20.20.20, local AS number 100
	BGP table node count 0

	Neighbor        V         AS MsgRcvd    MsgSent    InQ  OutQ  AdjOut  Up/Down   State/PfxAccepted
	10.10.10.10     4        100          0          0    0     0       0 never     Idle (Admin)
	80.80.80.80     4        100          0          0    0     0       0 never     Idle (Admin)

	Total number of established neighbors with IPv4 Vpn 0/2

	Total number of NSR capable BGP sessions 0

	IPv6 Unicast
	---------------------
	BGP router identifier 20.20.20.20, local AS number 100
	BGP table node count 0
	Table route limit: 190000
	Table route count: 0
	Routes over limit: 0

	Neighbor        V         AS MsgRcvd    MsgSent    InQ  OutQ  AdjOut  Up/Down   State/PfxAccepted
	10:10:10::10    4        100      19789        353    0     0       0 03:05:34                  0
	33:20:101::2    4        102        196      10190    0     0       0 00:45:17  Idle (Admin)

	Total number of established neighbors with IPv6 Unicast 1/2

	Total number of NSR capable BGP sessions 0

	Total number of established neighbors 1/7



    dnRouter# show bgp ipv4 flowspec summary

	BGP router identifier 9.9.9.3, local AS number 2
	RIB entries 1
	Peers 1

	  Neighbor        V         AS MsgRcvd MsgSent TblVer InQ  OutQ  AdjOut  Up/Down   State/PfxAccepted
	  192.168.1.2     4          1      16      17      0    0     0       0 00:01:34                  1

	Total number of neighbors 1

	Total number of NSR capable BGP sessions 0

	dnRouter# show bgp instance vrf A summary


	dnRouter# show bgp ipv4 unicast summary

	IPv4 Unicast
	---------------------
	BGP router identifier 20.20.20.20, local AS number 100
	BGP table node count 1367995
	Table route limit: 759999
	Table route count: 683998
	Routes over limit: 0

	Neighbor        V         AS MsgRcvd    MsgSent    InQ  OutQ  AdjOut  Up/Down   State/PfxAccepted
	10.10.10.10     4        100          0          0    0     0       0 never     Idle (Admin)
	12.12.12.12     4        100          0          0    0     0       0 never     Idle (Admin)
	30.30.30.30     4        100          0          0    0     0       0 never     Idle (Admin)
	33.20.101.2     4        102          0          0    0     0       0 never     Idle (Admin)
	80.80.80.80     4        100          0          0    0     0       0 never     Idle (Admin)
	10:10:10::10    4        100      19789        353    0     0       0 03:05:34             683998
	33:20:101::2    4        102        196      10190    0     0       0 00:45:17  Idle (Admin)

	Total number of established neighbors with IPv4 Unicast 1/7

	Total number of NSR capable BGP sessions 0

	**BGP with enabled confederation**

	dnRouter# show bgp summary

	IPv4 Unicast
	---------------------
	BGP router identifier 9.9.9.9, local AS number 65000, confederation identifier 1
	RIB entries 1, using 112 bytes of memory
	Peers 3, using 133 KiB of memory
	...

    dnRouter# show bgp ipv4 flowspec summary

	BGP router identifier 9.9.9.3, local AS number 2
	RIB entries 1
	Peers 1


	  Neighbor        V         AS MsgRcvd MsgSent TblVer InQ  OutQ  AdjOut  Up/Down   State/PfxAccepted
	  11.11.11.1      4        100       4       7      0    0     0       1 00:02:13                  0
	  2.2.2.2         4      65000       4       7      0    0     0       1 00:02:07                  0
	  3.3.3.3         4      65001       4       7      0    0     0       1 00:02:16                  0

	Total number of established neighbors with IPv4 Unicast 3/6

	Total number of NSR capable BGP sessions 0


    dnRouter# show bgp ipv4 multicast summary

	BGP router identifier 9.9.9.3, local AS number 2
	RIB entries 1
	Peers 1

	  Neighbor        V         AS MsgRcvd MsgSent TblVer InQ  OutQ  AdjOut  Up/Down   State/PfxAccepted
	  205.0.0.1       4        100      69      69      3   0     0       0 00:14:19                   1

	Total number of neighbors 1

	Total number of NSR capable BGP sessions 0




    dnRouter# show bgp l2vpn evpn summary

	BGP router identifier 101.3.3.3, local AS number 65000
	BGP table node count 87

  	Neighbor        V         AS MsgRcvd MsgSent InQ  OutQ  AdjOut  Up/Down   State/PfxAccepted
  	101.1.1.1       4      65000    1143    1226    0     0      47 18:21:06                  9
  	101.2.2.2       4      65000       0       0    0     0       0 never     Connect
  	101.6.6.6       4      65000       0       0    0     0       0 never     Active
  	101.7.7.7       4      65000    1108    1333    0     0      54 03:12:27                  2
  	101.8.8.8       4      65000    1124    1269    0     0      54 03:12:26                  2
  	101.10.10.10    4      65000       0       0    0     0       0 never     Connect
  	101.11.11.11    4      65000       0       0    0     0       0 never     Connect
  	101.12.12.12    4      65000       0       0    0     0       0 never     Connect
  

Total number of established neighbors with L2vpn EVPN 3/8

Total number of NSR capable BGP sessions 0


.. **Help line:**

**Command History**

+---------+---------------------------------------------------------------------------+
| Release | Modification                                                              |
+=========+===========================================================================+
| 6.0     | Command introduced                                                        |
+---------+---------------------------------------------------------------------------+
| 10.0    | Added link-state address-family                                           |
+---------+---------------------------------------------------------------------------+
| 11.6    | Added BGP confederation show command output                               |
+---------+---------------------------------------------------------------------------+
| 13.0    | Added support for flowspec in the sub-address family                      |
+---------+---------------------------------------------------------------------------+
| 15.0    | Added support for displaying BGP IPv6 Labeled-Unicast peers in the output |
+---------+---------------------------------------------------------------------------+
| 16.0    | Added support for IPv4 Route Target Constrain SAFI                        |
+---------+---------------------------------------------------------------------------+
| 16.1    | Added support for IPv4 Multicast SAFI                                     |
+---------+---------------------------------------------------------------------------+
