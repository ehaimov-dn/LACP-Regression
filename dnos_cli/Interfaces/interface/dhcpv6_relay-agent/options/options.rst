interfaces dhcpv6 relay-agent options
-------------------------------------

**Minimum user role:** operator

To enter DHCPv6 relay agent's options configuration mode:

**Command syntax: options**

**Command mode:** config

**Hierarchies**

- interfaces dhcpv6 relay-agent

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# dhcpv6 relay-agent
    dnRouter(cfg-if-ge100-0/0/0-dhcpv6-relay)# options
    dnRouter(cfg-if-ge100-0/0/0-dhcpv6-relay-options)#


**Removing Configuration**

To remove the DHCPv6 relay agent's options configuration:
::

    dnRouter(cfg-if-ge100-0/0/0-dhcpv6-relay)# no options

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 25.2    | Command introduced |
+---------+--------------------+
