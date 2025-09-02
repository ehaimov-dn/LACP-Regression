interfaces ndp router-advertisement prefix-advertisement prefix valid-lifetime
------------------------------------------------------------------------------

**Minimum user role:** operator

Value to be placed in the Valid Lifetime in the Prefix Information option, in seconds.
Valid Lifetime is the total time the address is available.
Valid Lifetime must be equal to or greater than the Preferred Lifetime.
The valid lifetime enables sessions to continue for transactions that began before the address became deprecated (end of Preferred Lifetime). 
However, in this time frame the address should no longer be used for new sessions. 
If this time expires without the deprecated address being refreshed, the address becomes invalid and may be assigned to another interface.
To set the signaled prefix information valid-lifetime for Router Advertisement:

**Command syntax: valid-lifetime [valid-lifetime]**

**Command mode:** config

**Hierarchies**

- interfaces ndp router-advertisement prefix-advertisement prefix

**Note**

- valid-lifetime must be equal or greater than the preferred-lifetime

- valid-lifetime value 4294967295 means infinity.

**Parameter table**

+----------------+----------------------------------------------------------------------------------+--------------+---------+
| Parameter      | Description                                                                      | Range        | Default |
+================+==================================================================================+==============+=========+
| valid-lifetime | The value to be placed in the Valid Lifetime in the Prefix Information option.   | 0-4294967295 | 2592000 |
|                | The designated value of all 1's (0xffffffff) represents infinity.                |              |         |
+----------------+----------------------------------------------------------------------------------+--------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# ndp router-advertisement
    dnRouter(cfg-if-ge100-1/1/1-ndp-ra)# prefix-advertisement
    dnRouter(cfg-ge100-1/1/1-ndp-ra-pr-adv)# prefix 2006:18:91::48/127
    dnRouter(cfg-ndp-ra-pr-adv-prefix)# valid-lifetime 3000000


**Removing Configuration**

To revert the valid-lifetime to its default value:
::

    dnRouter(cfg-ndp-ra-pr-adv-prefix)# no valid-lifetime

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+
