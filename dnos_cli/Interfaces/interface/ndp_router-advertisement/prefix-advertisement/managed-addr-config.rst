interfaces ndp router-advertisement prefix-advertisement managed-addr-config
----------------------------------------------------------------------------

**Minimum user role:** operator

Once enabled, set the M flag in router-advertisement advertisements.
M flag set indicates receiving neighbors that addresses are available via DHCPv6 and stateful configuration should be used.
To enable managed-addr-config:

**Command syntax: managed-addr-config [managed-addr-config]**

**Command mode:** config

**Hierarchies**

- interfaces ndp router-advertisement prefix-advertisement

**Parameter table**

+---------------------+----------------------------------------------------------------------------------+--------------+----------+
| Parameter           | Description                                                                      | Range        | Default  |
+=====================+==================================================================================+==============+==========+
| managed-addr-config | The value to be placed in the 'Managed address configuration' flag field in the  | | enabled    | disabled |
|                     | Router Advertisement.                                                            | | disabled   |          |
+---------------------+----------------------------------------------------------------------------------+--------------+----------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ndp router-advertisement
    dnRouter(cfg-if-ge100-1/1/1-ndp-ra)# prefix-advertisement
    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# managed-addr-config enabled


**Removing Configuration**

To revert the managed-addr-config to its default value:
::

    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# no managed-addr-config

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+
