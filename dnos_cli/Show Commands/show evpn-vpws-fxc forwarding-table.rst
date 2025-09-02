show evpn-vpws-fxc forwarding-table
-----------------------------------

**Minimum user role:** viewer

To show the forwarding-table:

**Command syntax: show evpn-vpws-fxc forwarding-table** instance [instance-name] ncp [ncp-id]

.. instance - display view for specific evpn-vpws-fxc instance

.. ac-interface - display detailed information for a specific access interface

.. ncp - display information from a specific ncp. by default, display from active NCP with minimum ID.

**Command mode:** operational

**Note**

.. By default, the information will be sent from the active NCP with the lowest ID.

- The brief view is displayed by service name alphabetically.

.. Technical limitations:

.. On large scale routing tables, the table might not be presented ordered

.. When there are l2vpn table updates while presenting the table, the table might contain duplicate entries and might not contain all entries.

**Parameter table:**

+---------------+---------------------------------------------------------------------------------------------------+--------+------------------------+
| Parameter     | Description                                                                                       | Range  | Default                |
+===============+===================================================================================================+========+========================+
| instance-name | The evpn-vpws-fxc instance to display information.                                                | String | Default                |
+---------------+---------------------------------------------------------------------------------------------------+--------+------------------------+
| ncp-id        | Displays information from a specific NCP. By default, the active NCP with lowest ID is displayed. | 0..191 | NCP with the lowest ID |
+---------------+---------------------------------------------------------------------------------------------------+--------+------------------------+
| ac-interface  | The access interface to display detailed information.                                             | String | All                    |
+---------------+---------------------------------------------------------------------------------------------------+--------+------------------------+

**Example**
::

	dnRouter# show evpn-vpws-fxc forwarding-table

    Ingress-Terminations (separated by commas): M - MPLS, SRv6 - SRv6 Local SID
    Egress-Encapsulation: M - MPLS, SRv6 - SRv6 Tunnel (Destination IP)

    NCP-ID: 0

    | Service-Name       | Local-AC             | Normalized-VID           | Ingress-Termination                    | Neighbor        | Egress-Encapsulation                          |
    +--------------------+----------------------+--------------------------+----------------------------------------+-----------------+-----------------------------------------------+
    | MY_EVPN_VPWS_FXC_1 | ge100-0/0/2          | outer: 4001, inner: 4002 | M{11457}                               | 10.10.10.10      | M{78711}                                     |
    | MY_EVPN_VPWS_FXC_1 | ge100-0/0/2          | outer: 4001, inner: 4002 | M{11457}                               | 10.10.11.10      | M{87811}                                     |
    | MY_EVPN_VPWS_FXC_1 | ge100-0/0/3          | outer: 51, inner: 52     | M{11457}                               | 10.10.12.10      | M{99911}                                     |
    | MY_EVPN_VPWS_FXC_2 | ge100-0/0/4          | single-tag: 60           | M{32000}                               | 10.10.20.10      | M{11000}                                     |
    | MY_EVPN_VPWS_FXC_2 | ge100-0/0/4          | single-tag: 60           | M{32000}                               | 10.10.21.10      | M{12000}                                     |
    | MY_EVPN_VPWS_FXC_3 | ge100-0/0/5          | single-tag: 70           | M{32006}                               | 2000::2          | M{11006}                                     |

	dnRouter# show evpn-vpws-fxc forwarding-table instance MY_EVPN_VPWS_FXC_1

    Ingress-Terminations (separated by commas): M - MPLS, SRv6 - SRv6 Local SID
    Egress-Encapsulation: M - MPLS, SRv6 - SRv6 Tunnel (Destination IP)

    NCP-ID: 0

    | Service-Name       | Local-AC             | Normalized-VID           | Ingress-Termination                    | Neighbor        | Egress-Encapsulation                          |
    +--------------------+----------------------+--------------------------+----------------------------------------+-----------------+-----------------------------------------------+
    | MY_EVPN_VPWS_FXC_1 | ge100-0/0/2          | outer: 4001, inner: 4002 | M{11457}                               | 10.10.10.10      | M{78711}                                     |
    | MY_EVPN_VPWS_FXC_1 | ge100-0/0/2          | outer: 4001, inner: 4002 | M{11457}                               | 10.10.11.10      | M{87811}                                     |
    | MY_EVPN_VPWS_FXC_1 | ge100-0/0/3          | outer: 51, inner: 52     | M{11457}                               | 10.10.12.10      | M{99911}                                     |

	dnRouter# show evpn-vpws-fxc forwarding-table instance MY_EVPN_VPWS_FXC_1 ac_interface ge100-0/0/2

    NCP-ID: 0
    EVPN-VPWS-FXC Forwarding Table:
    MY_EVPN_VPWS_FXC_1
        AC Interface:
        name: ge100-0/0/2 Normalized-VID: outer: 4001, inner: 4002
        PW local label: 11457
        next-hop(1): 10.10.10.10 Recursive, Active
        PW label: 78711
        next-hop(1,1): 10.10.10.10 Active
        mpls labels: 4444
        interface: ge100-0/0/1.10
        next-hop(2): 10.10.11.10 Recursive, Active
        PW label: 87811
        next-hop(2,1): 10.10.11.10 Active
        mpls labels: 5555
        interface: ge100-0/0/1.11


.. **Help line:** show evpn-vpws-fxc forwarding-table

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 18.3    | Command introduced |
+---------+--------------------+
