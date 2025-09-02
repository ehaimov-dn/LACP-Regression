show route forwarding-table
---------------------------

**Minimum user role:** viewer

To display the forwarding table, use the following command:

**Command syntax: show route forwarding-table** {vrf [vrf-name] | all} {ipv4 \| ipv6 \| ipv4 [ipv4-prefix] \| ipv6 [ipv6-prefix]} ncp [ncp-id]

**Command mode:** operational

..
	**Internal Note**

	- By default, the command output includes ipv4 & ipv6 forwarding-table.

	- By default, the information will be sent from the active NCP with the lowest ID.

	- Brief view display is order by prefix numeric value from lowest to highest

	- For MPLS, in the Egress-Encapsulation column, display the pushed mpls label for the route.

	- Support up to 7 mpls labels.

	- First label to the left is the outermost (top) label on the label stack the information will be sent from the first configured active forwarder id.

	- For SRv6, only the first SID is displayed, with the number of additional SIDs. the full SID stack will be displayed by the detailed command.

	- Technical limitations:

	- On large scale routing tables, the table might not be presented ordered

	- When there are routing table updates while presenting the table, the table might contain duplicate entries and might not contain all entries.

**Parameter table**

+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|  Parameter  |                                                                                  Description                                                                                 |
+=============+==============================================================================================================================================================================+
| ipv4        | Displays only IPv4 forwarding table                                                                                                                                          |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ipv6        | Displays only IPv6 forwarding table                                                                                                                                          |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ipv4-prefix | Displays the forwarding table for the specified IPv4 prefix (displays IPv4 route table)                                                                                      |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ipv6-prefix | Displays the forwarding table for the specified IPv6 prefix (displays IPv6 route table)                                                                                      |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vrf-name    | Displays the forwarding table for the specified VRF. If not specified, the global VRF forwarding table is displayed. If All is specified, all configured VRFs are displayed  |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ncp-id      | Displays information from a specific NCP. By default, information is sent from the active NCP with the lowest ID                                                             |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The following information is displayed on each route:

+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| Attribute            | Description                                                                                                                                |
+======================+============================================================================================================================================+
| Type                 | The type of route:                                                                                                                         |
|                      | Connected - connected routes                                                                                                               |
|                      | Local - routes designated to NCC (punted)                                                                                                  |
|                      | Discard - discarded routes due to NCC ruling                                                                                               |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| IP-prefix            | The prefix of the route                                                                                                                    |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| Next Hop             | The next hop (IP or tunnel)                                                                                                                |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| Interface            | The interface of the route                                                                                                                 |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| Egress-Encapsulation | The egress encapsulation of the route. Up to 7 MPLS labels are supported. The leftmost label displayed is the outermost (top) label on the |
|                      | label stack. For SRv6, only the first SID is displayed, the full SID stack will be displayed by the detailed command.                      |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------+

**Example**
::

	dnRouter# show route forwarding-table

	Legend: * - Active, A - Alternate path, B - Bypass, S - Secondary, EA - Enhanced-Alternate
	Egress-Encapsulation: M - MPLS {labels are arranged from top (left) to BoS (right), E - Entropy Label}
						V - VXLAN {vtep id}, RSVP - RSVP Tunnel {'tunnel name'}, SRv6 - SRv6 {First segment + Number of additional segments}

	VRF: default
	NCP-ID: 0
	IPv4 Forwarding Table:
	| IP Prefix                      | Next Hop                       | Interface            | Egress-Encapsulation                                                                |
	+--------------------------------+--------------------------------+----------------------+-------------------------------------------------------------------------------------+
	| (*)1.1.3.0/31                  | 1.3.16.0                       | bundle-100.1004      |                                                                                     |
	| (*)1.1.6.0/31                  | 1.6.16.0                       | bundle-1002          |                                                                                     |
	| (*)1.1.17.0/31                 | 1.16.17.1                      | bundle-1550.3856     |                                                                                     |
	| (*)1.1.210.0/31                | 1.3.16.0                       | bundle-100.1004      |                                                                                     |
	| (*)1.6.16.1/31                 | connected                      | bundle-1002          |                                                                                     |
	| (*)1.6.16.0/32                 | connected                      | bundle-1002          |                                                                                     |
	| (*)1.6.16.1/32                 | local                          |                      |                                                                                     |
	| (*)1.8.16.1/31                 | connected                      | bundle-2002          |                                                                                     |
	| (*)1.8.16.0/32                 | connected                      | bundle-2002          |                                                                                     |
	| (*)1.8.16.1/32                 | local                          |                      |                                                                                     |
	| (*)1.16.209.0/24               | 1.3.16.0                       | bundle-100.1004      |                                                                                     |
	| (*)101.10.1.100/32             | 1.3.16.0                       | bundle-100.1004      | M{77402}                                                                            |
	| (*)                            | 1.3.16.0                       | bundle-100.1004      | M{77363}                                                                            |
	| (A)                            | 1.4.64.1                       | bundle-200           | RSVP{Tunnel_A},M{3,377,555}                                                         |
	| (*)101.10.1.103/32             | 1.3.16.0                       | bundle-100.1004      | RSVP{Tunnel_1},M{77361}                                                             |
	| (*)                            | 1.3.16.0                       | bundle-100.1004      | RSVP{Tunnel_2},M{77375}                                                             |
	| (*)                            | 1.3.16.0                       | bundle-100.1004      | RSVP{Tunnel_3},M{77333}                                                             |
	|   (B)                          | 1.4.64.1                       | bundle-200           | RSVP{Tunnel_bypass},M{7,733,371,348}                                                |
	| (*)101.10.1.104/32             | 1.3.16.0                       | bundle-100.1004      | RSVP{Tunnel_4},M{77461}                                                             |
	|  (S)                           | 1.4.64.1                       | bundle-200           | RSVP{Tunnel_4},M{7,733,371,348}                                                     |
	| (*)99.99.99.99/32              | discard                        | Null0                |                                                                                     |

	IPv6 Forwarding Table:
	| IP Prefix                      | Next Hop                       | Interface            | Egress-Encapsulation                                                                |
	+--------------------------------+--------------------------------+----------------------+-------------------------------------------------------------------------------------+
	| (*)2001:1235::0/122            | 2001:1235::1                   | bundle-3             | M{100}                                                                              |
	| (*)                            | 2001:1111::2                   | bundle-3             | M{300}                                                                              |
	| (*)2001:1111::1/128            | local                          |                      |                                                                                     |
	| (*)2001:4444::0/128            | discard                        | Null0                |                                                                                     |
	| (*)2003:3221::0/122            | 2003:3221::1                   | bundle-5             | SRv6{2001:db8:4001:4002:4003::+2}                                                   |



	dnRouter# show route forwarding-table ipv6 ncp 2

	Legend: * - Active, A - Alternate path, B - Bypass, S - Secondary, EA - Enhanced-Alternate
	Egress-Encapsulation: M - MPLS {labels are arranged from top (left) to BoS (right), E - Entropy Label}
						V - VXLAN {vtep id}, RSVP - RSVP Tunnel {'tunnel name'}, SRv6 - SRv6 {First segment + Number of additional segments}

	VRF: default
	NCP-ID: 2
	IPv6 Forwarding Table:
	| IP Prefix                      | Next Hop                       | Interface            | Egress-Encapsulation                                                                |
	+--------------------------------+--------------------------------+----------------------+-------------------------------------------------------------------------------------+
	| (*)2001:1235::0/122            | 2001:1235::1                   | bundle-3             | M{100}                                                                              |
	| (*)                            | 2001:1111::2                   | bundle-3             | M{300},V{50091}                                                                     |
	| (*)2001:1111::1/128            | local                          |                      |                                                                                     |
	| (*)2003:3221::0/122            | 2003:3221::1                   | bundle-5             | SRv6{2001:db8:4001:4002:4003::+2}                                                   |


	dnRouter# show route forwarding-table ipv4
	dnRouter# show route forwarding-table vrf default ipv4
	dnRouter# show route forwarding-table ipv6

	dnRouter# show route forwarding-table vrf MyVrf_1 ipv4 1.6.16.1/31
	VRF: MyVrf_1
	IPv4 Forwarding Table:
	Destination: 90.1.1.0/24
	    next-hop: connected
	    Interface: bundle-1002

	dnRouter# show route forwarding-table ipv4 90.1.1.0/24
	VRF: default
	IPv4 Forwarding Table:
	Destination: 90.1.1.0/24
	    next-hop(1): 2.2.2.2, Active
	    Interface: bundle-2
	    next-hop(2): 4.4.4.4, Active
	    interface: bundle-4
	    Alternate-path:
	      next-hop: 3.3.3.3 Recursive
	        next-hop(3,1): 13.0.1.1
	        mpls labels: 8156(top)
	        interface: bundle-3
	        via tunnel_1
	        Bypass:
	          next-hop: 13.0.2.1
	          mpls labels: 74413(top),8245
	          Interface: bundle-2
	          via bypass_1
	      next-hop(3,2): 13.0.1.1
	      mpls labels: 87441
	      interface: bundle-3
	      via tunnel_2
	      Bypass:
			next-hop: 13.0.2.1
			mpls labels: 74414(top),8247
			interface: bundle-2
			via bypass_1

	dnRouter# show route forwarding-table ipv4 91.1.0.0/24
	VRF: default
	IPv4 Forwarding Table:
	Destination: 90.1.0.0/24
	    next-hop(1): 2.2.2.2 Recursive, Active
	    mpls labels: 1001(top)
	      next-hop(1,1): 13.0.1.1 Active
	      mpls labels: 100
	      interface: bundle-3
	      via tunnel_1
	      Bypass:
	        next-hop: 13.0.2.1
	        mpls labels: 101(top), 100
	        Interface: bundle-2
	        via bypass_1
	      next-hop(1,2): 13.0.1.1 Active
	      mpls labels: 102(top)
	      interface: bundle-3
	      via tunnel_2
	      Secondary:
	        next-hop: 13.0.2.1
	        mpls labels: 103
	        Interface: bundle-2
	        via tunnel_2
	    next-hop(2): 8.8.8.8 Recursive, Active
	    mpls labels: 2542(top)
	      next-hop(2,1): 14.0.1.1 Active
	      mpls labels: 103(top)
	      Interface: bundle-4
	      via tunnel_4
	      next-hop(2,2): 14.0.1.1 Active
	      mpls labels: 104(top)
	      interface: bundle-3
	      via tunnel_5

	dnRouter# show route forwarding-table ipv6 91.1.0.0/24
	NCP-ID: 0
	VRF: default
	IPv6 Forwarding Table:
	Destination: 2003:3221::0/122
		next-hop(1): 2005:3227::8 Recursive, Active
		next-hop(1,1): 2000::2 Active
		srv6 segments: 2001:db8:4001:4002:4003::
						2001:db8:5001:5002:5003::
						2001:db8:6001:6002:6003::
		interface: ge100-0/0/1


.. **Help line:** show route forwarding-table

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 5.1.0   | Command introduced |
+---------+--------------------+
| 11.0    | Added NCP filter   |
+---------+--------------------+
| 16.1    | Added All filter   |
+---------+--------------------+
