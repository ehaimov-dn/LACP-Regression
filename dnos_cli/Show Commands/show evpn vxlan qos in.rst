show evpn vxlan qos in
----------------------

**Minimum user role:** viewer

To display the evpn vxlan QoS in counters:

**Command syntax: show evpn vxlan qos in** instance [instance-name]

**Command mode:** operational

.. **Note**

**Parameter table**

+----------------+---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
| Parameter      | Description                                             | Range                                                                                                                                                                                                                                                         | Default |
+================+=========================================================+===============================================================================================================================================================================================================================================================+=========+
| instance-name  | The configured EVPN instance name.                      | string 1..255                                                                                                                                                                                                                                                 | \-      |
+----------------+---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+


**Example**
::

    dnRouter# show evpn vxlan qos in 

    Evpn: evpn1
    Qos in
        Known-unicast-bit-rate
            Configured rate: 5000 kbps burst: 100 kByte
            Conformed packets:                                 12447 (         500 pps /       0 kpps )
            Conformed octets:                               14936400 (      600000 bps /       0 kbps )
            Violated packet drops:                              5000 (          13 pps /       0 kpps )
            Violated octet drops:                            5000000 (       26000 bps /       0 kbps )
    
    Evpn: evpn2
    Qos in
        Known-unicast-bit-rate
            Configured rate: 5000 kbps burst: 100 kByte
            Conformed packets:                                 10000 (         500 pps /       0 kpps )
            Conformed octets:                               14921400 (      590000 bps /       0 kbps )
            Violated packet drops:                                 0 (           0 pps /       0 kpps )
            Violated octet drops:                                  0 (           0 bps /       0 kbps )

    
    dnRouter# show evpn vxlan qos in evpn2
    
    Evpn: evpn2
    Qos in
        Known-unicast-bit-rate
            Configured rate: 5000 kbps burst: 100 kByte
            Conformed packets:                                 10000 (         500 pps /       0 kpps )
            Conformed octets:                               14921400 (      590000 bps /       0 kbps )
            Violated packet drops:                                 0 (           0 pps /       0 kpps )
            Violated octet drops:                                  0 (           0 bps /       0 kbps )


.. **Help line:** show evpn vxlan qos in

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+