interfaces ipv6-admin-state
---------------------------

**Minimum user role:** operator

Interface will support ipv6 traffic if one of the following conditions is met
- Interface has ipv6-address configured. Used for Global Unicast Address
- Interface is enabled for dhcpv6 client support
- Interface ipv6-admin-state is explicitly enabled

In case ipv6-admin-state is explicitly disabled, interface will not support ipv6 traffic
In case ipv6-admin-state is enabled, but no ipv6-address configured, interface will support ipv6 traffic leverging link-local address.

To configure ipv6-admin-state:

**Command syntax: ipv6-admin-state [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Physical
  - Physical vlan
  - Bundle
  - Bundle vlan
  - IRB

**Parameter table**

+-------------+---------------------------------------------------------+--------------+---------+
| Parameter   | Description                                             | Range        | Default |
+=============+=========================================================+==============+=========+
| admin-state | Sets the administrative state of IPv6 on the interface. | | enabled    | \-      |
|             |                                                         | | disabled   |         |
+-------------+---------------------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# ipv6-admin-state enabled
    dnRouter(cfg-if-ge100-0/0/0)# ipv6-admin-state disabled


**Removing Configuration**

To revert to the default state:
::

    dnRouter(cfg-if-ge100-0/0/0)# no ipv6-admin-state

**Command History**

+---------+---------------------------------------------------------+
| Release | Modification                                            |
+=========+=========================================================+
| 15.0    | Command introduced                                      |
+---------+---------------------------------------------------------+
| 19.3    | Update behavior for case ipv6-address is not configured |
+---------+---------------------------------------------------------+
