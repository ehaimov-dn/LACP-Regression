show rib-manager nexthop-tracking
---------------------------------

**Minimum user role:** viewer

To display registered nexthop address in RIB for nexthop-tracking and their status:



**Command syntax: show rib-manager {ipv4 | ipv6} nexthop-tracking** {address [address] \| reachable \| unreachable \| vrf [vrf] \| color \| min-length} 

**Command mode:** operational


**Parameter table**

+---------------------+---------------------------------------------------------------------------------------+------------+
| Parameter           | Description                                                                           | Range      |
+=====================+=======================================================================================+============+
| address             | Filters the display for nexthop matching provided address                             | A.B.C.D    |
|                     | Address type (ipv4 / ipv6) must match the nexthop type (ipv4 / ipv6)                  | x:x::x:x   |
+---------------------+---------------------------------------------------------------------------------------+------------+
| reachable           | Displays only nexthop that are reachable and have a valid resolution                  | -          |
+---------------------+---------------------------------------------------------------------------------------+------------+
| unreachable         | Displays only nexthop that are unreachable or that doesn't have a valid resolution    | -          |
+---------------------+---------------------------------------------------------------------------------------+------------+
| vrf                 | Filter the displayed information to the specified VRF                                 | String     |
|                     | If not specified, nexthops for the default VRF are displayed                          |            |
+---------------------+---------------------------------------------------------------------------------------+------------+
| color               | Displays color information                                                            | -          |
+---------------------+---------------------------------------------------------------------------------------+------------+
| min-length          | Filter by min-length requested                                                        | -          |
+---------------------+---------------------------------------------------------------------------------------+------------+



.. **Note**

	- Nexthop resolution that violate minimum-length requirement will be considered as unreachable nexthops


**Example**
::

	dnRouter# show rib-manager ipv4 nexthop-tracking
	10.10.10.2/32
	 (Normal)
	 resolved via 10.0.0.0/8 (connected), metric: 0
	 is directly connected, ge100-0/0/1
	 Last update: 27-Sep-2024 11:24:40 UTC
	 Client list: bgp(bgp, register time: 27-Sep-2024 11:22:56 UTC)

	
	2.2.2.2/32 colors: 100
	 (Normal)
	 resolved via 2.2.2.2/32 <c> 100 (isis-sr), metric: 10
	 192.168.0.2, label 3, via ge100-0/0/39
	 Last update: 08-Oct-2024 06:25:01 UTC
	 Client list: bgp(bgp, register time: 07-Oct-2024 11:57:44 UTC)

	 1.7.0.2/32
	 (Normal)
	 min-length
	 unresolved: min-length 32 violation
	 Last update: 02-Oct-2024 13:58:56 UTC+3:00
	 STATIC reference count: 1
	 Client list: static(local, static, register time: 02-Oct-2024 13:32:18 UTC+3:00)3.


.. **Help line:** show RIB-Manager nexthop-tracking

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.2.2  | Command introduced |
+---------+--------------------+

