show services port-mirroring sessions
-------------------------------------

**Minimum user role:** viewer

To display port-mirroring sessions configuration:



**Command syntax: show services port-mirroring sessions** [session-name]

**Command mode:** operational



..
	**Internal Note**

	- Port-mirroring session current configuration

**Parameter table**

+-----------------------+------------------------------------------------------------+---------------------------------------------------------------+
| Parameter             | Description                                                | Range                                                         |
+=======================+============================================================+===============================================================+
| session-name          | The name of the port-mirroring session                     | String                                                        |
+-----------------------+------------------------------------------------------------+---------------------------------------------------------------+

The following is the displayed information from the command:

+-----------------------+-----------------------------------------------------------------------------------+----------------------------------------------------+----------+
| Parameter             | Description                                                                       | Range                                              | Default  |
+=======================+===================================================================================+=============================+======================+==========+
| session-name          | The name of the port-mirroring session                                            | String                                             | \-       |
+-----------------------+-----------------------------------------------------------------------------------+----------------------------------------------------+----------+
| session-id            | The ID number of the session                                                      | 1..10                                              | \-       |
+-----------------------+-----------------------------------------------------------------------------------+----------------------------------------------------+----------+
| type                  | The mirroring session type                                                        | Local                                              | \-       |
|                       |                                                                                   | ERSPANv2                                           |          |
+-----------------------+-----------------------------------------------------------------------------------+----------------------------------------------------+----------+
| admin-state           | The administrative state of the port-mirroring session                            | Enabled                                            | Disabled |
|                       |                                                                                   | Disabled                                           |          |
+-----------------------+-----------------------------------------------------------------------------------+----------------------------------------------------+----------+
| sampling-probability  | The sampling probability of traffic from source interfaces                        | 1..65535                                           | 1        |
+-----------------------+-----------------------------------------------------------------------------------+----------------------------------------------------+----------+
| destination-interface | The type of destination interface                                                 | ge<interface speed>-<A>/<B>/<C>                    | \-       |
|                       |                                                                                   | ge<interface speed>-<A>/<B>/<C>.<sub-interface id> |          |
+-----------------------+-----------------------------------------------------------------------------------+----------------------------------------------------+----------+
| source-address        | The source address of the GRE tunnel for a remote session                         | IP address                                         | \-       |
+-----------------------+-----------------------------------------------------------------------------------+----------------------------------------------------+----------+
| destination-address   | The destination address of the GRE tunnel for a remote session                    | IP address                                         | \-       |
+-----------------------+-----------------------------------------------------------------------------------+----------------------------------------------------+----------+
| vrf-name              | The destination VRF of the GRE tunnel for a remote session                        | String                                             | \-       |
+-----------------------+-----------------------------------------------------------------------------------+----------------------------------------------------+----------+
| DSCP                  | The DSCP traffic class value to be set on all traffic mirrored to the destination | 0..63                                              | 0        |
+-----------------------+-----------------------------------------------------------------------------------+----------------------------------------------------+----------+
| TTL                   | The IP TTL to be set on all traffic mirrored to the destination                   | 1..255                                             | 255      |
+-----------------------+-----------------------------------------------------------------------------------+----------------------------------------------------+----------+
| source-interface      | The type of source interface                                                      | ge<interface speed>-<A>/<B>/<C>                    | \-       |
|                       |                                                                                   | ge<interface speed>-<A>/<B>/<C>.<sub-interface id> |          |
|                       |                                                                                   | bundle-<bundle id>                                 |          |
|                       |                                                                                   | bundle-<bundle id>.<sub-interface id>              |          |
+-----------------------+-----------------------------------------------------------------------------------+----------------------------------------------------+----------+
| direction             | The direction of the session                                                      | Ingress                                            | Both     |
|                       |                                                                                   | Egress                                             |          |
|                       |                                                                                   | Both                                               |          |
+-----------------------+-----------------------------------------------------------------------------------+----------------------------------------------------+----------+

**Example**
::

	dnRouter# show services port-mirroring sessions IDS-Debug

	Session: IDS-Debug, Session ID: 1
	  Type: local
	  Description:
	  Admin-state: Enabled
	  Sampling probability: 1 out of 1
	  Destination interface: ge100-1/0/25
	  Source interfaces:
	    ge100-1/0/20:
	      Direction: Both
	    ge100-1/0/21:
		  Direction: Ingress


	dnRouter# show services port-mirroring sessions

	Session: IDS-Debug, Session ID: 1
	  Description:
	  Admin-state: enabled
	  Sampling probability: 1 out of 1
	  Destination interface: ge100-1/0/25
	  Source interfaces:
	    ge100-1/0/20:
	      Direction: both
	    ge100-1/0/21:
	      Direction: ingress

	Session: test, Session ID: 2
	  Type: local
	  Description: TokyoHQ_test1
	  Admin-state: disabled
	  Sampling probability: 1 out of 1
	  Destination interface: ge100-1/0/28
	  Source interfaces:
	    bundle-11177:
	      Direction: egress

	Session: Session3, Session ID: 3
	  Type: ERSPANv2, ERSPAN-Session-ID: 1
	  Description: monitoring
	  Admin-state: enabled
	  Sampling probability: 1 out of 10
	  Tunnel configuration:
	    Source address: 1.1.1.1
	    Destination address: 1.1.1.2, VRF: default
	    DSCP: 0
	    TTL: 255
	  Source interfaces:
	    bundle-2.100:
	      Direction: both
	    bundle-3.200:
	      Direction: ingress

.. **Help line:** Displays port mirroring sessions configuration

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 15.1    | Command introduced |
+---------+--------------------+
