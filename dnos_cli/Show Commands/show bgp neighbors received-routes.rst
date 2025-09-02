show bgp neighbors received-routes
----------------------------------

**Minimum user role:** viewer

The following command displays the routes received from a BGP neighbor:

**Command syntax: show bgp** {instance vrf [vrf-name]} [address-family] [sub-address-family] **neighbors neighbor-address received-routes**

**Command mode:** operational


..
	**Internal Note**

	- use vrf to display information for a non-default vrf

	- for non-default instance vrf support only "unicast" sub-address-family

**Parameter table**

+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
|      Parameter     |                                                                                  Description                                                                                  |                               Range                                        |
+====================+===============================================================================================================================================================================+============================================================================+
| vrf-name           | Display routing information for a non-default VRF                                                                                                                             | 1..255 characters                                                          |
+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| address-family     | Display routing information for a specific address-family (AFI)                                                                                                               | IPv4 IPv6 Link-State                                                       |
+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| sub-address-family | Display routing information for a specific subsequent address-family (SAFI). Only unicast is supported with a non-default VRF. N/A for link-state address-family              | unicast labeled-unicast multicast vpn flowspec rt-constrains 'l2vpn evpn'  |
+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| neighbor-address   | Neighbor address                                                                                                                                                              | A.B.C.D                                                                    |
|                    |                                                                                                                                                                               | xx:xx::xx:xx                                                               |
+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+


**Example**
::

    dnRouter# show bgp neighbors 100.0.61.61 received-routes


    BGP IPv4 Unicast, local router ID is 100.0.18.18
    Status codes: s - suppressed, d - damped, h - history, * - valid, > - best, =  -multipath, a - alternate-path,
                i - internal, r - RIB-failure, S - Stale, SL - LLGR Stale, R - Removed, L - over-limit, x - best-external
    Origin codes: i - IGP, e - EGP, ? - incomplete
    Next hop codes: v - Via another VRF
    RPKI validation codes: V - valid, I - invalid, N - not-found, U - unverified

        |       Network      |    Next hop    |Metric|  LocPref | Weight |   Path   |
    -----------------------------------------------------------------------------------
    U*>i|7.12.101.0/32       | 100.0.12.12    |      |      1000|       0|   71201 i|
    U*>i|7.12.101.1/32       | 100.0.12.12    |      |      1000|       0|   71201 i|
    U*>i|7.12.101.2/32       | 100.0.12.12    |      |      1000|       0|   71201 i|
    U*>i|7.12.101.3/32       | 100.0.12.12    |      |      1000|       0|   71201 i|
    U*>i|7.12.101.4/32       | 100.0.12.12    |      |      1000|       0|   71201 i|



.. **Help line:** show bgp ipv4 routes

**Command History**

+---------+-----------------------------------------------------------------------------------------+
| Release | Modification                                                                            |
+=========+=========================================================================================+
| 6.0     | Command introduced                                                                      |
+---------+-----------------------------------------------------------------------------------------+
| 16.1    | Added support for IPv4 Multicast SAFI                                                   |
+---------+-----------------------------------------------------------------------------------------+
| TBD     | Added support for labeled-unicast SAFI                                                  |
+---------+-----------------------------------------------------------------------------------------+

