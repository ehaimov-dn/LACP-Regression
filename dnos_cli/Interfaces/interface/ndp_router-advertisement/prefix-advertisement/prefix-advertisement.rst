interfaces ndp router-advertisement prefix-advertisement
--------------------------------------------------------

**Minimum user role:** operator

The router-advertisement prefix-advertisement configuration defines the router support of transmitting router-advertisement Neighbor Discovery messages over the ipv6 supporting interface.
To enter the prefix-advertisement configuration level:

**Command syntax: prefix-advertisement**

**Command mode:** config

**Hierarchies**

- interfaces ndp router-advertisement

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ndp router-advertisement
    dnRouter(cfg-if-ge100-1/1/1-ndp-ra)# prefix-advertisement
    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)#


**Removing Configuration**

To clear all prefix-advertisement settings:
::

    - dnRouter(cfg-if-ge100-1/1/1-ndp-ra)# no prefix-advertisement

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+
