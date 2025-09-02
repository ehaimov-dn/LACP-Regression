show ospfv3 neighbors
---------------------

**Minimum user role:** viewer

The show ospf neighbors command displays OSPFv3 neighbors information. You can display details on the neighbors and you can filter by interface.

To display neighbor information, use the following command:

**Command syntax: show ospfv3 neighbors** { address [neighbor-address] \| interface [interface-name] detail }

**Command mode:** operational



**Note**

- The "Uptime" in the output displays the amount of time the OSPFv3 neighbor was in the current state.

.. - Table view order: The show ospfv3 neighbors table view should be ordered by neighbor id in ascend

**Parameter table**

+------------------+-------------------------------------------------------------+----------------------------------------------------+---------------+
| Parameter        | Description                                                 | Range                                              | Default       |
+==================+=============================================================+====================================================+===============+
| No parameter     | Displays all the neighbors                                  |                                                    | \-            |
+------------------+-------------------------------------------------------------+----------------------------------------------------+---------------+
| neighbor-address | The neighbor's router ID to filter the information          | A.B.C.D                                            | \-            |
+------------------+-------------------------------------------------------------+----------------------------------------------------+---------------+
| interface-name   | Filters the displayed information for a specified interface | ge<interface speed>-<A>/<B>/<C>                    | \-            |
|                  |                                                             | ge<interface speed>-<A>/<B>/<C>.<sub-interface id> |               |
|                  |                                                             | bundle-<bundle id>                                 |               |
|                  |                                                             | bundle-<bundle id>.<sub-interface id>              |               |
+------------------+-------------------------------------------------------------+----------------------------------------------------+---------------+
| detail           | Prints detailed information                                 |                                                    |               |
+------------------+-------------------------------------------------------------+----------------------------------------------------+---------------+

**Example**
::

    dnRouter# show ospfv3 neighbors


    Neighbor ID     Pri State            Dead Time Address                             Interface                                                  Uptime RXmtL RqstL DBsmL
    2.2.2.2           1 Twoway/DROther     37.068s fe80::a8c1:abff:fef6:8ed4           ge100-0/0/0 fe80::a8c1:abff:fe7e:7eeb                        8m3s     0     0     0
    4.4.4.4           1 Full/Backup        31.118s fe80::a8c1:abff:fe69:cf03           ge100-0/0/0 fe80::a8c1:abff:fe7e:7eeb                        8m3s     0     0     0
    5.5.5.5           1 Full/DR            37.073s fe80::18a7:3ff:feff:1               ge100-0/0/0 fe80::a8c1:abff:fe7e:7eeb                       7m58s     0     0     0
    1.2.3.4           1 Full               39.045s fe80::18d0:93ff:fe7b:5b25           ge100-0/0/1 fe80::5c69:6bff:fe3e:55ae                       2m34s     0     0     0
    4.3.2.1           1 Full               30.004s fe80::1cb1:f7ff:fee1:2392           ge100-0/0/2 fe80::e068:3bff:fe81:4e2a                      03m08s     0     0     0


    dnRouter# show ospfv3 neighbors address 1.2.3.4

    Neighbor ID     Pri State      Dead Time      Address                             Interface                                           Uptime      RXmtL RqstL DBsmL
    1.2.3.4           1 Full         35.972s      fe80::18d0:93ff:fe7b:5b25           ge100-0/0/1 fe80::5c69:6bff:fe3e:55ae               03m18s          0     0     0


    dnRouter# show ospfv3 neighbors interface ge100-0/0/1

    Neighbor ID     Pri State      Dead Time      Address                             Interface                                           Uptime      RXmtL RqstL DBsmL
    1.2.3.4           1 Full         36.293s      fe80::18d0:93ff:fe7b:5b25           ge100-0/0/1 fe80::5c69:6bff:fe3e:55ae               04m09s          0     0     0


    dnRouter# show ospfv3 neighbors interface ge100-0/0/1 detail

    Neighbor 1.2.3.4, ge100-0/0/1
        Area 0.0.0.0 via interface ge100-0/0/1 (ifindex 7)
        His IfIndex: 7 Link-local address: fe80::5c69:6bff:fe3e:55ae
        Neighbor priority is 1, State is Full, for 5m28s, 0 state changes
        DR is 0.0.0.0, BDR is 0.0.0.0
        Options 19 *|*|-|R|-|-|E|V6
        Hello due in 30.308s
        DbDesc status: Slave SeqNum: 0x95380800
        Summary-List: 0 LSAs
        Request-List: 0 LSAs
        Retrans-List: 0 LSAs
        0 Pending LSAs for DbDesc in Time 0 usecs  [thread off]
        0 Pending LSAs for LSReq in Time 0 usecs  [thread off]
        0 Pending LSAs for LSUpdate in Time 0 usecs  [thread off]
        0 Pending LSAs for LSAck in Time 0 usecs  [thread off]
        BFD: Disabled
        BFD min-rx: 300 min-tx: 300 multiplier: 3


    dnRouter# show ospfv3 neighbors interface ge100-0/0/0 detail

    Neighbor 2.2.2.2, ge100-0/0/0
        Area 0.0.0.0 via interface ge100-0/0/0 (ifindex 1033)
        His IfIndex: 1032 Link-local address: fe80::a8c1:abff:fef6:8ed4
        Neighbor priority is 1, State is Twoway, for 12m3s, 5 state changes
        DR is 5.5.5.5, BDR is 4.4.4.4
        Options 19 *|*|-|R|-|-|E|V6
        Hello due in 37.614s
        DbDesc status: Initial More Master SeqNum: 0x8a30e100
        Summary-List: 0 LSAs
        Request-List: 0 LSAs
        Retrans-List: 0 LSAs
        0 Pending LSAs for DbDesc in Time 0 usecs [thread off]
        0 Pending LSAs for LSReq in Time 0 usecs [thread off]
        0 Pending LSAs for LSUpdate Unicast in Time 0 usecs [thread off]
        0 Pending LSAs for LSUpdate Multicast in Time 0 usecs [thread off]
        0 Pending LSAs for LSUpdate Unicast Priority in Time 0 usecs [thread off]
        0 Pending LSAs for LSAck in Time 0 usecs [thread off]
        BFD: Disabled
        BFD min-rx: 300 min-tx: 300 multiplier: 3

.. **Help line:** Displays OSPFv3 neighbors information

**Command History**

+---------+----------------------------------------------------+
| Release | Modification                                       |
+=========+====================================================+
| 11.6    | Command introduced                                 |
+---------+----------------------------------------------------+
| 15.0    | Added support for added "uptime" in command output |
+---------+----------------------------------------------------+
| TBD     | Added support for broadcast network type           |
+---------+----------------------------------------------------+
