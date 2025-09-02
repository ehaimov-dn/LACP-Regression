show access-lists counters global-acl
-------------------------------------

**Minimum user role:** viewer

To display the global in-band access-list:



**Command syntax: show access-lists counters global-acl** [access-list-type] [access-list-name]

**Command mode:** operational


..
	**Internal Note**

	- When a user selects a specific type/access-list-name it will filter according to it

	- The user should be able to filter with several parameters on the same line. (filter by access-list-name)


**Parameter table**

+------------------+------------------------------------------------------------+-------------------------------------+---------+
| Parameter        | Description                                                | Range                               | Default |
+==================+============================================================+=====================================+=========+
| access-list-type | Filter the displayed information to a specific type        | IPv4                                | \-      |
|                  |                                                            | IPv6                                |         |
+------------------+------------------------------------------------------------+-------------------------------------+---------+
| access-list-name | Filter the displayed information to a specific access-list | The name of an existing access-list |         |
+------------------+------------------------------------------------------------+-------------------------------------+---------+

The following information is displayed in the table:

+------------------+------------------------------------------------------------------------------------------------------------+
| Field            | Description                                                                                                |
+==================+============================================================================================================+
| Access-list name | The name of the access-list                                                                                |
+------------------+------------------------------------------------------------------------------------------------------------+
| Index            | The rule ID                                                                                                |
+------------------+------------------------------------------------------------------------------------------------------------+
| Type             | The type of rule (allow/deny/description)                                                                  |
+------------------+------------------------------------------------------------------------------------------------------------+
| Nexthop1         | A single next-hop ipv4/ipv6 address that is eligible for forwarding ipv4/ipv6 traffic                      |
+------------------+------------------------------------------------------------------------------------------------------------+
| Next-Table       | Next VRF table to which matching packet will be forwarded                                                  |
+------------------+------------------------------------------------------------------------------------------------------------+
| Protocol         | The protocol specified in the rule                                                                         |
+------------------+------------------------------------------------------------------------------------------------------------+
| DSCP             | The DSCP value received on incoming packet                                                                 |
+------------------+------------------------------------------------------------------------------------------------------------+
| Packet Length    | The Packet length in the rule                                                                              |
+------------------+------------------------------------------------------------------------------------------------------------+
| SRC/Dest Ports   | The source/destination ports specified in the rule                                                         |
+------------------+------------------------------------------------------------------------------------------------------------+
| SRC/Dest IP      | The source/destination IP specified in the rule                                                            |
+------------------+------------------------------------------------------------------------------------------------------------+
| Matches          | The number of packets that matched the rule (packets that were dropped by prior rules will not be counted) |
+------------------+------------------------------------------------------------------------------------------------------------+

**Example**
::


    dnRouter# show access-lists counters global-acl

    Access Lists - Ipv4

    Direction: in

    | Access-list name   | Index        | Type   | Nexthop1   | Next-Table   | Protocol   | Src Ports   | Src IP   | Dest Ports   | Dest IP   | Dscp   | Packet Length   | Description   | Log   | Matches   |
    |--------------------+--------------+--------+------------+--------------+------------+-------------+----------+--------------+-----------+--------+-----------------+---------------+-------+-----------|
    | test               | 1000         | allow  |            |              | any        | any         | any      | any          | any       |        | any             |               |       | 13        |
    |                    | default-icmp | allow  |            |              | icmp(0x01) | any         | any      | any          | any       |        | any             |               |       | 13        |
    |                    | default      | deny   |            |              | any        | any         | any      | any          | any       |        | any             |               |       | 13        |

    Access Lists - Ipv6

    Direction: in

    | Access-list name   | Index   | Type   | Nexthop1   | Next-Table   | Protocol   | Src Ports   | Src IP   | Dest Ports   | Dest IP   | Dscp   | Packet Length   | Description   | Log   | Matches   |
    |--------------------+---------+--------+------------+--------------+------------+-------------+----------+--------------+-----------+--------+-----------------+---------------+-------+-----------|

.. **Help line:** Shows access-lists global-acl counters

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+


