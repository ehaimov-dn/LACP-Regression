show access-lists counters
--------------------------

**Minimum user role:** viewer


To display access-list counters per rule for an access-list assigned to an interface:


**Command syntax: show access-lists counters** [interface-name]

**Command mode:** operational


..
	**Internal Note**

	- When a user selected a specific interface, it will display **all** access-list under it (IPv4 & IPv6). Counters will be displayed **per interface**


**Parameter table**

+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+
| Parameter      | Description                                                                                                                                                                                                                     | Range                                               | Default |
+================+=================================================================================================================================================================================================================================+=====================================================+=========+
| interface-name | The name of the interface to which the access-list is assigned. Counters for all IPv4 and IPv6 access-lists associated with the interface are displayed. The counters are displayed per access-list > per rule > per interface. | ge<interface speed>-<A>/<B>/<C>                     | \-      |
|                |                                                                                                                                                                                                                                 |                                                     |         |
|                |                                                                                                                                                                                                                                 | ge<interface speed>-<A>/<B>/<C>.<sub-interface id>  |         |
|                |                                                                                                                                                                                                                                 |                                                     |         |
|                |                                                                                                                                                                                                                                 | bundle-<bundle-id>                                  |         |
|                |                                                                                                                                                                                                                                 |                                                     |         |
|                |                                                                                                                                                                                                                                 | bundle-<bundle-id>.<sub-interface-id>               |         |
|                |                                                                                                                                                                                                                                 |                                                     |         |
|                |                                                                                                                                                                                                                                 | mgmt0                                               |         |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+---------+

The following information is displayed:

+------------------+------------------------------------------------------------------------------------------------------------+
| Field            | Description                                                                                                |
+==================+============================================================================================================+
| Access-list name | The name of the access-list                                                                                |
+------------------+------------------------------------------------------------------------------------------------------------+
| Index            | The rule ID                                                                                                |
+------------------+------------------------------------------------------------------------------------------------------------+
| Type             | The type of rule (allow/deny)                                                                              |
+------------------+------------------------------------------------------------------------------------------------------------+
| Nexthop1         | A single next-hop ipv4/ipv6 address that is eligible for forwarding ipv4/ipv6 traffic                      |
+------------------+------------------------------------------------------------------------------------------------------------+
| Next Table       | The VRF name to which the matched traffic shall be redirected to determine the forwarding behavior         |
+------------------+------------------------------------------------------------------------------------------------------------+
| Protocol         | The protocol specified in the rule                                                                         |
+------------------+------------------------------------------------------------------------------------------------------------+
| DSCP             | The DSCP value received on incoming packet                                                                 |
+------------------+------------------------------------------------------------------------------------------------------------+
| SRC/Dest Ports   | The source/destination ports specified in the rule                                                         |
+------------------+------------------------------------------------------------------------------------------------------------+
| SRC/Dest IP      | The source/destination IP specified in the rule                                                            |
+------------------+------------------------------------------------------------------------------------------------------------+
| packet-length    | The IP packet length specified in the rule                                                                 |
+------------------+------------------------------------------------------------------------------------------------------------+
| Matches          | The number of packets that matched the rule (packets that were dropped by prior rules will not be counted) |
+------------------+------------------------------------------------------------------------------------------------------------+
| Log              | Indicates wether to generate Syslog when there is a match on this rule                                     |
+------------------+------------------------------------------------------------------------------------------------------------+
| CIR              | Commited information rate when there is a match on this rule                                               |
+------------------+------------------------------------------------------------------------------------------------------------+
| CBS              | Commited burst size when there is a match on this rule                                                     |
+------------------+------------------------------------------------------------------------------------------------------------+
| Violated packets | The number of packets that matched the rule and dropped by the policer (+average drops in last 5 seconds)  |
+------------------+------------------------------------------------------------------------------------------------------------+
| Violated octets  | The number of octets that matched the rule and dropped by the policer (+average drops in last 5 seconds)   |
+------------------+------------------------------------------------------------------------------------------------------------+

**Example**
::


	dnRouter# show access-lists counters bundle-1
	Interface: bundle-1
	Access Lists  Ipv4
	Direction: in
	| Access-list name   | Index         | Type   | Nexthop1     | Next Table |  Protocol   | Src Ports   | Src IP   | Dest Ports   | Dest IP   | Dscp | Packet Length | Description | Log       | CIR (mbps) | CBS (kbytes) | Violated packets    | Violated octets     | Matches |
	|--------------------+---------------+--------+--------------+------------+-------------+-------------+----------+--------------+-----------+------+---------------+-------------+-----------+------------+--------------+---------------------+---------------------+---------|
	| MyAclName (global) | 10            | allow  |              |            |  any        | any         | any      | any          | any       | any  |    any        |             |           | 100        | 200          | 5000 (26 pps)       | 5000000 (26000 bps) | 100     |
	|                    | 15            | deny   |              |            |  icmp       | any         | 10.1.1.2 | any          | any       | any  |    any        |             | Enabled   |            |              |                     |                     | N/A     |
	|                    | default-icmp  | allow  |              |            |  icmp       | any         | any      | any          | any       | any  |    any        |             |           |            |              |                     |                     | N/A     |
	|                    | default       | deny   |              |            |  any        | any         | any      | any          | any       | any  |    any        |             |           |            |              |                     |                     | N/A     |
	| MySecondACL        | 10            | allow  |              |            |  tcp        | 100-4500    | 10.1.1.2 | any          | any       | any  |    any        |             |           |            |              |                     |                     | 100     |
	|                    | default-icmp  | allow  |              |            |  icmp       | any         | any      | any          | any       | any  |    any        |             |           |            |              |                     |                     | 100     |
	|                    | default       | deny   |              |            |  any        | any         | any      | any          | any       | any  |    any        |             |           |            |              |                     |                     | 100     |


	Direction: out
	| Access-list name   | Index         | Type   | Nexthop1     | Next Table |  Protocol   | Src Ports   | Src IP   | Dest Ports   | Dest IP   | Dscp | Packet Length | Description | CIR (mbps) | CBS (kbytes) | Violated packets    | Violated octets     | Matches |
	|--------------------+---------------+--------+--------------+------------+-------------+-------------+----------+--------------+-----------+------+---------------+-------------+------------+--------------+---------------------+---------------------+---------|
	| MyAclName (global) | 10            | allow  |              |            |  any        | any         | any      | any          | any       | any  |    any        |             | 100        | 200          | 5000 (26 pps)       | N/A                 | 100     |
	|                    | 15            | deny   |              |            |  icmp       | any         | 10.1.1.2 | any          | any       | any  |    any        |             |            |              |                     |                     | N/A     |
	|                    | default-icmp  | allow  |              |            |  icmp       | any         | any      | any          | any       | any  |    any        |             |            |              |                     |                     | N/A     |
	|                    | default       | deny   |              |            |  any        | any         | any      | any          | any       | any  |    any        |             |            |              |                     |                     | N/A     |
	| MySecondACL        | 10            | allow  |              |            |  tcp        | 100-4500    | 10.1.1.2 | any          | any       | any  |    any        |             |            |              |                     |                     | 100     |
	|                    | default-icmp  | allow  |              |            |  icmp       | any         | any      | any          | any       | any  |    any        |             |            |              |                     |                     | 100     |
	|                    | default       | deny   |              |            |  any        | any         | any      | any          | any       | any  |    any        |             |            |              |                     |                     | 100     |

	Access Lists  Ipv6
	Direction: in
	| Access-list name   | Index          | Type   | Nexthop1     | Next Table | Protocol   | Src Ports   | Src IP       | Dest Ports   | Dest IP   | Dscp | Packet Length | Description | Log       | CIR (mbps) | CBS (kbytes) | Violated packets    | Violated octets     | Matches |
	|--------------------+----------------+--------+--------------+------------+------------+-------------+--------------+--------------+-----------+------+---------------+-------------+-----------+------------+--------------+---------------------+---------------------+---------|
	| MyAclName (global) | 10             | allow  |              |            | any        | any         | any          | any          | any       | any  |    any        |             |           | 100        | 200          | 5000 (26 pps)       | 5000000 (26000 bps) | 100     |
	|                    | 15             | deny   |              |            | icmp       | any         | 2001:1234::1 | any          | any       | any  |    any        |             | Enabled   |            |              |                     |                     | N/A     |
	|                    | default-icmp-v6| allow  |              |            | ipv6-icmp  | any         | any          | any          | any       | any  |    any        |             |           |            |              |                     |                     | N/A     |
	|                    | default        | deny   |              |            | any        | any         | any          | any          | any       | any  |    any        |             |           |            |              |                     |                     | N/A     |
	| MySecondACL        | 10             | allow  |              |            | tcp        | 100-4500    | 1001::2222:2 | any          | any       | any  |    any        |             |           |            |              |                     |                     | 100     |
	|                    | default-icmp-v6| allow  |              |            | ipv6-icmp  | any         | any          | any          | any       | any  |    any        |             |           |            |              |                     |                     | 100     |
	|                    | default        | deny   |              |            | any        | any         | any          | any          | any       | any  |    any        |             |           |            |              |                     |                     | 100     |

	Direction: out


	dnRouter# show access-lists counters
	Interface: bundle-1
	Access Lists  Ipv4
	Direction: in
	| Access-list name   | Index         | Type   | Nexthop1     | Next Table | Protocol   | Src Ports   | Src IP   | Dest Ports   | Dest IP   | Dscp | Packet Length | Description | Log       | CIR (mbps) | CBS (kbytes) | Violated packets    | Violated octets     | Matches |
	|--------------------+---------------+--------+--------------+------------+------------+-------------+----------+--------------+-----------+------+---------------+-------------+-----------+------------+--------------+---------------------+---------------------+---------|
	| MyAclName (global) | 10            | allow  |              |            | any        | any         | any      | any          | any       | any  |    any        |             |           | 100        | 200          | 5000 (26 pps)       | 5000000 (26000 bps) | 100     |
	|                    | 15            | deny   |              |            | icmp       | any         | 10.1.1.2 | any          | any       | any  |    any        |             | Enabled   |            |              |                     |                     | N/A     |
	|                    | default-icmp  | allow  |              |            | icmp       | any         | any      | any          | any       | any  |    any        |             |           |            |              |                     |                     | N/A     |
	|                    | default       | deny   |              |            | any        | any         | any      | any          | any       | any  |    any        |             |           |            |              |                     |                     | N/A     |
	| MySecondACL        | 10            | allow  |              |            | tcp        | 100-4500    | 10.1.1.2 | any          | any       | any  |    any        |             |           |            |              |                     |                     | 100     |
	|                    | default-icmp  | allow  |              |            | icmp       | any         | any      | any          | any       | any  |    any        |             |           |            |              |                     |                     | 100     |
	|                    | default       | deny   |              |            | any        | any         | any      | any          | any       | any  |    any        |             |           |            |              |                     |                     | 100     |


	Direction: out

	Access Lists  Ipv6
	Direction: in
	| Access-list name   | Index          | Type   | Nexthop1     | Next Table | Protocol   | Src Ports   | Src IP       | Dest Ports   | Dest IP   | Dscp | Packet Length | Description | Log       | CIR (mbps) | CBS (kbytes) | Violated packets    | Violated octets     | Matches |
	|--------------------+----------------+--------+--------------+------------+------------+-------------+--------------+--------------+-----------+------+---------------+-------------+-----------+------------+--------------+---------------------+---------------------+---------|
	| MyAclName (global) | 10             | allow  |              |            | any        | any         | any          | any          | any       | any  |    any        |             |           | 100        | 200          | 5000 (26 pps)       | 5000000 (26000 bps) | 100     |
	|                    | 15             | deny   |              |            | icmp       | any         | 2001:1234::1 | any          | any       | any  |    any        |             | Enabled   |            |              |                     |                     | N/A     |
	|                    | default-icmp-v6| allow  |              |            | ipv6-icmp  | any         | any          | any          | any       | any  |    any        |             |           |            |              |                     |                     | N/A     |
	|                    | default        | deny   |              |            | any        | any         | any          | any          | any       | any  |    any        |             |           |            |              |                     |                     | N/A     |
	| MySecondACL        | 10             | allow  |              |            | tcp        | 100-4500    | 1001::2222:2 | any          | any       | any  |    any        |             |           |            |              |                     |                     | 100     |
	|                    | default-icmp-v6| allow  |              |            | ipv6-icmp  | any         | any          | any          | any       | any  |    any        |             |           |            |              |                     |                     | 100     |
	|                    | default        | deny   |              |            | any        | any         | any          | any          | any       | any  |    any        |             |           |            |              |                     |                     | 100     |


	Direction: out

	Interface: bundle-2
	Access Lists  Ipv4
	Direction: in
	| Access-list name   | Index         | Type   | Nexthop1     | Next Table | Protocol   | Src Ports   | Src IP   | Dest Ports   | Dest IP   | Dscp | Packet Length | Description | Log       | CIR (mbps) | CBS (kbytes) | Violated packets    | Violated octets     | Matches |
	|--------------------+---------------+--------+--------------+------------+------------+-------------+----------+--------------+-----------+------+---------------+-------------+-----------+------------+--------------+---------------------+---------------------+---------|
	| MyAclName (global) | 10            | allow  |              |            | any        | any         | any      | any          | any       | any  |    any        |             |           | 100        | 200          | 5000 (26 pps)       | 5000000 (26000 bps) | 100     |
	|                    | 15            | deny   |              |            | icmp       | any         | 10.1.1.2 | any          | any       | any  |    any        |             | Enabled   |            |              |                     |                     | N/A     |
	|                    | default-icmp  | allow  |              |            | icmp       | any         | any      | any          | any       | any  |    any        |             |           |            |              |                     |                     | N/A     |
	|                    | default       | deny   |              |            | any        | any         | any      | any          | any       | any  |    any        |             |           |            |              |                     |                     | N/A     |

	Direction: out


	Access Lists  Ipv6
	Direction: in
	| Access-list name   | Index          | Type   | Nexthop1     | Next Table | Protocol   | Src Ports   | Src IP       | Dest Ports   | Dest IP   | Dscp | Packet Length | Description | Log       | CIR (mbps) | CBS (kbytes) | Violated packets    | Violated octets     | Matches |
	|--------------------+----------------+--------+--------------+------------+------------+-------------+--------------+--------------+-----------+------+---------------+-------------+-----------+------------+--------------+---------------------+---------------------+---------|
	| MyAclName (global) | 10             | allow  |              |            | any        | any         | any          | any          | any       | any  |    any        |             |           | 100        | 200          | 5000 (26 pps)       | 5000000 (26000 bps) | 100     |
	|                    | 15             | deny   |              |            | icmp       | any         | 2001:1234::1 | any          | any       | any  |    any        |             | Enabled   |            |              |                     |                     | N/A     |
	|                    | default-icmp-v6| allow  |              |            | ipv6-icmp  | any         | any          | any          | any       | any  |    any        |             |           |            |              |                     |                     | N/A     |
	|                    | default        | deny   |              |            | any        | any         | any          | any          | any       | any  |    any        |             |           |            |              |                     |                     | N/A     |


	Direction: out


	Interface: mgmt0
	Access Lists  Ipv4
	Direction: in
	| Access-list name   | Index         | Type   | Nexthop1     | Next Table | Protocol   | Src Ports   | Src IP   | Dest Ports   | Dest IP   | Dscp | Packet Length | Matches | Description | Log       |
	|--------------------+---------------+--------+--------------+------------+------------+-------------+----------+--------------+-----------+------+---------------+---------|-------------+-----------+
	| MyAclName          | 10            | allow  |              |            | any        | any         | any      | any          | any       | any  |    any        | N/A     |             |           |
	|                    | 15            | deny   |              |            | icmp       | any         | 10.1.1.2 | any          | any       | any  |    any        | N/A     |             | Enabled   |
	|                    | default-icmp  | allow  |              |            | icmp       | any         | any      | any          | any       | any  |    any        | N/A     |             |           |
	|                    | default       | deny   |              |            | any        | any         | any      | any          | any       | any  |    any        | N/A     |             |           |

	Direction: out


	Access Lists  Ipv6
	Direction: in
	| Access-list name   | Index          | Type   | Nexthop1     | Next Table | Protocol   | Src Ports   | Src IP       | Dest Ports   | Dest IP   | Dscp | Packet Length | Matches | Description | Log       |
	|--------------------+----------------+--------+--------------+------------+------------+-------------+--------------+--------------+-----------+------+---------------+---------|-------------+-----------+
	| MyAclName          | 10             | allow  |              |            | any        | any         | any          | any          | any       | any  |    any        | N/A     |             |           |
	|                    | 15             | deny   |              |            | icmp       | any         | 2001:1234::1 | any          | any       | any  |    any        | N/A     |             | Enabled   |
	|                    | default-icmp-v6| allow  |              |            | ipv6-icmp  | any         | any          | any          | any       | any  |    any        | N/A     |             |           |
	|                    | default        | deny   |              |            | any        | any         | any          | any          | any       | any  |    any        | N/A     |             |           |


	Direction: out

	** Example output for NCP hardware model AS9286-32D **

	dnRouter# show access-lists counters

	Interfaces: bundle-1, bundle-2, bundle-3, ge400-0/0/0

	Direction: in

	| Access-list name   | Index        | Type   | Nexthop1   | Next-Table   | Protocol   | Src Ports   | Src IP   | Dest Ports   | Dest IP   | Dscp   | Packet Length   | Matches   | Description   | Log   |
	|--------------------+--------------+--------+------------+--------------+------------+-------------+----------+--------------+-----------+--------+-----------------+-----------+---------------+-------|
	| testipv4           | 1000         | allow  |            |              | any        | any         | any      | any          | any       |        | any             | 0         |               |       |
	|                    | default-icmp | allow  |            |              | icmp(0x01) | any         | any      | any          | any       |        | any             | 0         |               |       |
	|                    | default      | deny   |            |              | any        | any         | any      | any          | any       |        | any             | 0         |               |       |

.. **Help line:** show access-lists counters

**Note:**

 - For the NCP hardware model AS9286-32D, the access-list counters are aggregated for all interfaces to which the access-list is attached in the same direction. While you can filter by interface-name to view a specific access-list on this platform, the counters do not reflect traffic related to that specific interface


**Command History**

+---------+--------------------------------------------------+
| Release | Modification                                     |
+=========+==================================================+
| 5.1.0   | Command introduced                               |
+---------+--------------------------------------------------+
| 7.0     | Replaced access-list with access-lists in syntax |
+---------+--------------------------------------------------+
| 13.0    | Updated output support for DSCP and Nexthop      |
+---------+--------------------------------------------------+
| 16.2    | Updated output support for Next Table            |
+---------+--------------------------------------------------+
| 17.0    | Updated output support for Packet Length         |
+---------+--------------------------------------------------+
| 19.2    | Updated output support for Log                   |
+---------+--------------------------------------------------+
| 19.3    | Updated output support for rate-limit            |
+---------+--------------------------------------------------+
| 25.2    | Update output for NCP hardware model AS9286-32D  |
+---------+--------------------------------------------------+
