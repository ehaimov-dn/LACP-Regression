interfaces dhcpv6 relay-agent vrf
---------------------------------

**Minimum user role:** operator

To configure the target VRF for all DHCPv6 servers of the relay agent interface:

**Command syntax: vrf [vrf-name]**

**Command mode:** config

**Hierarchies**

- interfaces dhcpv6 relay-agent

**Note**

- In case that destination VRF is configured, it shall apply to all DHCPv6 servers on the relay agent interface. If not configured, then all DHCPv6 servers must be in the same VRF as the relaying interface.

**Parameter table**

+-----------+----------------------------------------------------------------------------------+------------------+---------+
| Parameter | Description                                                                      | Range            | Default |
+===========+==================================================================================+==================+=========+
| vrf-name  | The name of the VRF instance of the DHCPv6 servers (if different from the        | | string         | \-      |
|           | interface VRF)                                                                   | | length 1-255   |         |
+-----------+----------------------------------------------------------------------------------+------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# dhcpv6 relay-agent
    dnRouter(cfg-if-ge100-0/0/0-dhcpv6-relay)# vrf MyVRF_2


**Removing Configuration**

To remove the destination VRF configuration:
::

    dnRouter(cfg-if-ge100-0/0/0-dhcpv6-relay)# no vrf

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 25.2    | Command introduced |
+---------+--------------------+
