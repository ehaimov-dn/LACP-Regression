interfaces ndp router-advertisement prefix-advertisement prefix
---------------------------------------------------------------

**Minimum user role:** operator

A list of prefixes to be placed in the Prefix Information options in Router Advertisement messages, sent from the interface.
By default, all interface configured global addresses are advertised as prefix information (the link local address is not advertised).
Users may set a locally configured IPv6 prefix to modify its related prefix option attributes.
Users may configure additional prefixes to be sent in Router Advertisement.
To configure a prefix and enter its configuration level:

**Command syntax: prefix [ipv6-prefix]**

**Command mode:** config

**Hierarchies**

- interfaces ndp router-advertisement prefix-advertisement

**Note**
- A configured prefix can have both network and host bits set.
- Only the subnet is advertised, i.e., bits not within the prefix-length will be zero.
- Cannot configure (commit validation) multiple prefixes from the same subnet.

**Parameter table**

+-------------+----------------------+------------+---------+
| Parameter   | Description          | Range      | Default |
+=============+======================+============+=========+
| ipv6-prefix | IPv6 address prefix. | X:X::X:X/x | \-      |
+-------------+----------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ndp router-advertisement
    dnRouter(cfg-if-ge100-1/1/1-ndp-ra)# prefix-advertisement
    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# prefix 2006:18:91::48/127
    dnRouter(cfg-ndp-ra-pr-adv-prefix)#


**Removing Configuration**

To remove prefixes:
::

    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# no prefix 

To remove a specific prefix:
::

    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# no prefix 2006:18:91::48/127

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+
