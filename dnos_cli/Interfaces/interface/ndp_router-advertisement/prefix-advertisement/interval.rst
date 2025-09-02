interfaces ndp router-advertisement prefix-advertisement interval max
---------------------------------------------------------------------

**Minimum user role:** operator

To configure the interval for periodic router-advertisement transmissions:
- max - The maximum time, in seconds, allowed between sending unsolicited Multicast Router Advertisements from the interface. The default is 600 seconds.
- min - The minimum time, in seconds, allowed between sending unsolicited Multicast Router Advertisements from the interface. For max >= 9sec, the default is 0.33max, otherwise thr defualt is 0.75max.

**Command syntax: interval max [interval-max]** min [interval-min]

**Command mode:** config

**Hierarchies**

- interfaces ndp router-advertisement prefix-advertisement

**Note**

- min must be <= 0.75*max.

**Parameter table**

+--------------+----------------------------------------------------------------------------------+---------+---------+
| Parameter    | Description                                                                      | Range   | Default |
+==============+==================================================================================+=========+=========+
| interval-max | The maximum time allowed between sending unsolicited multicast Router            | 4-65535 | 600     |
|              | Advertisements from the interface.                                               |         |         |
+--------------+----------------------------------------------------------------------------------+---------+---------+
| interval-min | The minimum time allowed between sending unsolicited multicast Router            | 3-1350  | \-      |
|              | Advertisements from the interface.  The default value to be used operationally   |         |         |
|              | if this leaf is not configured is determined as follows:  - if                   |         |         |
|              | max-rtr-adv-interval >= 9 seconds, the default value is 0.33 \*                  |         |         |
|              | max-rtr-adv-interval;  - otherwise, it is 0.75 \* max-rtr-adv-interval.          |         |         |
+--------------+----------------------------------------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ndp router-advertisement
    dnRouter(cfg-if-ge100-1/1/1-ndp-ra)# prefix-advertisement
    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# interval max 1500
    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# interval max 1500 min 1000


**Removing Configuration**

To revert the interval max to its default value:
::

    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# no interval max

To revert the interval min to its default value:
::

    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# no interval max 1500 min

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+
