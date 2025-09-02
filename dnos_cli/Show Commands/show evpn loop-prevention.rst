show evpn loop-prevention
-------------------------

**Minimum user role:** operator

To show the detailed information of an EVPN instance.

**Command syntax: show evpn loop-prevention** instance [service-name] local
**Command syntax: show evpn** instance [service-name] loop-prevention local
**Command syntax: show evpn loop-prevention** instance [service-name] interface local
**Command syntax: show evpn** instance [service-name] loop-prevention interface local
**Command syntax: show evpn loop-prevention** instance [service-name] interface [interface-name-service] local
**Command syntax: show evpn** instance [service-name] loop-prevention interface [interface-name-service] local
**Command syntax: show evpn loop-prevention** instance [service-name] mac-table local
**Command syntax: show evpn** instance [service-name] loop-prevention mac-table local
**Command syntax: show evpn loop-prevention** instance [service-name] mac-table [mac-address] local
**Command syntax: show evpn** instance [service-name] loop-prevention mac-table [mac-address] local

**Command mode:** operational

**Parameter table:**

+------------------------+-----------------------------------------+-------------------+---------------+
| Parameter              | Description                             | Values            | Default value |
+========================+=========================================+===================+===============+
| service-name           | Service name                            | String            | \-            |
+------------------------+-----------------------------------------+-------------------+---------------+
| interface-name-service | Evpn attachment circuit inside service  | String            | \-            |
+------------------------+-----------------------------------------+-------------------+---------------+
| mac-address            | Display information about MAC address   | xx:xx:xx:xx:xx:xx | \-            |
+------------------------+-----------------------------------------+-------------------+---------------+

**Note:**
The commands accept `loop-prevention` either before or after `instance`.


**Example**
::

    dev-dnRouter# show evpn loop-prevention instance evpn_1 local

    EVPN: evpn_1

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
        | 04:00:00:00:00:00 | 0 / 5                       |
        +-------------------+-----------------------------+

        +---------------------+----------+-------------------------+
        | Shutdown Interfaces | Status   | Remaining Shutdown Time |
        +---------------------+----------+-------------------------+
        | ge100-0/0/12.1      | Shutdown | N/A                     |
        | ge100-0/0/12.2      | Shutdown | N/A                     |
        +---------------------+----------+-------------------------+


    dev-dnRouter# show evpn loop-prevention instance evpn_1 interface local

    EVPN: evpn_1
        +---------------------+----------+-------------------------+
        | Shutdown Interfaces | Status   | Remaining Shutdown Time |
        +---------------------+----------+-------------------------+
        | ge100-0/0/12.1      | Shutdown | N/A                     |
        | ge100-0/0/12.2      | Shutdown | N/A                     |
        +---------------------+----------+-------------------------+


    dev-dnRouter# show evpn loop-prevention instance evpn_1 interface ge100-0/0/12.1 local

    EVPN: evpn_1
    Interface: ge100-0/0/12.1

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
            | 25-Feb-2025-10:41:06 | Shutdown | 0 / restore-manually | MAC Address 02:00:00:00:00:00 |
            +----------------------+----------+----------------------+-------------------------------+


    dev-dnRouter# show evpn loop-prevention instance evpn_1 mac-table local

        +-------------------+-----------------------------+
        | MAC Address       | Mac Moves in Window / Limit |
        +-------------------+-----------------------------+
        | 02:00:00:00:00:00 | 0 / 5                       |
        | 04:00:00:00:00:00 | 0 / 5                       |
        +-------------------+-----------------------------+


    dev-dnRouter# show evpn loop-prevention instance evpn_1 mac-table 02:00:00:00:00:00 local

    EVPN: evpn_1 id: evi_id=1, eth_tag=0
    Mac-Address: 02:00:00:00:00:00

          Local Loop Prevention
          =====================

          Move History
          ------------

            +----------------------+----------------+-----------------+---------------------------+
            | Time                 | Interface      | Sequence Number | Comment                   |
            +----------------------+----------------+-----------------+---------------------------+
            | 25-Feb-2025-10:41:02 | ge100-0/0/12.3 | 0               | learn                     |
            | 25-Feb-2025-10:41:05 | ge100-0/0/12.1 | 1               |                           |
            | 25-Feb-2025-10:41:05 | ge100-0/0/12.2 | 2               |                           |
            | 25-Feb-2025-10:41:05 | ge100-0/0/12.3 | 3               |                           |
            | 25-Feb-2025-10:41:05 | ge100-0/0/12.1 | 4               |                           |
            | 25-Feb-2025-10:41:06 | ge100-0/0/12.2 | 5               |                           |
            | 25-Feb-2025-10:41:06 |                | 0               | ge100-0/0/12.3 remains up |
        +----------------------+----------------+-----------------+---------------------------+


**Help line:** Display loop-prevention information

**Command History**

+---------+-------------------------------------+
| Release | Modification                        |
+=========+=====================================+
| 25.1    | Command introduced                  |
+---------+-------------------------------------+
