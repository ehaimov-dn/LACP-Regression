show ospfv3 neighbors detail
----------------------------

**Minimum user role:** viewer

To display detailed information on all OSPFv3 Neighbors:



**Command syntax: show ospfv3 neighbors detail**

**Command mode:** operational

**Example**
::

	dnRouter# show ospfv3 neighbors detail

	 Neighbor 100.0.0.7, ge100-0/0/9.200
	    Area 0.0.0.0 via interface ge100-0/0/9.200 (ifindex 14549)
	    His IfIndex: 1 Link-local address: fe80::21d:1ff:fe00:1
	    Neighbor priority is 1, State is Full, for 4d19h4m13s, 0 state changes
	    DR is 0.0.0.0, BDR is 0.0.0.0
	    Options 19 *|*|-|R|-|-|E|V6
	    Hello due in 32.231s
	    DbDesc status: Master SeqNum: 0x396e1500
	    Summary-List: 0 LSAs
	    Request-List: 0 LSAs
	    Retrans-List: 2 LSAs
	      [Router Id:0 Adv:100.0.0.7]
	      [Inter-Prefix Id:2155872256 Adv:100.0.0.7]
	    0 Pending LSAs for DbDesc in Time 0 usecs [thread off]
	    0 Pending LSAs for LSReq in Time 0 usecs [thread off]
	    0 Pending LSAs for LSUpdate in Time 0 usecs [thread off]
	    0 Pending LSAs for LSAck in Time 0 usecs [thread off]
	    BFD: Enabled
	    BFD min-rx: 50 min-tx: 50 multiplier: 3

	 Neighbor 100.0.0.7, ge100-0/0/9.201
	    Area 0.0.0.0 via interface ge100-0/0/9.201 (ifindex 14550)
	    His IfIndex: 1 Link-local address: fe80::21d:1ff:fe00:2
	    Neighbor priority is 1, State is Full, for 4d19h14m13, 0 state changes
	    DR is 0.0.0.0, BDR is 0.0.0.0
	    Options 19 *|*|-|R|-|-|E|V6
	    Hello due in 36.834s
	    DbDesc status: Master SeqNum: 0x396e1500
	    Summary-List: 0 LSAs
	    Request-List: 0 LSAs
	    Retrans-List: 1 LSAs
	      [Router Id:0 Adv:100.0.0.7]
	    0 Pending LSAs for DbDesc in Time 0 usecs [thread off]
	    0 Pending LSAs for LSReq in Time 0 usecs [thread off]
	    0 Pending LSAs for LSUpdate in Time 0 usecs [thread off]
	    0 Pending LSAs for LSAck in Time 0 usecs [thread off]
	    BFD: Enabled
	    BFD min-rx: 50 min-tx: 50 multiplier: 3

	 Neighbor 100.0.0.7, ge100-0/0/9.202
	    Area 0.0.0.0 via interface ge100-0/0/9.202 (ifindex 14551)
	    His IfIndex: 1 Link-local address: fe80::21d:1ff:fe00:3
	    Neighbor priority is 1, State is Full, for 4d19h14m13, 0 state changes
	    DR is 0.0.0.0, BDR is 0.0.0.0
	    Options 19 *|*|-|R|-|-|E|V6
	    Hello due in 34.253s
	    DbDesc status: Master SeqNum: 0x396e1500
	    Summary-List: 0 LSAs
	    Request-List: 0 LSAs
	    Retrans-List: 1 LSAs
	      [Router Id:0 Adv:100.0.0.7]
	    0 Pending LSAs for DbDesc in Time 0 usecs [thread off]
	    0 Pending LSAs for LSReq in Time 0 usecs [thread off]
	    0 Pending LSAs for LSUpdate in Time 0 usecs [thread off]
	    0 Pending LSAs for LSAck in Time 0 usecs [thread off]
	    BFD: Enabled
	    BFD min-rx: 50 min-tx: 50 multiplier: 3

	 Neighbor 4.4.4.4, ge100-0/0/0
	    Area 0.0.0.0 via interface ge100-0/0/0 (ifindex 1033)
	    His IfIndex: 4 Link-local address: fe80::a8c1:abff:fe69:cf03
	    Neighbor priority is 1, State is Full, for 3m57s, 5 state changes
	    DR is 5.5.5.5, BDR is 4.4.4.4
	    Options 19 *|*|-|R|-|-|E|V6
	    Hello due in 39.211s
	    DbDesc status: Slave SeqNum: 0x94064912
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

.. **Help line:** Displays OSPFv3 neighbors detailed information

**Command History**

+---------+----------------------------------------------------------------+
| Release | Modification                                                   |
+=========+================================================================+
| 11.6    | Command introduced                                             |
+---------+----------------------------------------------------------------+
| 15.0    | Updated display of duration and added counter of state changes |
+---------+----------------------------------------------------------------+
| 19.3    | Removed all parameter                                          |
+---------+----------------------------------------------------------------+
| TBD     | Added support for broadcast network type                       |
+---------+----------------------------------------------------------------+

