show ospfv3 interfaces
----------------------

**Minimum user role:** viewer

The show ospfv3 interfaces command displays OSPFv3 interfaces information.


**Command syntax: show ospfv3 interfaces** [interface-name | detail]

**Command mode:** operational



**Note**

.. - interface-name is optional

**Parameter table**

+----------------+-------------------------------------------------------------+----------------------------------------------------+---------------+
| Parameter      | Description                                                 | Values                                             | Default value |
+================+=============================================================+====================================================+===============+
| interface-name | Filters the displayed information for a specified interface | ge<interface speed>-<A>/<B>/<C>                    | all           |
|                |                                                             | ge<interface speed>-<A>/<B>/<C>.<sub-interface id> |               |
|                |                                                             | bundle-<bundle id>                                 |               |
|                |                                                             | bundle-<bundle id>.<sub-interface id>              |               |
|                |                                                             | lo<lo-interface id>                                |               |
+----------------+-------------------------------------------------------------+----------------------------------------------------+---------------+
| detail         | Prints detailed information                                 |                                                    |               |
+----------------+-------------------------------------------------------------+----------------------------------------------------+---------------+

**Example**
::

  dnRouter#  show ospfv3 interfaces

	Interface                                         State     Type                Area
	ge100-0/0/0                                       Up        BROADCAST           0.0.0.0
	ge100-0/0/3.1001                                  Up        POINT-TO-POINT      0.0.0.0
	ge100-0/0/4.10                                    Up        POINT-TO-POINT      0.0.0.0
	lo0                                               Up        LOOPBACK            0.0.0.0

  dnRouter#  show ospfv3 interfaces detail

  ge100-0/0/0 is up
    ifindex 1033, MTU 1500 bytes, BW 100000000 Kbit <UP,BROADCAST,RUNNING,MULTICAST>
      Link Local address fe80::a8c1:abff:fe7e:7eeb, Interface ID 0, Area 0.0.0.0
    MTU mismatch detection:enabled
    Router ID 1.1.1.1, Network type BROADCAST, Cost: 1
    Transmit Delay 1 sec, State DROther, Priority 1
    DR: 5.5.5.5 BDR: 4.4.4.4
    Multicast group memberships: OSPFv3AllRouters
    Timer intervals configured: Hello 10s, Dead 40s, Retransmit 5s
      Hello due in 7.733s
    Neighbor Count is 3, Adjacent neighbor count is 2
    IPsec AH authentication disabled

  ge100-0/0/3.1001 is up
    ifindex 14472, MTU 1500 bytes, BW 100000000 Kbit <UP,BROADCAST,RUNNING,MULTICAST>
      Link Local address fe80::1abe:92ff:fea0:5203, Interface ID 0, Area 0.0.0.0
    MTU mismatch detection:enabled
    Router ID 22.22.22.22, Network type POINT-TO-POINT, Cost: 1
    Transmit Delay 1 sec, State PointToPoint, Priority 1
    No designated router on this network
    No backup designated router on this network
    Multicast group memberships: OSPFv3AllRouters
    Timer intervals configured: Hello 10s, Dead 40s, Retransmit 5s
      Hello due in 1.417s
    Neighbor Count is 1, Adjacent neighbor count is 1

  ge100-0/0/4.10 is up
    ifindex 14472, MTU 1500 bytes, BW 100000000 Kbit <UP,BROADCAST,RUNNING,MULTICAST>
      Link Local address fe80::1abe:92ff:fea0:5203, Area 0.0.0.0
    MTU mismatch detection:enabled
    Router ID 22.22.22.22, Network type POINT-TO-POINT, Cost: 1
    Transmit Delay 1 sec, State PointToPoint, Priority 1
    No designated router on this network
    No backup designated router on this network
    Multicast group memberships: OSPFv3AllRouters
    Timer intervals configured: Hello 10s, Dead 40s, Retransmit 5s
      Hello due in 1.417s
    Neighbor Count is 1, Adjacent neighbor count is 1
    IPsec AH authentication enabled, SPI 256, MD5 algorithm
    BFD: Admin state: Enabled
       Minimum Tx Interval: 300
       Minimum Rx Interval: 300
       BFD Multiplier: 3

  lo0 is up
    ifindex 9217 <UP,BROADCAST,LOOPBACK,RUNNING,NOARP>
      Link Local address fe80::202:3ff:fe04:506, Area 0.0.0.0
    Router ID 100.70.1.124, Network type LOOPBACK, Cost: 0
    No designated router on this network
    No backup designated router on this network
    Multicast group memberships: OSPFv3AllRouters

.. **Help line:** Displays OSPFv3 interfaces information.

**Command History**

+---------+-------------------------------------------+
| Release | Modification                              |
+=========+===========================================+
| 11.6    | Command introduced                        |
+---------+-------------------------------------------+
| 17.0    | Added IPsec AH authentication information |
+---------+-------------------------------------------+
| 19.1    | Added detail parameter                    |
+---------+-------------------------------------------+
| TBD     | Added support for broadcast network type  |
+---------+-------------------------------------------+
