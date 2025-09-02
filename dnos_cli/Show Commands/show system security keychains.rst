show system security keychains
------------------------------

**Minimum user role:** viewer

This command displays a detailed view of the configured security key chains in the system.

To display the security key chains:

**Command syntax: show system security keychains** [keychain-name]

**Command mode:** operational


..
    **Internal Note**

    - support auto-complete for configured key chains

    - when 'keychain-name' is not specified, then a summary output of all key chains will be printed

    - filter by list key (keychain-name)

**Parameter table**

+----------------+------------------------------------------+--------+---------+
| Parameter      | Description                              | Range  | Default |
+================+==========================================+========+=========+
| keychain-name  | The name of the security key chain       | String | \-      |
+----------------+------------------------------------------+--------+---------+

For each security key chain, the following information is displayed:

+---------------------+----------------------------------------------------------------------------------------------------------------+--------------------+-----------+
| Parameter           | Description                                                                                                    | Range              | Default   |
+=====================+================================================================================================================+====================+===========+
|                     |                                                                                                                |                    | \-        |
+---------------------+----------------------------------------------------------------------------------------------------------------+--------------------+-----------+

**Example**
::

    dnRouter# show system security keychains

    Security Key Chains:

    | Key chain        | Number of Keys | Receive Tolerance [Seconds] | Status        | Last Update Time    |
    +------------------+----------------+-----------------------------+---------------+---------------------+
    | isis-keys        | 8              | 3600                        | Valid         | 2024-10-10 00:10:00 |
    | security-auth    | 32             | infinite                    | No valid keys | 2024-10-12 00:00:07 |


    dnRouter# show system security keychains isis-keys

    Security Key Chains:
    
    Key-chain: isis-keys
      Status: Valid
      Last Update Time: 2024-10-10 00:10:00
      Receive-tolerance: infinite
      Keys:
        | Key ID   | Cryptographic Algorithm | Send Lifetime                                   | Status        | Receive Lifetime                                | Status        |
        +----------+-------------------------+-------------------------------------------------+---------------+-------------------------------------------------+---------------+
        | 0        | HMAC-SHA-256            | 2024-09-08 14:30:00 - 2024-10-08 15:30:00 local | Expired       | 2024-09-08 14:30:00 - 2024-10-10 23:59:59 local | Valid         |
        | 1        | HMAC-SHA-256            | 2024-10-08 14:30:00 - 2024-10-08 15:30:00 GMT   | Valid         | 2024-10-08 14:30:00 - 2024-10-08 15:30:00 GMT   | Valid         |
        | 2        | HMAC-SHA-256            | 2024-11-08 14:30:00 - forever                   | Pending       | 2024-11-08 14:30:00 - forever                   | Pending       |
        ...


.. **Help line:** show configured security key chains

**Command History**

+---------+------------------------------------------------------------------------------------------------+
| Release | Modification                                                                                   |
+=========+================================================================================================+
| 25.2    | Command introduced                                                                             |
+---------+------------------------------------------------------------------------------------------------+