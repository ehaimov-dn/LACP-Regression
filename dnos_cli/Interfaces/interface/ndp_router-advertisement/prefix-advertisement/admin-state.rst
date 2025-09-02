interfaces ndp router-advertisement prefix-advertisement admin-state
--------------------------------------------------------------------

**Minimum user role:** operator

Once enabled, the router will send router-advertisement icmpv6 messages over the interface.
Router-advertisement messages will be sent over the interface periodically, and upon reception of valid Router solicitation messages.
To enable router-advertisement prefix-advertisement:

**Command syntax: admin-state [admin-state]**

**Command mode:** config

**Hierarchies**

- interfaces ndp router-advertisement prefix-advertisement

**Note**

- The interface must be enabled for IPv6, either with LLA only or with global IPv6 address configured

- When prefix-advertisement admin-state is enabled, the router-advertisement install-default-route must be disabled.

**Parameter table**

+-------------+----------------------------------------------------------------------------------+--------------+----------+
| Parameter   | Description                                                                      | Range        | Default  |
+=============+==================================================================================+==============+==========+
| admin-state | Indicating whether or not the router sends periodic Router Advertisements and    | | enabled    | disabled |
|             | responds to Router Solicitations.                                                | | disabled   |          |
+-------------+----------------------------------------------------------------------------------+--------------+----------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ndp router-advertisement
    dnRouter(cfg-if-ge100-1/1/1-ndp-ra)# prefix-advertisement
    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)#


**Removing Configuration**

To revert the admin-state to its default value:
::

    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# no admin-state

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+
