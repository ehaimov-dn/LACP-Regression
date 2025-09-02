show system grpc 
-----------------

**Minimum user role:** viewer

To display the GRPC configuration per system:



**Command syntax: show system grpc**

**Command mode:** operational



**Note**

- PPS relates to the number of gRPC messages and not packets.
- gRPC cipher list contains all available ciphers with an indication per cipher if it is enabled or disabled.

.. - vrf "default" represents the in-band management, while vrf "mgmt0" represents the out-of-band management.

    - PPS - relates to the number of gRPC messages (not IP packets)



**Example**
::

    dnRouter# show system grpc

    gRPC port: 50051
    gNMI version: 0.10
    gNMI encoding: proto3
    Max-sessions: 20


    VRF mgmt0
    Status: available
    Admin-state: enabled
        Client List
          Client list type: allow
          Client list IP networks:
            1.2.3.0/24
            1.2.4.0/24
                2001:db8:2222::/48

    VRF default
    Status: available
    Admin-state: enabled
        Client List
          Client list type: allow
          Client list IP networks:
            1.2.3.0/24
            1.2.4.0/24
                2001:db8:2222::/48

    VRF my_vrf
    Status: available
    Admin-state: enabled
        Client List
          Client list type: allow
          Client list IP networks:
            1.2.2.0/24
            1.2.1.0/24
                2002:db8:2222::/48


    Cipher list:
    TLS_AES_128_GCM_SHA256 (enabled)
    TLS_AES_256_GCM_SHA384 (enabled)
    TLS_CHACHA20_POLY1305_SHA256 (enabled)
    TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 (enabled)
    TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 (enabled)
    TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (enabled)
    TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (enabled)
    TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256 (enabled)
    TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256 (enabled)

    Server-authentication: TLS (certificate: myCert.crt, file exists: True)
    Client-authentication: enabled (CA certificate: ca_cert.crt, file exists: True)
    Telemetry Statistics:
      Exported bit rate: 0.6 Mbps
      Exported leaves: 45,123
      Exported leaf rate: 312 leaves per second

.. **Help line:** show system grpc

**Command History**

+---------+---------------------------------------------------------------------+
| Release | Modification                                                        |
+=========+=====================================================================+
| 11.0    | Command introduced                                                  |
+---------+---------------------------------------------------------------------+
| 13.1    | Added support for in-band (default VRF) and out-of-band (mgmt0 VRF) |
+---------+---------------------------------------------------------------------+
| 19.1.3  | Added list of grpc supported ciphers                                |
+---------+---------------------------------------------------------------------+
| 25.1    | Added client auth state and CA certificate name                     |
+---------+---------------------------------------------------------------------+
