interfaces baud-rate
--------------------

**Minimum user role:** operator

Sets the baud rate of the console interface.

**Command syntax: baud-rate [baud-rate]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Console

**Parameter table**

+-----------+----------------------------------+------------+---------+
| Parameter | Description                      | Range      | Default |
+===========+==================================+============+=========+
| baud-rate | Set console interface baud-rate. | | 115200   | 115200  |
|           |                                  | | 38400    |         |
|           |                                  | | 9600     |         |
+-----------+----------------------------------+------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# console-ncc-0/0
    dnRouter(cfg-if-console-ncc-0/0)# baud-rate 115200


**Removing Configuration**

To revert to the default state:
::

    dnRouter(cfg-if-console-ncc-0/0)# no baud-rate

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.1.3  | Command introduced |
+---------+--------------------+
