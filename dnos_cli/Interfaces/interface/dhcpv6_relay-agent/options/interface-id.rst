interfaces dhcpv6 relay-agent options interface-id
--------------------------------------------------

**Minimum user role:** operator

"To set the DHCPv6 option 18 Interface ID, as specified in RFC 8415:"

**Command syntax: interface-id [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces dhcpv6 relay-agent options

**Note**

- The default behavior is to add the interface ID option to relayed DHCPv6 messages. This option is currently only supported in NC-AI.

**Parameter table**

+-------------+----------------------------------------------------------------------------------+--------------+---------+
| Parameter   | Description                                                                      | Range        | Default |
+=============+==================================================================================+==============+=========+
| admin-state | Relay Agent Interface-ID (option 18) — An ASCII string that identifies the       | | enabled    | enabled |
|             | interface on which the client DHCPv6 packet is received.                         | | disabled   |         |
+-------------+----------------------------------------------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# dhcpv6 relay-agent
    dnRouter(cfg-if-ge100-0/0/0-dhcpv6-relay)# options
    dnRouter(cfg-if-ge100-0/0/0-dhcpv6-relay-options)# interface-id enabled


**Removing Configuration**

To revert the interface-id option configuration to its default value:
::

    dnRouter(cfg-if-ge100-0/0/0-dhcpv6-relay-options)# no interface-id

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 25.2    | Command introduced |
+---------+--------------------+
