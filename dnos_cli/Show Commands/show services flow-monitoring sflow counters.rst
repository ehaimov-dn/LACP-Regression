show services flow-monitoring sflow counters
--------------------------------------------

**Minimum user role:** viewer

To display sflow counters per NCP:



**Command syntax: show services flow-monitoring sflow counters**  ncp [ncp-id]

**Command mode:** operational



.. 
	**Internal Note**

	- "show services sflow counters" without parameter, shows cache counters for all NCPs.

**Parameter table**

+-----------+--------------------------------------------------------+--------+
| Parameter | Description                                            | Range  |
+===========+========================================================+========+
| ncp-id    | Filters the displayed information to the specified NCP | 0..255 |
+-----------+--------------------------------------------------------+--------+

The following information is displayed per NCP:

+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Parameter                                               | Description                                                                                                                 |
+=========================================================+=============================================================================================================================+
| Number of sampled IPv4/IPv6/MPLS ingress/egress packets | The number of IPv4/IPv6/MPLS ingress/egress packets that were sampled by the data plane and handled by the flow-tracker     |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Total number of sampled packets                         | The total number of packets that were sampled by the data plane and handled by the flow-tracker (IPv4+IPv6+MPLS)            |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Rate of sampled packets                                 | The current rate of sampled packets by the data plane                                                                       |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Total number of dropped sampled packets                 | The packets that were sampled by the data plane but dropped by the flow-tracker                                             |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+


**Example**
::

	dnRouter# show services flow-monitoring sflow counters ncp 5
	Number of sampled IPv4 ingress packets: 45
	Number of sampled IPv4 egress packets: 45
	Number of sampled IPv6 ingress packets: 21
	Number of sampled IPv6 egress packets: 21
	Number of sampled IPv4oMPLS ingress packets: 2000
	Number of sampled IPv4oMPLS egress packets: 2000
	Number of sampled IPv6oMPLS ingress packets: 2000
	Number of sampled IPv6oMPLS egress packets: 2000
	Total number of sampled packets: 2066
	Rate of sampled packets: 100 pps
	Total number of dropped sampled packets: 120
	
	
	dnRouter# show services flow-monitoring cache counters
	
	NCP-1
	
	Number of sampled IPv4 ingress packets: 45
	Number of sampled IPv4 egress packets: 45
	Number of sampled IPv6 ingress packets: 21
	Number of sampled IPv6 egress packets: 21
	Number of sampled IPv4oMPLS ingress packets: 2000
	Number of sampled IPv4oMPLS egress packets: 2000
	Number of sampled IPv6oMPLS ingress packets: 2000
	Number of sampled IPv6oMPLS egress packets: 2000
	Total number of sampled packets: 2066
	Rate of sampled packets: 100 pps
	Total number of dropped sampled packets: 120
	
	
	NCP-5
	
	Number of sampled IPv4 ingress packets: 45
	Number of sampled IPv4 egress packets: 45
	Number of sampled IPv6 ingress packets: 21
	Number of sampled IPv6 egress packets: 21
	Number of sampled IPv4oMPLS ingress packets: 2000
	Number of sampled IPv4oMPLS egress packets: 2000
	Number of sampled IPv6oMPLS ingress packets: 2000
	Number of sampled IPv6oMPLS egress packets: 2000
	Total number of sampled packets: 2066
	Rate of sampled packets: 100 pps
	Total number of dropped sampled packets: 120
	
	

.. **Help line:** show sflow counters per NCP.

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 25.1    | Command introduced |
+---------+--------------------+


