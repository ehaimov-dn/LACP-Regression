show bgp ext-community
-----------------------

**Minimum user role:** viewer

To display routes matching the extended community attribute:

**Command syntax: show bgp** {instance vrf [vrf-name]} [address-family] [sub-address-family] **ext-community regex [regex]**

**Command mode:** operational


..
	**Internal Note**

	- use vrf to display information for a non-default vrf

	- for non-default instance vrf support only "unicast" sub-address-family

	- address-family sub-address-family are optional, if not specified display for all sub-address-families

	- regex is required to specify the extended community pattern to match

**Parameter table**

+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------+
| Parameter          | Description                                                                                                                                             | Range                       |
+====================+=========================================================================================================================================================+=============================+
| vrf-name           | Display routing information for a non-default VRF                                                                                                       | 1..255 characters           |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------+
| address-family     | Display routing information for a specific address-family (AFI)                                                                                         | IPv4                        |
|                    |                                                                                                                                                         | IPv6                        |
|                    |                                                                                                                                                         | Link-state                  |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------+
| sub-address-family | Display routing information for a specific subsequent address-family (SAFI). Only unicast is supported with a non-default VRF.                          | unicast                     |
|                    | N/A for link-state address-family                                                                                                                       | multicast                   |
|                    |                                                                                                                                                         | vpn                         |
|                    |                                                                                                                                                         | flowspec                    |
|                    |                                                                                                                                                         | rt-constrains               |
|                    |                                                                                                                                                         | l2vpn evpn                  |
|                    |                                                                                                                                                         | labeled-unicast             |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------+
| regex              | A regular expression defining a search pattern to match extended community attributes                                                                   | \-                          |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------+

**Example**
::

	dnRouter# # show bgp ipv4 vpn ext-community regex "RT:1.*:.*"

    BGP IPv4 Vpn, local router ID is 100.0.18.18
    Status codes: s - suppressed, d - damped, h - history, * - valid, > - best, = - multipath, a - alternate-path, P - Pending
                i - internal, r - RIB-failure, S - Stale, SL - LLGR Stale, R - Removed, L - over-limit, x - best-external
    Origin codes: i - IGP, e - EGP, ? - incomplete
    Next hop codes: v - Via another VRF
    RPKI validation codes: V - valid, I - invalid, N - not-found, U - unverified


    Route Distinguisher: 100.0.12.12:1

        |       Network      |                Next hop                |Metric|  LocPref | Weight |   Path   |
    ---------------------------------------------------------------------------------------------------------
    U*>i|12.0.0.0/32         | 100.0.12.12                            |      |       100|       0|  120001 i|
    U*>i|12.0.0.1/32         | 100.0.12.12                            |      |       100|       0|  120001 i|

.. **Help line:** displays routes matching the extended community attribute

**Command History**

+---------+------------------------------------------------------------------------------------------+
| Release | Modification                                                                             |
+=========+==========================================================================================+
| TBD     | Command introduced                                                                       |
+---------+------------------------------------------------------------------------------------------+ 