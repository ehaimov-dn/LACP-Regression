show bridge-domain loop-prevention
----------------------------------

**Minimum user role:** operator

To show the detailed information of a bridge-domain instance.

**Command syntax: show bridge-domain loop-prevention** instance [service-name]
**Command syntax: show bridge-domain** instance [service-name] loop-prevention
**Command syntax: show bridge-domain loop-prevention** instance [service-name] interface
**Command syntax: show bridge-domain** instance [service-name] loop-prevention interface
**Command syntax: show bridge-domain loop-prevention** instance [service-name] interface [interface-name-service]
**Command syntax: show bridge-domain** instance [service-name]  loop-preventioninterface [interface-name-service]
**Command syntax: show bridge-domain loop-prevention** instance [service-name] mac-table
**Command syntax: show bridge-domain** instance [service-name] loop-prevention mac-table
**Command syntax: show bridge-domain loop-prevention** instance [service-name] mac-table [mac-address]
**Command syntax: show bridge-domain** instance [service-name] loop-prevention mac-table [mac-address]

**Command mode:** operational

**Parameter table:**

+------------------------+-----------------------------------------+-------------------+---------------+
| Parameter              | Description                             | Values            | Default value |
+========================+=========================================+===================+===============+
| service-name           | Service name                            | String            | \-            |
+------------------------+-----------------------------------------+-------------------+---------------+
| interface-name-service | Attachment circuit inside service       | String            | \-            |
+------------------------+-----------------------------------------+-------------------+---------------+
| mac-address            | Display information about MAC address   | xx:xx:xx:xx:xx:xx | \-            |
+------------------------+-----------------------------------------+-------------------+---------------+

**Note:**
The commands accept `loop-prevention` either before or after `instance`.

**Example**
::

    dev-dnRouter# show bridge-domain loop-prevention instance bd_1

    Bridge domain: bd_1

        +-------------------------------+-----------------------------+
        |                               | Local Loop Prevention (LLP) |
        +-------------------------------+-----------------------------+
        | Loop Prevention               | enabled                     |
        | Loop Detection Threshold      | 5                           |
        | Loop Detection Window         | 90s                         |
        | Restore Timer                 | 10s                         |
        | Restore Max Cycles            | restore-manually            |
        | Restore Reset Interval        | 24h                         |
        | Action                        | ac-shutdown                 |
        | Number of Shutdown Interfaces | 2                           |
        +-------------------------------+-----------------------------+

        Local Loop Prevention
        =====================

        +-------------------+-----------------------------+
        | MAC Address       | Mac Moves in Window / Limit |
        +-------------------+-----------------------------+
        | 02:00:00:00:00:00 | 0 / 5                       |
        | 04:00:00:00:00:00 | 4 / 5                       |
        +-------------------+-----------------------------+

        +---------------------+----------+-------------------------+
        | Shutdown Interfaces | Status   | Remaining Shutdown Time |
        +---------------------+----------+-------------------------+
        | ge100-0/0/11.1      | Shutdown | N/A                     |
        | ge100-0/0/11.2      | Shutdown | N/A                     |
        +---------------------+----------+-------------------------+


    dev-dnRouter# show bridge-domain loop-prevention instance bd_1 interface

    Bridge domain: bd_1
        +---------------------+----------+-------------------------+
        | Shutdown Interfaces | Status   | Remaining Shutdown Time |
        +---------------------+----------+-------------------------+
        | ge100-0/0/11.1      | Shutdown | N/A                     |
        | ge100-0/0/11.2      | Shutdown | N/A                     |
        +---------------------+----------+-------------------------+


    dev-dnRouter# show bridge-domain loop-prevention instance bd_1 interface ge100-0/0/11.1

    Bridge domain: bd_1
    Interface: ge100-0/0/11.1

        Status			:	Shutdown
        Remaining Shutdown Time	:	N/A

        Local Loop Prevention
        =====================

        +------------------------+-----------------------+
        |                        | Local Loop Prevention |
        +------------------------+-----------------------+
        | Number of Cycles       | 0 / restore-manually  |
        | Restore Timer          | 10s                   |
        | Restore Reset Interval | 24h                   |
        +------------------------+-----------------------+


        Shutdown History
        ================

            +----------------------+----------+----------------------+-------------------------------+
            | Time                 | Action   | Count                | Source                        |
            +----------------------+----------+----------------------+-------------------------------+
            | 25-Feb-2025-18:04:55 | Shutdown | 0 / restore-manually | MAC Address 02:00:00:00:00:00 |
            +----------------------+----------+----------------------+-------------------------------+


    dev-dnRouter# show bridge-domain loop-prevention instance bd_1 mac-table

        +-------------------+-----------------------------+
        | MAC Address       | Mac Moves in Window / Limit |
        +-------------------+-----------------------------+
        | 02:00:00:00:00:00 | 0 / 5                       |
        | 04:00:00:00:00:00 | 0 / 5                       |
        +-------------------+-----------------------------+


    dev-dnRouter# show bridge-domain loop-prevention instance bd_1 mac-table 02:00:00:00:00:00

    Bridge-Domain: bd_1 id: 1
    Mac-Address: 02:00:00:00:00:00

          Local Loop Prevention
          =====================

          Move History
          ------------

            +----------------------+----------------+-----------------+---------------------------+
            | Time                 | Interface      | Sequence Number | Comment                   |
            +----------------------+----------------+-----------------+---------------------------+
            | 25-Feb-2025-18:04:49 | ge100-0/0/11.3 | 0               | learn                     |
            | 25-Feb-2025-18:04:54 | ge100-0/0/11.1 | 1               |                           |
            | 25-Feb-2025-18:04:54 | ge100-0/0/11.2 | 2               |                           |
            | 25-Feb-2025-18:04:54 | ge100-0/0/11.3 | 3               |                           |
            | 25-Feb-2025-18:04:55 | ge100-0/0/11.1 | 4               |                           |
            | 25-Feb-2025-18:04:55 | ge100-0/0/11.2 | 5               |                           |
            | 25-Feb-2025-18:04:55 |                | 0               | ge100-0/0/11.3 remains up |
            +----------------------+----------------+-----------------+---------------------------+


**Help line:** Display loop-prevention information

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 25.1    | Command introduced                  |
+---------+-------------------------------------+
