show interfaces dhcpv6
----------------------

**Minimum user role:** viewer

The command displays DHCPv6 IP addresses for a specific interface.

**Command syntax:show interfaces dhcpv6** [interface-name]

**Command mode:** operational



**Note**

- The command is applicable to the following interface types:

	- mgmt0

	- mgmt-ncc

	- Physical

	- Physical VLAN

	- Bundle

	- Bundle VLAN.


- Specify an interface to filter the displayed information to that interface.

**Parameter table**

+----------------+-----------------------------------------------------------+-----------------------------------------------------------------------------+-----------+
| Parameter      | Description                                               | Range                                                                       | Default   |
+================+===========================================================+=============================================================================+===========+
| interface-name | Filters the displayed information to a specific interface | mgmt0, mgmt-ncc-0, mgmt-ncc-1, geX-X/X/X, geX-X/X/X.Y, bundle-X, bundle-X.Y | \-        |
+----------------+-----------------------------------------------------------+-----------------------------------------------------------------------------+-----------+

**Example**
::

	dnRouter# show interfaces dhcpv6

	| Interface            | DHCPv6 address               | DHCPv6 Server IP         | DHCPv6 Server DUID           | Lease expires       |
	+----------------------+------------------------------+--------------------------+------------------------------+---------------------+
	| bundle-328.999       | 2011:999::cab1               | fe80::a00:27ff:fed4:10bb | 000100012d9d975b52540018528c | 2024-04-03 07:28:44 |
	| ge100-0/0/2          | 9000::3e                     | fe80::a00:27ff:fed4:10bb | 000100012d9d975b52540018528c | 2024-04-03 07:29:51 |
	| ge100-0/0/2.321      | 5001::f197                   | fe80::a00:27ff:fed4:10bb | 000100012d9d975b52540018528c | 2024-04-03 07:29:57 |
	| ge100-0/0/3          | 6001::cbf0                   | fe80::a00:27ff:fed4:10bb | 000100012d9d975b52540018528c | 2024-04-03 07:29:17 |
	| mgmt0                | 2001:db8:0:1::254            | fe80::b06:13fa:fcb3:10ca | 0001000129f2c2c516a86786a6cd | 2024-04-03 07:29:37 |
	| mgmt-ncc-0           | 2192::cfda                   | fe80::b06:13fa:fcb3:10ca | 0001000129f2c2c516a86786a6cd | 2024-04-03 07:21:13 |
  

	dnRouter# show interfaces dhcpv6 mgmt0

	Interface mgmt0
		Listening on: 84:4d:c0:7f:92:fc
		Bound IPv6 Address: 2001:db8:0:1::254/128 (DHCPv6)
		Bound IPv6 Local Address: fe80::864d:c0ff:fe7f:92fc/64
		IPv6 DHCP: enabled
		DHCPv6 addresses:
			DHCPv6 Address: 2001:db8:0:1::254
				Client MAC: 84:4d:c0:7f:92:fc, DUID: 000100011c39cf88080027fe8f95
				From Server: fe80::b06:13fa:fcb3:10ca, DUID: 0001000129f2c2c516a86786a6cd
				Lease starts:  2024-04-03 07:19:37
				Lease expires: 2024-04-03 07:29:37
				DHCPv6 options:
					N/A


	dnRouter# show int dhcpv6 ge100-0/0/2.321

	Interface ge100-0/0/2.321
		Listening on: e8:c5:7a:66:d0:71
		Bound IPv6 Address: 5001::f197/128 (DHCPv6)
		Bound IPv6 Local Address: fe80::eac5:7aff:fe66:d071/64
		IPv6 DHCP: enabled

		DHCPv6 addresses:
			DHCPv6 Address: 5001::f197
				Client MAC: e8:c5:7a:66:d0:71, DUID: 000100011c39cf88080027fe8f95
				From Server: fe80::a00:27ff:fed4:10bb, DUID: 000100012d9d975b52540018528c
				Lease starts:  2024-04-03 06:37:26
				Lease expires: 2024-04-03 07:29:57
				DHCPv6 options:
					N/A


.. **Help line:** show interfaces dhcpv6

**Command History**

+---------+-------------------------------------------------+
| Release | Modification                                    |
+=========+=================================================+
| 13.0    | Command introduced                              |
+---------+-------------------------------------------------+
| 19.1    | Extended support for in-band network interfaces |
+---------+-------------------------------------------------+