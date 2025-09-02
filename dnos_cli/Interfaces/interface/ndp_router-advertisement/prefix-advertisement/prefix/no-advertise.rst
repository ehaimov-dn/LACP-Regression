interfaces ndp router-advertisement prefix-advertisement prefix no-advertise
----------------------------------------------------------------------------

**Minimum user role:** operator

Suppress advertisement of this prefix from Router Advertisement prefix information.
Prefix information will not be transmitted even when the prefix belongs to an interface.

**Command syntax: no-advertise**

**Command mode:** config

**Hierarchies**

- interfaces ndp router-advertisement prefix-advertisement prefix

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ndp router-advertisement
    dnRouter(cfg-if-ge100-1/1/1-ndp-ra)# prefix-advertisement
    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# prefix 2006:18:91::48/127
    dnRouter(cfg-ndp-ra-pr-adv-prefix)# no-advertise


**Removing Configuration**

To unset no-advertise:
::

    dnRouter(cfg-ndp-ra-pr-adv-prefix)# no no-advertise

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+
