interfaces ndp router-advertisement prefix-advertisement prefix autonomous-config
---------------------------------------------------------------------------------

**Minimum user role:** operator

When set, indicates that this prefix can be used for stateless address configuration.
To configure autonomous-config:

**Command syntax: autonomous-config [autonomous-config]**

**Command mode:** config

**Hierarchies**

- interfaces ndp router-advertisement prefix-advertisement prefix

**Parameter table**

+-------------------+----------------------------------------------------------------------------------+--------------+---------+
| Parameter         | Description                                                                      | Range        | Default |
+===================+==================================================================================+==============+=========+
| autonomous-config | The value to be placed in the Autonomous Flag field in the Prefix Information    | | enabled    | enabled |
|                   | option.                                                                          | | disabled   |         |
+-------------------+----------------------------------------------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ndp router-advertisement
    dnRouter(cfg-if-ge100-1/1/1-ndp-ra)# prefix-advertisement
    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# prefix 2006:18:91::48/127
    dnRouter(cfg-ndp-ra-pr-adv-prefix)# autonomous-config disabled


**Removing Configuration**

To revert the autonomous-config to its default value:
::

    dnRouter(cfg-ndp-ra-pr-adv-prefix)# no autonomous-config

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+
