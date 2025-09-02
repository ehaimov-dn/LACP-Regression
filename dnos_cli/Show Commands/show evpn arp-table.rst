show evpn arp-table
-------------------

**Minimum user role:** operator

To show the arp-table for an EVPN instance.

**Command syntax: show evpn arp-table** instance [evpn-name]
**Command syntax: show evpn arp-table** ip [ipv4-address]
**Command syntax: show evpn arp-table** source-ip [nexthop-ip-address]
**Command syntax: show evpn ** instance [evpn-name] **arp-table** 
**Command syntax: show evpn ** instance [evpn-name] **arp-table** ip [ipv4-address]
**Command syntax: show evpn ** instance [evpn-name] **arp-table** source-ip [nexthop-ip-address]


**Command mode:** operational

**Parameter table:**

+--------------------+----------------------------------------------------------+-------------------+---------------+
| Parameter          | Description                                              | Values            | Default value |
+====================+==========================================================+===================+===============+
| evpn-name          | The name of the EVPN instance                            | String | all      | \-            |
+--------------------+----------------------------------------------------------+-------------------+---------------+
| ipv4-address       | Provide information for the specified arp table entry    | String | all      | \-            |
+--------------------+----------------------------------------------------------+-------------------+---------------+
| nexthop-ip-address | Provide all entries for the specified nexthop-ip-address | String | all      | \-            |
+--------------------+----------------------------------------------------------+-------------------+---------------+

**Note:**

- Specifying an evpn-name will display the information of the specified EVPN instance.

- If no instance is specified, this will result in the listing of the inclusive-multicast-table information for all the EVPN instances.

- If ip is specified then detailed information will be provided for that ip-address.

- If source-ip is specified then all entries with that nexthop ip-address will be provided.


**Example**
::


   dnRouter# show evpn arp-table

      EVPN: EVPN_Site1_Interop_001000
        EVI ID : 2326
        Description : EVPN_Interop

        ETH TAG: 0

        IRB Interface: irb3900
        IP Address      | MAC address          | Origin                 | Nexthop
        -------------------------------------------------------------------------------------------------
        200.1.100.16    | 84:40:76:c2:45:1a    | bgp                    | 100.0.16.16
        200.1.100.18    | 84:40:76:62:c5:c5    | local-irb              | irb3900
        200.1.100.27    | 84:40:76:a5:eb:79    | bgp                    | 100.0.27.27
        200.1.100.92    | 84:40:76:0d:ec:52    | bgp                    | 100.0.92.92
      EVPN: EVPN_Site1_Interop_00901
        EVI ID : 2327
        Description : EVPN_Interop

        ETH TAG: 0

        IRB Interface: irb3801
        IP Address      | MAC address          | Origin                 | Nexthop
        -------------------------------------------------------------------------------------------------
        200.1.1.16      | 84:40:76:c2:45:1a    | bgp                    | 100.0.16.16
        200.1.1.18      | 84:40:76:62:c5:c5    | local-irb              | irb3801
        200.1.1.27      | 84:40:76:a5:eb:79    | bgp                    | 100.0.27.27
        200.1.1.92      | 84:40:76:0d:ec:52    | bgp                    | 100.0.92.92
      EVPN: EVPN_Site1_Interop_00902
        EVI ID : 2328
        Description : EVPN_Interop

        ETH TAG: 0

        IRB Interface: irb3802
        IP Address      | MAC address          | Origin                 | Nexthop
        -------------------------------------------------------------------------------------------------
        200.1.2.16      | 84:40:76:c2:45:1a    | bgp                    | 100.0.16.16
        200.1.2.18      | 84:40:76:62:c5:c5    | local-irb              | irb3802
        200.1.2.27      | 84:40:76:a5:eb:79    | bgp                    | 100.0.27.27
        200.1.2.92      | 84:40:76:0d:ec:52    | bgp                    | 100.0.92.92

      =======================================================

      dnRouter# show evpn arp-table instance EVPN_Site1_Interop_00902

        EVPN: EVPN_Site1_Interop_00902
        EVI ID : 2328
        Description : EVPN_Interop

        ETH TAG: 0

        IRB Interface: irb3802
        IP Address      | MAC address          | Origin                 | Nexthop
        -------------------------------------------------------------------------------------------------
        200.1.2.16      | 84:40:76:c2:45:1a    | bgp                    | 100.0.16.16
        200.1.2.18      | 84:40:76:62:c5:c5    | local-irb              | irb3802
        200.1.2.27      | 84:40:76:a5:eb:79    | bgp                    | 100.0.27.27
        200.1.2.92      | 84:40:76:0d:ec:52    | bgp                    | 100.0.92.92

      =======================================================


    dnRouter# show evpn arp-table instance EVPN_Site1_Interop_00902

      EVPN: EVPN_Site1_Interop_00902
        EVI ID : 2328
        Description : EVPN_Interop

        ETH TAG: 0

        IRB Interface: irb3802
        IP Address      | MAC address          | Origin                 | Nexthop
        -------------------------------------------------------------------------------------------------
        200.1.2.16      | 84:40:76:c2:45:1a    | bgp                    | 100.0.16.16
        200.1.2.18      | 84:40:76:62:c5:c5    | local-irb              | irb3802
        200.1.2.27      | 84:40:76:a5:eb:79    | bgp                    | 100.0.27.27
        200.1.2.92      | 84:40:76:0d:ec:52    | bgp                    | 100.0.92.92


    =======================================================


   dnRouter# show evpn instance EVPN_Site1_Interop_00902 arp-table ip 200.1.2.27

      EVPN    : EVPN_Site1_Interop_00902
        EVI ID  : 2328
        ETH TAG : 0
        IP address: 200.1.2.27
        MAC address: 84:40:76:a5:eb:79
        Protocol: bgp
            ESI: N/A
        Encapsulation: mpls
        (1) Nexthop: 100.0.27.27
          MAC label: 1511
      Resolution: Single-homed (Single-homed MAC without ESI)
      Timestamp: 22-Jun-2025-16:41:38
        Default Gateway: True
        Sticky: True
        Sequence number: 0

       IP Mobility
        Moves per Detection Window: 0
        Number of Completed Suppression Cycles: 0
        Suppression: None
        Traffic Handling: Forward
        Expected suppression release time: N/A
       Mobility History
        Event                | MAC Address          | Origin                 | Reason               | Date
        ------------------------------------------------------------------------------------------------------------------
        Remote               | 84:40:76:a5:eb:79    | 100.0.27.27            | Sticky               | 22-Jun-2025-15:14:45
        Remote               | 84:40:76:a5:eb:79    | 100.0.27.27            | Sticky               | 22-Jun-2025-16:41:38

    =======================================================

   dnRouter# show evpn instance EVPN_Site1_Interop_00902 arp-table ip 200.1.2.18

      EVPN    : EVPN_Site1_Interop_00902
      EVI ID  : 2328
      ETH TAG : 0
      IP address: 200.1.2.18
        MAC address: 84:40:76:62:c5:c5
      Protocol: Local
         ESI: N/A
         Interface: irb3802
         Timestamp: 19-Jun-2025-23:17:41
           Default Gateway: True
          Sticky: True
        Sequence number: 0

    =======================================================

   dnRouter# show evpn arp-table source-ip 100.0.16.16

   EVPN: EVPN_Site1_Interop_001000
    EVI ID : 2326
    Description : EVPN_Interop

    ETH TAG: 0

    IRB Interface: irb3900
      IP Address      | MAC address          | Origin                 | Nexthop
      -------------------------------------------------------------------------------------------------
      200.1.100.16    | 84:40:76:c2:45:1a    | bgp                    | 100.0.16.16
   EVPN: EVPN_Site1_Interop_00901
    EVI ID : 2327
    Description : EVPN_Interop

    ETH TAG: 0

    IRB Interface: irb3801
      IP Address      | MAC address          | Origin                 | Nexthop
      -------------------------------------------------------------------------------------------------
      200.1.1.16      | 84:40:76:c2:45:1a    | bgp                    | 100.0.16.16
   EVPN: EVPN_Site1_Interop_00902
    EVI ID : 2328
    Description : EVPN_Interop

    ETH TAG: 0

    IRB Interface: irb3802
      IP Address      | MAC address          | Origin                 | Nexthop
      -------------------------------------------------------------------------------------------------
      200.1.2.16      | 84:40:76:c2:45:1a    | bgp                    | 100.0.16.16

    =======================================================


   dnRouter# show evpn instance EVPN_Site1_Interop_00902 arp-table source-ip 100.0.27.27

     EVPN: EVPN_Site1_Interop_00902
     EVI ID : 2328
     Description : EVPN_Interop

     ETH TAG: 0

     IRB Interface: irb3802
       IP Address      | MAC address          | Origin                 | Nexthop
       -------------------------------------------------------------------------------------------------
       200.1.2.27      | 84:40:76:a5:eb:79    | bgp                    | 100.0.27.27

.. **Help line:** show information of the MAC Table of the EVPN instances

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| TBD     | Command introduced                  |
+---------+-------------------------------------+