interfaces ndp router-advertisement prefix-advertisement prefix preferred-lifetime
----------------------------------------------------------------------------------

**Minimum user role:** operator

Value to be placed in the Preferred Lifetime in the Prefix Information option, in seconds.
Preferred Lifetime is the length of time during which the address can be used freely as both a source and a destination address for traffic exchanges with other devices.
Preferred Lifetime must be equal to or less than the Valid Lifetime.
If this time expires without the address being refreshed, the address becomes deprecated and should be replaced with a new, preferred address. New sessions cannot use the address obtained by this prefix.
To set the signaled prefix information Preferred-lifetime for Router Advertisement:

**Command syntax: preferred-lifetime [preferred-lifetime]**

**Command mode:** config

**Hierarchies**

- interfaces ndp router-advertisement prefix-advertisement prefix

**Note**

- valid-lifetime must be equal to or greater than the preferred-lifetime.

- preferred-lifetime value 4294967295 means infinity.

**Parameter table**

+--------------------+----------------------------------------------------------------------------------+--------------+---------+
| Parameter          | Description                                                                      | Range        | Default |
+====================+==================================================================================+==============+=========+
| preferred-lifetime | The value to be placed in the Preferred Lifetime in the Prefix Information       | 0-4294967295 | 604800  |
|                    | option. The designated value of all 1's (0xffffffff) represents infinity.        |              |         |
+--------------------+----------------------------------------------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ndp router-advertisement
    dnRouter(cfg-if-ge100-1/1/1-ndp-ra)# prefix-advertisement
    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# prefix 2006:18:91::48/127
    dnRouter(cfg-ndp-ra-pr-adv-prefix)# preferred-lifetime 2500000


**Removing Configuration**

To revert the preferred-lifetime to its default value:
::

    dnRouter(cfg-ndp-ra-pr-adv-prefix)# no preferred-lifetime

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+
