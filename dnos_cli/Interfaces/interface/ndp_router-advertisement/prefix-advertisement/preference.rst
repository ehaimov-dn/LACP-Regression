interfaces ndp router-advertisement prefix-advertisement preference
-------------------------------------------------------------------

**Minimum user role:** operator

Preference allows a neighbor to prefer a given router router-advertisements.
To configure the local router advertised preference value:

**Command syntax: preference [preference]**

**Command mode:** config

**Hierarchies**

- interfaces ndp router-advertisement prefix-advertisement

**Parameter table**

+------------+----------------------------------------------------------------------------------+------------+---------+
| Parameter  | Description                                                                      | Range      | Default |
+============+==================================================================================+============+=========+
| preference | Default router preferences and preferences for more-specific routes. 2-bit       | | medium   | medium  |
|            | signed integer.  Indicates whether to prefer this router over other default      | | high     |         |
|            | routers.  If the Router Lifetime is zero, the preference value MUST be set to    | | low      |         |
|            | (00) by the sender and MUST be ignored by the receiver.  If the Reserved (10)    |            |         |
|            | value is received, the receiver MUST treat the value as if it were (00).         |            |         |
+------------+----------------------------------------------------------------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ndp router-advertisement
    dnRouter(cfg-if-ge100-1/1/1-ndp-ra)# prefix-advertisement
    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# preference high


**Removing Configuration**

To revert the preference to its default value:
::

    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# no preference

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+
