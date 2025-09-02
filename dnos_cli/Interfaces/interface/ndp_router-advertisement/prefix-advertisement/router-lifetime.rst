interfaces ndp router-advertisement prefix-advertisement router-lifetime
------------------------------------------------------------------------

**Minimum user role:** operator

Value to be placed in the Router Lifetime field of the Router Advertisements sent from the interface, in seconds.
A value of zero indicates that the router is not to be used as a default router.
Router-lifetime default value is 3*(interval max).
To configure the router-lifetime:

**Command syntax: router-lifetime [router-lifetime]**

**Command mode:** config

**Hierarchies**

- interfaces ndp router-advertisement prefix-advertisement

**Note**

- router-lifetime must be >= interval max

**Parameter table**

+-----------------+----------------------------------------------------------------------------------+---------+---------+
| Parameter       | Description                                                                      | Range   | Default |
+=================+==================================================================================+=========+=========+
| router-lifetime | The value to be placed in the Router Lifetime field of Router Advertisements     | 0-65535 | \-      |
|                 | sent from the interface, in seconds.  It MUST be either zero or between          |         |         |
|                 | max-rtr-adv-interval and 9000 seconds.  A value of zero indicates that the       |         |         |
|                 | router is not to be used as a default router.  These limits may be overridden by |         |         |
|                 | specific documents that describe how IPv6 operates over different link layers.   |         |         |
|                 | If this parameter is not configured, the device SHOULD use a value of 3 \*       |         |         |
|                 | max-rtr-adv-interval.                                                            |         |         |
+-----------------+----------------------------------------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ndp router-advertisement
    dnRouter(cfg-if-ge100-1/1/1-ndp-ra)# prefix-advertisement
    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# router-lifetime 2000


**Removing Configuration**

To revert the router-lifetime to its default value:
::

    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# no router-lifetime

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+
