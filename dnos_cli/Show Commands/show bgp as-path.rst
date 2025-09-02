show bgp as-path
----------------

**Minimum user role:** viewer

To display routes matching the as-path attribute:

**Command syntax: show bgp** instance vrf [vrf-name] [address-family] [sub-address-family] **as-path regex [regex]**

**Command mode:** operational


..
	**Internal Note**

	- instance address-family and sub-address-family are optional, if not specified display for all sub-address-families and default vrf

**Parameter table**

+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------+
| Parameter          | Description                                                                                                                                             | Range                       |
+====================+=========================================================================================================================================================+=============================+
| vrf-name           | Display routing information for a non-default VRF                                                                                                       | 1..255 characters           |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------+
| address-family     | Display routing information for a specific address-family (AFI)                                                                                         | IPv4                        |
|                    |                                                                                                                                                         | IPv6                        |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------+
| sub-address-family | Display routing information for a specific subsequent address-family (SAFI). Only unicast is supported with a non-default VRF.                          | unicast                     |
|                    | N/A for link-state address-family                                                                                                                       | labeled-unicast             |
|                    |                                                                                                                                                         | vpn                         |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------+
| regex              | A regular expression defining a search pattern to match communities attribute in                                                                        | \-                          |
|                    | BGP updates.                                                                                                                                            |                             |
|                    | See Regular Expressions.                                                                                                                                |                             |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------+

**Example**
::

	dnRouter# show bgp as-path regex "5122*"

    BGP IPv4 Unicast, local router ID is 100.0.18.18
    Status codes: s - suppressed, d - damped, h - history, * - valid, > - best, = - multipath, a - alternate-path, P - Pending
                i - internal, r - RIB-failure, S - Stale, SL - LLGR Stale, R - Removed, L - over-limit, x - best-external
    Origin codes: i - IGP, e - EGP, ? - incomplete
    Next hop codes: v - Via another VRF
    RPKI validation codes: V - valid, I - invalid, N - not-found, U - unverified

        |       Network      |                Next hop                |Metric|  LocPref | Weight |   Path   |
    ---------------------------------------------------------------------------------------------------------
    U*>i|5.112.101.0/32      | 100.0.12.12                            |      |       100|       0|   51201 i|
    U*>i|5.112.101.1/32      | 100.0.12.12                            |      |       100|       0|   51201 i|
    
.. **Help line:** displays routes matching the as-path attribute


**Command History**

+---------+------------------------------------------------------------------------------------------+
| Release | Modification                                                                             |
+=========+==========================================================================================+
| TBD     | Command introduced                                                                       |
+---------+------------------------------------------------------------------------------------------+
