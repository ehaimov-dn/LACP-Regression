interfaces ndp router-advertisement prefix-advertisement advertise-mtu
----------------------------------------------------------------------

**Minimum user role:** operator

When enabled, send the MTU option under Router Advertisement.
The MTU option will include information about interface ipv6 mtu value.
To enable advertise-mtu:

**Command syntax: advertise-mtu [advertise-mtu]**

**Command mode:** config

**Hierarchies**

- interfaces ndp router-advertisement prefix-advertisement

**Parameter table**

+---------------+----------------------------------------------------------------------------------+--------------+----------+
| Parameter     | Description                                                                      | Range        | Default  |
+===============+==================================================================================+==============+==========+
| advertise-mtu | Configure if to include MTU option in transmitted router advertisements. The MTU | | enabled    | disabled |
|               | option is used in Router Advertisement messages to ensure that all nodes on a    | | disabled   |          |
|               | link use the same MTU value in those cases where the link MTU is not well known. |              |          |
+---------------+----------------------------------------------------------------------------------+--------------+----------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ndp router-advertisement
    dnRouter(cfg-if-ge100-1/1/1-ndp-ra)# prefix-advertisement
    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# advertise-mtu enabled


**Removing Configuration**

To revert the advertise-mtu to its default value:
::

    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# no advertise-mtu

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+
