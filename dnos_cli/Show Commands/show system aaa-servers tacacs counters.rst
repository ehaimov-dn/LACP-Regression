show system aaa-servers tacacs counters
---------------------------------------

**Minimum user role:** viewer

Displays the counters for the TACACS+ servers. If you specify a server ip-address, the output result is filtered to show only the information for the requested server.

**Command syntax: show system aaa-servers tacacs counters** [ip-address]

**Command mode:** operational

..
	**Internal Note**

	- If ip-address parameter is not specified, information for all AAA servers is presented
	- Servers are displayed in the order of their priority from the lowest to the highest
	- In case of multiple servers with the same ip-address, there will be multiple entries for each server with the same ip-address

**Parameter table**

+------------+---------------------------------------------------------------------------------+----------+
| Parameter  | Description                                                                     | Range    |
+============+=================================================================================+==========+
| ip-address | Filters the display by the IPv4 or IPv6 address of the specific TACACS+ server. | A.B.C.D  |
|            |                                                                                 | x:x::x:x |
+------------+---------------------------------------------------------------------------------+----------+

For every server, the following information is displayed:

+-------------------------+------------------------------------------------------------------------------------+----------------+
| Field                   | Description                                                                        | Range          |
+=========================+====================================================================================+================+
| IP Address              | The IPv4 or IPv6 address of the AAA server.                                        | A.B.C.D        |
|                         | See system aaa-server tacacs server.                                               | x:x::x:x       |
+-------------------------+------------------------------------------------------------------------------------+----------------+
| Priority                | The configured priority of the TACACS+ server.                                     | 1..255         |
+-------------------------+------------------------------------------------------------------------------------+----------------+
| Messages Sent           | Total number of messages sent to the TACACS server.                                | 64-bit counter |
+-------------------------+------------------------------------------------------------------------------------+----------------+
| Messages Received       | Total number of messages received by the TACACS server.                            | 64-bit counter |
+-------------------------+------------------------------------------------------------------------------------+----------------+
| Received Errors         | Total number of errors encountered while receiving or processing received messages.| 64-bit counter |
+-------------------------+------------------------------------------------------------------------------------+----------------+
| Auth Requests           | Total number of authentication requests sent to the TACACS server.                 | 64-bit counter |
+-------------------------+------------------------------------------------------------------------------------+----------------+
| Auth Accepts            | Total number of authentication accepts received by the TACACS server.              | 64-bit counter |
+-------------------------+------------------------------------------------------------------------------------+----------------+
| Auth Rejects            | Total number of authentication rejects received by the TACACS server.              | 64-bit counter |
+-------------------------+------------------------------------------------------------------------------------+----------------+
| Last Cleared            | When the counters for the interface were cleared.                                  | Time format    |
|                         |                                                                                    | Never          |
+-------------------------+------------------------------------------------------------------------------------+----------------+

In case counters are queried for one specific server, the following Additional information is displayed:

+--------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------+
| Field                    | Description                                                                                            | Range                         |
+==========================+========================================================================================================+===============================+
| VRF                      | The TACACS server management type.                                                                     | default         - in-band     |
|                          |                                                                                                        | non-default-vrf - out-of-band |
|                          |                                                                                                        | mgmt0           - out-of-band |
+--------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------+
| Port                     | The TCP port number used when making connections to the AAA server.                                    | 0..65535                      |
+--------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------+

**Example**
::

	dnRouter# show system aaa-servers tacacs counters

	| IP           | Priority | Messages | Messages | Error    | Authentication | Authentication | Authentication | Authentication | Authentication | Last             |
	| Address      |          | Sent     | Recived  | Received | Requests       | Accept         | Reject         | Errors         | Timeouts       | Cleared          |
	+--------------+----------+----------+----------+----------+----------------+----------------+----------------+----------------+----------------+------------------+
	| 1.1.1.1      | 1        | 500      | 490      | 2        | 250            | 245            | 2              | 5              | 1              | never            |
	+--------------+----------+----------+----------+----------+----------------+----------------+----------------|----------------+----------------+------------------+
	| 192.168.2.2  | 2        | 800      | 780      | 5        | 300            | 290            | 5              | 6              | 22             | 2 days, 12:34:56 |
	+--------------+----------+----------+----------+----------+----------------+----------------+----------------|----------------+----------------+------------------+
	| 2001:0db8::1 | 3        | 600      | 590      | 3        | 150            | 145            | 2              | 0              | 1              | 0 days, 12:34:00 |
	+--------------+----------+----------+----------+----------+----------------+----------------+----------------|----------------+----------------+------------------+

	dnRouter# show system aaa-servers tacacs counters 1.1.1.1

	TACACS Server IP Address 1.1.1.1, Priority 1, VRF default, Port 49

	counters:
		Messages Sent:                      500
		Messages Received:                  490
		Received Errors:                    2
		Authentication Requests:            250
		Authentication Accepts:             245
		Authentication Rejects:             2
		Authentication Errors:              3
		Authentication Timeouts:            2
		Last Cleared:                       never

.. **Help line:** Displays counters for the tacacs server(s)


**Command History**

+---------+----------------------------------------------------------------------------------------------------------------------------+
| Release | Modification                                                                                                               |
+=========+============================================================================================================================+
| 25.1    | Command introduced                                                                                                         |
+---------+----------------------------------------------------------------------------------------------------------------------------+