show srv6 forwarding-table
---------------------------

**Minimum user role:** viewer

To display the forwarding table, use the following command:

**Command syntax: show srv6 forwarding-table** {vrf [vrf-name] | all} {local-sid \| local-sid [ipv6-prefix]} ncp [ncp-id]

**Command mode:** operational

..
	**Internal Note**

	- By default, the information will be sent from the active NCP with the lowest ID.

	- Brief view display is order by prefix numeric value from lowest to highest

	- Technical limitations:

	- On large scale routing tables, the table might not be presented ordered

	- When there are routing table updates while presenting the table, the table might contain duplicate entries and might not contain all entries.

**Parameter table**

+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|  Parameter  |                                                                                  Description                                                                                 |
+=============+==============================================================================================================================================================================+
| local-sid   | Displays only SRv6 local-sid forwarding table                                                                                                                                |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ipv6-prefix | Displays the SRv6 local-sid forwarding table information for the specified SRv6 local-sid (displays IPv6 route table)                                                        |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vrf-name    | Displays the forwarding table for the specified VRF. If not specified, the global VRF forwarding table is displayed. If All is specified, all configured VRFs are displayed  |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ncp-id      | Displays information from a specific NCP. By default, information is sent from the active NCP with the lowest ID                                                             |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The following information is displayed on each route:
,
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Attribute            | Description                                                                                                                                           |
+======================+=======================================================================================================================================================+
| srv6-local-sid       | The type of route:                                                                                                                                    |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Next Hop             | The prefix of the route                                                                                                                               |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Interface            | The interface of the route                                                                                                                            |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Egress-Encapsulation | The Egress encapsulation for the local-sid.                                                                                                           |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

**Example**
::

	dnRouter# show srv6 forwarding-table local-sid

	NCP-ID: 0
	Base locator length: 32
	VRF: default
	SRv6 Local SID Forwarding Table:

	| srv6-local-sid                 | Behavior | Next Hop                       | Interface            | Egress-Encapsulation                             |
	+--------------------------------+----------+--------------------------------+----------------------+--------------------------------------------------+
	| 2001:db8:1:4001::/64           | END.X    | 10.10.10.2                     | ge100-0/0/1          |                                                  |
	| 2001:db8:1:4002::/64           | END.X    | 10.10.11.2                     | ge100-0/0/2          |                                                  |
	| 2001:db8:3001::/48             | END      |                                |                      |                                                  |
	| 2001:db8:3002::/48             | END      |                                |                      |                                                  |


	dnRouter# show srv6 forwarding-table local-sid ncp 2

	NCP-ID: 2
	Base locator length: 32
	VRF: default
	SRv6 Local SID Forwarding Table:

	| srv6-local-sid                 | Behavior | Next Hop                       | Interface            | Egress-Encapsulation                             |
	+--------------------------------+----------+--------------------------------+----------------------+--------------------------------------------------+
	| 4001:eff3:1:6001::/64           | END.X    | 20.20.20.2                     | ge100-2/0/1          |                                                  |
	| 2001:eff3:1:6002::/64           | END.X    | 20.20.21.2                     | ge100-2/0/2          |                                                  |
	| 2001:eff3:7001::/48             | END      |                                |                      |                                                  |
	| 2001:eff3:7002::/48             | END      |                                |                      |                                                  |


	dnRouter# show srv6 forwarding-table local-sid 2001:db8:3001::/48

	NCP-ID: 0
	VRF: default
	SRv6 Local SID 2001:db8:3001::/48
	Behavior: END
	Flavor: NEXT-CSID-ONLY


	dnRouter# show srv6 forwarding-table local-sid 2001:db8:1:4001::/48

	NCP-ID: 0
	VRF: default
	SRv6 Local SID 2001:db8:1:4001::/64
	Behavior: END.X
	Flavor: NEXT-CSID-ONLY
		next-hop(1): 10.10.10.2 Active
		mpls labels: 1000(top),1001,1002
		interface: ge100-0/0/1"""



.. **Help line:** show srv6 forwarding-table

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 25.2    | Command introduced |
+---------+--------------------+
