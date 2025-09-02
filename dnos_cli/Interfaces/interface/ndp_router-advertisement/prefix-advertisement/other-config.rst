interfaces ndp router-advertisement prefix-advertisement other-config
---------------------------------------------------------------------

**Minimum user role:** operator

Once enabled, set the O flag in router-advertisement advertisements.
O flag set indicates receiving neighbors that other information is available via stateful protocol (DHCPv6) such as DNS-related information.
To enable other-config:

**Command syntax: other-config [other-config]**

**Command mode:** config

**Hierarchies**

- interfaces ndp router-advertisement prefix-advertisement

**Note**

- Setting O flag is redundant if M flag is set

**Parameter table**

+--------------+----------------------------------------------------------------------------------+--------------+----------+
| Parameter    | Description                                                                      | Range        | Default  |
+==============+==================================================================================+==============+==========+
| other-config | The value to be placed in the 'Other configuration' flag field in the Router     | | enabled    | disabled |
|              | Advertisement.                                                                   | | disabled   |          |
+--------------+----------------------------------------------------------------------------------+--------------+----------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ndp router-advertisement
    dnRouter(cfg-if-ge100-1/1/1-ndp-ra)# prefix-advertisement
    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# other-config enabled


**Removing Configuration**

To revert the other-config to its default value:
::

    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# no other-config

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+
