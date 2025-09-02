interfaces flap-suppression
---------------------------

**Minimum user role:** operator

Set the flap suppression timer on the bundle interface, to delay the transition of the bundle interface to operational down state by allowing available standby links
to take the place of failed active links.

To configure the flap suppression timer on the bundle interface:

**Command syntax: flap-suppression [flap-suppression]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to bundle interfaces.

- Flap-suppression is not applicable in cases of transitions from operational down state to operational up state; nor from operational up state to operational down state when there are no standby interfaces available at all.

**Parameter table**

+------------------+----------------------------------------------------------------------------------+-------+---------+
| Parameter        | Description                                                                      | Range | Default |
+==================+==================================================================================+=======+=========+
| flap-suppression | Timer (in seconds) to suppress bundle transition to operational down state when  | 0-300 | \-      |
|                  | it does not have any standby links available.                                    |       |         |
+------------------+----------------------------------------------------------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1
    dnRouter(cfg-if-bundle-1)# flap-suppression 5


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-bundle-1)# no flap-suppression

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+
