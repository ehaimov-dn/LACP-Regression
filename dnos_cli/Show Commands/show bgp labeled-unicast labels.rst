show bgp labeled-unicast labels
-------------------------------

**Minimum user role:** viewer

To display bgp labeled-unicast mpls routes:

**Command syntax: show bgp [address-family] labeled-unicast labels**

**Command mode:** operational


..
	**Internal Note**


**Parameter table**

+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------+
| Parameter          | Description                                                                                                                                                       | Range                       |
+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------+
| address-family     | Display routing information for a specific address-family (AFI)                                                                                                   | IPv4                        |
|                    |                                                                                                                                                                   | IPv6                        |
+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------+

**Example**
::

	dnRouter# # show bgp ipv4 labeled-unicast labels

	BGP IPv4 Labeled-Unicast, local router ID is 100.0.18.18
	Status codes: s - suppressed, d - damped, h - history, * - valid, > - best, = - multipath, a - alternate-path, P - Pending
				i - internal, r - RIB-failure, S - Stale, SL - LLGR Stale, R - Removed, L - over-limit, x - best-external
	Origin codes: i - IGP, e - EGP, ? - incomplete
	Next hop codes: v - Via another VRF
	RPKI validation codes: V - valid, I - invalid, N - not-found, U - unverified

	|       Network      | Lb. In/Lb. out |                Next hop                |Metric|  LocPref | Weight |   Path   |
	----------------------------------------------------------------------------------------------------------------------------
	U*>i|5.12.126.0/32       |     27306/57041| 100.0.12.12                            |      |       100|       0|   51226 i|
	U*>i|5.12.126.1/32       |     27307/57042| 100.0.12.12                            |      |       100|       0|   51226 i|
	U*>i|5.12.126.2/32       |     27308/57043| 100.0.12.12                            |      |       100|       0|   51226 i|

**Command History**

+---------+-----------------------------------------------------------------------+
| Release | Modification                                                          |
+=========+=======================================================================+
| TBD     | Command introduced                                                    |
+---------+-----------------------------------------------------------------------+