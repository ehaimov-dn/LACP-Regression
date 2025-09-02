show system netconf
--------------------

**Minimum user role:** viewer

Network Configuration Protocol (Netconf) is an XML-based protocol that client applications use to request information from and make configuration changes to a device.

To display the NETCONF configuration in the system:

**Command syntax: show system netconf**

**Command mode:** operational



**Parameter table**

The following information is displayed:

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------+
| Parameter           | Description                                                                                                                                     | Reference                                    |
+=====================+=================================================================================================================================================+==============================================+
| admin-state         | The administrative state of the NETCONF feature                                                                                                 | system netconf vrf mgmt0 admin-state         |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------+
| listen-port         | The TCP port used for NETCONF connections over SSH                                                                                              | system netconf port                          |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------+
| max-sessions        | The maximum number of allowed concurrent sessions                                                                                               | system netconf max-sessions                  |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------+
| session-timeout     | The configured value for timeout when the session is idle                                                                                       | The TCP timeout                              |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------+
| class-of-service    | CoS for all outgoing NETCONF sessions                                                                                                           | system netconf class-of-service              |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------+
| rate limit          | The time window for SSH and Netconf connections rate limiting                                                                                   | system ssh server time-window                |
| time window         |                                                                                                                                                 |                                              |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------+
| rate limit          | the maximal number of SSH  and Netconf connection attempts within the defined time window                                                       | system ssh server max-attempts               |
| max-attempts        |                                                                                                                                                 |                                              |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------+
| VRF                 | The netconf session management type (in-band, out-of-band or non-default-vrf)                                                                   | default (in-band)                            |
|                     |                                                                                                                                                 | non-default-vrf (in-band)                    |
|                     |                                                                                                                                                 | mgmt0 (out-of-band)                          |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------+
| client list         | The IP addresses that depending on the client-list type will or will not be permitted access to NETCONF sessions                                | system netconf vrf mgmt0 client-list         |
|                     |                                                                                                                                                 | system netconf vrf mgmt0 client-list type    |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------+
| server capabilities | The NETCONF capabilities that are supported by the DNOS device. These capabilities are advertised to the client during session establishment.   | system netconf                               |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------+
| ciphers             | Ciphers used by ssh transport of the NETCONF feature                                                                                            | system ssh security ciphers                  |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------+
| macs                | MACs used by ssh transport of the NETCONF feature                                                                                               | system ssh security macs                     |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------+
| hostkey algorithms  | Hostkey algorithms used by ssh transport of the NETCONF feature                                                                                 | system ssh security host-key-algorithms      |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------+
| host certificate    | Host certificate used by SSH Server                                                                                                             | system ssh security host-certificate         |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------+
| ca certificate      | Certificate authority (CA) certificate used by SSH Server for client authentication                                                             | system ssh security ca-certificate           |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------+
| ca signature        |  Allowed signature algorithms for Certificate authority (CA) certificate signing                                                                | system ssh security ca-signature-certificate |
| algorithms          |                                                                                                                                                 |                                              |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------+

**Example**
::

    dnRouter# show system netconf

    Listen-port: 830
    Max-sessions: 6
    Session-timeout: 30 minutes
    Class-of-service: 16 (dscp)
    Rate limit time window: 50 seconds
    Rate limit max-attempts: 15
    Ciphers: chacha20-poly1305-openssh.com,aes256-gcm-openssh.com,aes128-gcm-openssh.com,aes256-ctr,aes192-ctr,aes128-ctr
    MACs: umac-64-etm-openssh.com,umac-128-etm-openssh.com,hmac-sha2-256-etm-openssh.com,hmac-sha2-512-etm-openssh.com,umac-64-openssh.com,umac-128-openssh.com,hmac-sha2-256,hmac-sha2-512
    Hostkey Algorithms: ssh-ed25519,ssh-rsa,rsa-sha2-256,rsa-sha2-512,ssh-dss,ecdsa-sha2-nistp256;
    Host certificate: my-host-cert.crt (file valid)
    CA public key file: my-ca.pub (file invalid)
    CA Signature Algorithms: ssh-ed25519,ssh-rsa,rsa-sha2-256

    VRF default
    admin-state: enabled
        Client List
          Client list type: allow
          Client list networks:
            1.2.3.0/24
            1.2.4.0/24
                2001:db8:2222::/48

    VRF my_vrf
    admin-state: disabled
        Client List
          Client list type: allow
          Client list networks:
            3.6.1.0/24
            3.2.4.0/24
                2001:db8:1111::/48

    VRF mgmt0
    admin-state: enabled
        Client List
          Client list type: allow
          Client list networks:
            1.1.1.0/24
            2.2.4.0/24
                2001:db8:1122::/48

    Server Capabilities:
        urn:ietf:params:netconf:base:1.0
        urn:ietf:params:netconf:capability:candidate:1.0
        urn:ietf:params:netconf:capability:validate:1.0
        urn:ietf:params:netconf:capability:confirmed-commit:1.0
        urn:ietf:params:netconf:base:1.1
        urn:ietf:params:netconf:capability:validate:1.1
        urn:ietf:params:netconf:capability:with-defaults:1.0?basic-mode=explicit&amp;also-supported=report-all

.. **Help line:** show active netconf sessions in system.

**Command History**

+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Release | Modification                                                                                                                                                                                  |
+=========+===============================================================================================================================================================================================+
| 10.0    | Command introduced                                                                                                                                                                            |
+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 11.0    | Updated command output to display CoS, client list information and server capabilities. Max-sessions is not configurable and is the maximum SSH sessions. Session-timeout is the TCP timeout. |
+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 13.1    | Added OOB support: display of client lists per in-band (default VRF) and out-of-band (mgmt0) VRF                                                                                              |
+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 17.0    | Added support for non-default VRF session management type                                                                                                                                     |
+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 19.2    | Added support for system ssh security                                                                                                                                                         |
+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 19.1.3  | Added support for ssh/netconf rate limit parameters (not available in v19.2)                                                                                                                  |
+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 25.1    | Added host and CA certificate names                                                                                                                                                           |
+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
