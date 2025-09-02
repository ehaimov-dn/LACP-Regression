show bgp labels vrf
-------------------

**Minimum user role:** viewer

To display locally allocated vrf instance labels:

**Command syntax: show bgp labels vrf all**

**Command mode:** operational


..
	**Internal Note**

**Example**
::

	dnRouter# # show bgp labels vrf all

	|      VRF-Name      |     VRF-ID     |  Route-Distinguisher |  VRF Local Label |
	---------------------------------------------------------------------------------------------------------
	|A6                  |               1|     100.18.18.18:1601|           1040385|
	|B6                  |               2|     100.18.18.18:1602|           1040386|

**Command History**

+---------+-----------------------------------------------------------------------+
| Release | Modification                                                          |
+=========+=======================================================================+
| TBD     | Command introduced                                                    |
+---------+-----------------------------------------------------------------------+
