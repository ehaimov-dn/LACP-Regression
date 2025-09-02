show evpn ndp-table
-------------------

**Minimum user role:** operator

To show the ndp-table for an EVPN instance.

**Command syntax: show evpn ndp-table-table** instance [evpn-name]
**Command syntax: show evpn ndp-table** ip [ipv6-address]
**Command syntax: show evpn ndp-table** source-ip [nexthop-ip-address]
**Command syntax: show evpn ** instance [evpn-name] **ndp-table** 
**Command syntax: show evpn ** instance [evpn-name] **ndp-table** ip [ipv6-address]
**Command syntax: show evpn ** instance [evpn-name] **ndp-table** source-ip [nexthop-ip-address]


**Command mode:** operational

**Parameter table:**

+--------------------+-------------------------------------------------------------------------------+-------------------+---------------+
| Parameter          | Description                                                                   | Values            | Default value |
+====================+===============================================================================+===================+===============+
| evpn-name          | The name of the EVPN instance                                                 | String | all      | \-            |
+--------------------+-------------------------------------------------------------------------------+-------------------+---------------+
| ipv6-address       | Provide information for the ndp table entry with the specified ip-address     | String | all      | \-            |
+--------------------+-------------------------------------------------------------------------------+-------------------+---------------+
| nexthop-ip-address | Provide all entries for the specified nexthop-ip-address                      | String | all      | \-            |
+--------------------+-------------------------------------------------------------------------------+-------------------+---------------+

**Note:**

- Specifying an evpn-name will display the information of the specified EVPN instance.

- If no instance is specified, this will result in the listing of the inclusive-multicast-table information for all the EVPN instances.

- If ip is specified then detailed information will be provided for that ip-address.

- If source-ip is specified then all entries with that nexthop ip-address will be provided.



**Example**
::

   dnRouter# show evpn ndp-table

   EVPN: EVPN_Site1_Interop_001000
     EVI ID : 2326
     Description : EVPN_Interop

     ETH TAG: 0

     IRB Interface: irb3900
       IP Address                                 | MAC address          | Origin                 | Nexthop
       ----------------------------------------------------------------------------------------------------------------------------
       2000:1:64::16                              | 84:40:76:c2:45:1a    | bgp                    | 100.0.16.16
       2000:1:64::18                              | 84:40:76:62:c5:c5    | local-irb              | irb3900
       2000:1:64::27                              | 84:40:76:a5:eb:79    | bgp                    | 100.0.27.27
       2000:1:64::92                              | 84:40:76:0d:ec:52    | bgp                    | 100.0.92.92
   EVPN: EVPN_Site1_Interop_00901
     EVI ID : 2327
     Description : EVPN_Interop

     ETH TAG: 0

     IRB Interface: irb3801
       IP Address                                 | MAC address          | Origin                 | Nexthop
       ----------------------------------------------------------------------------------------------------------------------------
       2000:1:1::16                               | 84:40:76:c2:45:1a    | bgp                    | 100.0.16.16
       2000:1:1::18                               | 84:40:76:62:c5:c5    | local-irb              | irb3801
       2000:1:1::27                               | 84:40:76:a5:eb:79    | bgp                    | 100.0.27.27
       2000:1:1::92                               | 84:40:76:0d:ec:52    | bgp                    | 100.0.92.92

   =======================================================

   dnRouter# show evpn ndp-table instance EVPN_Site1_Interop_00902

   EVPN: EVPN_Site1_Interop_00902
     EVI ID : 2328
     Description : EVPN_Interop

     ETH TAG: 0

     IRB Interface: irb3802
       IP Address                                 | MAC address          | Origin                 | Nexthop
       ----------------------------------------------------------------------------------------------------------------------------
       2000:1:2::16                               | 84:40:76:c2:45:1a    | bgp                    | 100.0.16.16
       2000:1:2::18                               | 84:40:76:62:c5:c5    | local-irb              | irb3802
       2000:1:2::27                               | 84:40:76:a5:eb:79    | bgp                    | 100.0.27.27
       2000:1:2::92                               | 84:40:76:0d:ec:52    | bgp                    | 100.0.92.92

   =======================================================


   dnRouter# show evpn instance EVPN_Site1_Interop_00902 ndp-table

   EVPN: EVPN_Site1_Interop_00902
     EVI ID : 2328
     Description : EVPN_Interop

     ETH TAG: 0

     IRB Interface: irb3802
       IP Address                                 | MAC address          | Origin                 | Nexthop
       ----------------------------------------------------------------------------------------------------------------------------
       2000:1:2::16                               | 84:40:76:c2:45:1a    | bgp                    | 100.0.16.16
       2000:1:2::18                               | 84:40:76:62:c5:c5    | local-irb              | irb3802
       2000:1:2::27                               | 84:40:76:a5:eb:79    | bgp                    | 100.0.27.27
       2000:1:2::92                               | 84:40:76:0d:ec:52    | bgp                    | 100.0.92.92


   =======================================================

   dnRouter# show evpn instance EVPN_Site1_Interop_00902 ndp-table ip 2000:1:2::92

   EVPN    : EVPN_Site1_Interop_00902
   EVI ID  : 2328
   ETH TAG : 0
   IP address: 2000:1:2::92
     MAC address: 84:40:76:0d:ec:52
     Protocol: bgp
         ESI: N/A
         Encapsulation: mpls
         (1) Nexthop: 100.0.92.92
             MAC label: 945
         Resolution: Single-homed (Single-homed MAC without ESI)
         Timestamp: 23-Jun-2025-14:03:56
           Default Gateway: True
           Sticky: True
           Sequence number: 0



   =======================================================

   dnRouter# show evpn ndp-table source-ip 100.0.27.27

   EVPN: EVPN_Site1_Interop_001000
     EVI ID : 2326
     Description : EVPN_Interop

     ETH TAG: 0

     IRB Interface: irb3900
       IP Address                                 | MAC address          | Origin                 | Nexthop
       ----------------------------------------------------------------------------------------------------------------------------
       2000:1:64::27                              | 84:40:76:a5:eb:79    | bgp                    | 100.0.27.27
   EVPN: EVPN_Site1_Interop_00901
     EVI ID : 2327
     Description : EVPN_Interop

     ETH TAG: 0

     IRB Interface: irb3801
       IP Address                                 | MAC address          | Origin                 | Nexthop
       ----------------------------------------------------------------------------------------------------------------------------
       2000:1:1::27                               | 84:40:76:a5:eb:79    | bgp                    | 100.0.27.27
   EVPN: EVPN_Site1_Interop_00902
     EVI ID : 2328
     Description : EVPN_Interop

     ETH TAG: 0

     IRB Interface: irb3802
       IP Address                                 | MAC address          | Origin                 | Nexthop
       ----------------------------------------------------------------------------------------------------------------------------
       2000:1:2::27                               | 84:40:76:a5:eb:79    | bgp                    | 100.0.27.27

   =======================================================

   dnRouter# show evpn instance EVPN_Site1_Interop_00902 ndp-table  source-ip 100.0.27.27

   EVPN: EVPN_Site1_Interop_00902
     EVI ID : 2328
     Description : EVPN_Interop

     ETH TAG: 0


     IRB Interface: irb3802
       IP Address                                 | MAC address          | Origin                 | Nexthop
       ----------------------------------------------------------------------------------------------------------------------------
       2000:1:2::27                               | 84:40:76:a5:eb:79    | bgp                    | 100.0.27.27





.. **Help line:** show information of the MAC Table of the EVPN instances

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| TBD     | Command introduced                  |
+---------+-------------------------------------+