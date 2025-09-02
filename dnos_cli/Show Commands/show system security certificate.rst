show system security certificate
--------------------------------

**Minimum user role:** viewer

Display parsed security certificate content of all CA and device certificates loaded to the system.

To display the certifications in the system:

**Command syntax: show system security certificate** [certificate-name]

**Note**

- When certificate name is not provided, all certificates downloaded to the system will be presented.

- A password protected file, e.g., a PKCS#12 bundle file, will be presented without its certificates' data.

**Command mode:** operational

**Parameter table**

The following information is displayed:

+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter             | Description                                                                                                                                     |
+=======================+=================================================================================================================================================+
| certificate-name      | The name of the certificate downloaded on the device                                                                                            |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| certificate-file      | The file name of the certificate downloaded on the device                                                                                       |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| Is password protected | Is the certificate file signed with a password                                                                                                  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| Is CA certificate     | Was the certificate issued by a Certificate Authority                                                                                           |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| Private key available | Is a private key available on the system for this certificate. Applicable only to device certificates                                           |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature Algorithm   | Algorithm identifier for the algorithm used by the CA to sign the certificate                                                                   |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| Public key algorithm  | The public key algorithm of the certificate                                                                                                     |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| Subject common name   | X509 subject common name (CN) attribute                                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| Issuer common name    | X509 certificate issuer common name (CN) attribute                                                                                              |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| Validity              | Start and end date of certificate validity period                                                                                               |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+

**Example**
::

    dnRouter# show system security certificate

        Certificate name : ca_certificate
        Certificate file : ca_certificate.crt
        Is password protected: False
        Is CA certificate: True
        Signature Algorithm: sha1WithRSAEncryption
        Public key algorithm: rsaEncryption
        Subject common name: AAA Certificate Services
        Issuer common name: AAA Certificate Services
        Validity:
            Start: Mar 12 00:00:00 2004 GMT
            End  : Mar 11 23:59:59 2028 GMT

        Certificate name : my_certificate
        Certificate file : my_certificate.crt
        Is password protected: False
        Is CA certificate: False
        Private key available: True
        Signature Algorithm: sha256WithRSAEncryption
        Public key algorithm: rsaEncryption
        Subject common name: dn_cert
        Issuer common name: dn_ca
        Validity:
            Start: Mar 12 00:00:00 2024 GMT
            End  : Mar 11 23:59:59 2034 GMT

        Certificate name : my_certificate_2
        Certificate file : my_certificate_2.pem
        Is password protected: False
        Is CA certificate: False
        Private key available: True
        Signature Algorithm: sha256WithRSAEncryption
        Public key algorithm: rsaEncryption
        Subject common name: dn_cert
        Issuer common name: dn_ca
        Validity: EXPIRED
            Start: Mar 12 00:00:00 2014 GMT
            End  : Mar 11 23:59:59 2024 GMT

    dnRouter# show system security certificate my_certificate_2

        Certificate name : my_certificate_2
        Certificate file : my_certificate_2.pem
        Is password protected: False
        Is CA certificate: False
        Private key available: True
        Signature Algorithm: sha256WithRSAEncryption
        Public key algorithm: rsaEncryption
        Subject common name: dn_cert
        Issuer common name: dn_ca
        Validity: EXPIRED
            Start: Mar 12 00:00:00 2014 GMT
            End  : Mar 11 23:59:59 2024 GMT

    dnRouter# show system security certificate my_certificate.p12

        Certificate name : my_certificate
        Certificate file : my_certificate.p12
        Is password protected: True

    dnRouter# show system security certificate corrupted_certificate.pem

        Certificate name : corrupted_certificate
        Certificate file : corrupted_certificate.pem
        ERROR: failed to parse certificate file
        Certificate corrupted or invalid format. Supported formats: PEM, PKCS#12

.. **Help line:** show available security certificates in system

**Command History**

+---------+--------------------------------+
| Release | Modification                   |
+=========+================================+
| 25.1    | Command introduced             |
+---------+--------------------------------+
