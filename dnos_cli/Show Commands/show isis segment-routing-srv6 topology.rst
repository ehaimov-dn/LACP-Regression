show isis segment-routing-srv6 topology
---------------------------------------

**Minimum user role:** viewer

To display the IS-IS SRv6 connectivity topology:

**Command syntax: show isis** instance [isis-instance-name] **segment-routing-srv6** **topology** {level [level] \| host-name \| [host-namex]}

**Command mode:** operational

.. **Note**

	- use "instance [isis-instance-name]" to display information from a specific ISIS instance, when not specified, display information from all isis instances

**Parameter table**

+--------------------+--------------------------------------------------------------------------------------------------------------------------+
| Parameter          | Description                                                                                                              |
+====================+==========================================================================================================================+
| isis-instance-name | Filters the displayed information to the specified instance                                                              |
+--------------------+--------------------------------------------------------------------------------------------------------------------------+
| level              | Filters information from a specific ISIS level (level-1 or level-2)                                                      |
+--------------------+--------------------------------------------------------------------------------------------------------------------------+
| host-name          | Filters information for only the specified host-name                                                                     |
+--------------------+--------------------------------------------------------------------------------------------------------------------------+

**Example**
::
      
  e2e_R1_1# show isis segment-routing-srv6 topology
  Instance 1
    SRv6 Topology Level-1:
      Nodes:
      Links:
      Prefixes:
      Sids:
    SRv6 Topology Level-2:
      Nodes:
        1111.1111.1111 - q1, ID: 1111::1113, SRv6-Capable, Algorithms: spf strict-spf
          MSD:[SRH Max SL: 10, SRH Max End Pop: 5, SRH Max H.encaps: 3, SRH Max H.insert: 3, SRH Max End D: 0]
        2222.2222.2222 - q2, ID: 1111::2222, SRv6-Capable, Algorithms: spf strict-spf
          MSD:[SRH Max SL: 10, SRH Max End Pop: 5, SRH Max H.encaps: 3, SRH Max H.insert: 3, SRH Max End D: 0]
        3333.3333.3333 - q3, ID: 1111::3333
        4444.4444.4444 - q4, ID: 1111::4444
      Links:
        1111.1111.1111 -> 2222.2222.2222 [1200::10 -> 1200::2] Llri[5440 -> 5445]
          Metric 10
          Sid: fc00:0:1:e002:: End.X NEXT-CSID PSP & USD Algorithm: spf Weight: 0; Sid Structure:[B: 32 N: 16 F: 16 A: 64];
        1111.1111.1111 -> 3333.3333.3333 [1300::10 -> 1300::3] Llri[5441 -> 5450]
          Metric 10
          Sid: fc00:0:1:e000:: End.X NEXT-CSID PSP & USD Algorithm: spf Weight: 0; Sid Structure:[B: 32 N: 16 F: 16 A: 64];
        2222.2222.2222 -> 1111.1111.1111 [1200::2 -> 1200::10] Llri[5445 -> 5440]
          Metric 10
          Sid: fc00:0:2:e002:: End.X NEXT-CSID PSP & USD Algorithm: spf Weight: 0; Sid Structure:[B: 32 N: 16 F: 16 A: 64];
        2222.2222.2222 -> 4444.4444.4444 [4200::2 -> 4200::4] Llri[5446 -> 5455]
          Metric 10
          Sid: fc00:0:2:e000:: End.X NEXT-CSID PSP & USD Algorithm: spf Weight: 0; Sid Structure:[B: 32 N: 16 F: 16 A: 64];
        3333.3333.3333 -> 1111.1111.1111 [1300::3 -> 1300::10] Llri[5450 -> 5441]
          Metric 10
        3333.3333.3333 -> 4444.4444.4444 [4300::3 -> 4300::4] Llri[5451 -> 5456]
          Metric 10
        4444.4444.4444 -> 2222.2222.2222 [4200::4 -> 4200::2] Llri[5455 -> 5446]
          Metric 10
        4444.4444.4444 -> 3333.3333.3333 [4300::4 -> 4300::3] Llri[5456 -> 5451]
          Metric 10
      Prefixes:
        1111::1111/128 : 1111.1111.1111 - Metric 0
        1111::2222/128 : 2222.2222.2222 - Metric 0
        1111::3333/128 : 3333.3333.3333 - Metric 0
        1111::4444/128 : 4444.4444.4444 - Metric 0
        1200::/120 : 1111.1111.1111 - Metric 10
        1200::/120 : 2222.2222.2222 - Metric 10
        1300::/120 : 1111.1111.1111 - Metric 10
        1300::/120 : 3333.3333.3333 - Metric 10
        4200::/120 : 2222.2222.2222 - Metric 10
        4200::/120 : 4444.4444.4444 - Metric 10
        4300::/120 : 3333.3333.3333 - Metric 10
        4300::/120 : 4444.4444.4444 - Metric 10
        fc00:0:1::/48 : 1111.1111.1111 - Metric 1
        fc00:0:2::/48 : 2222.2222.2222 - Metric 1 Locators:[Algo: spf Metric: 1 (D): 0]
      Sids:
        fc00:0:1:: : 1111.1111.1111 - Endpoint Behavior: End NEXT-CSID PSP & USD Flags: 0 Algorithm: spf Sid Structure:[B: 32 N: 16 F: 0 A: 80];
        fc00:0:2:: : 2222.2222.2222 - Endpoint Behavior: End NEXT-CSID PSP & USD Flags: 0 Algorithm: spf Sid Structure:[B: 32 N: 16 F: 0 A: 80];

  e2e_R1_1# show isis segment-routing-srv6 topology level level-2
  Instance 1
    SRv6 Topology Level-2:
      Nodes:
        1111.1111.1111 - q1, ID: 1111::1113, SRv6-Capable, Algorithms: spf strict-spf
          MSD:[SRH Max SL: 10, SRH Max End Pop: 5, SRH Max H.encaps: 3, SRH Max H.insert: 3, SRH Max End D: 0]
        2222.2222.2222 - q2, ID: 1111::2222, SRv6-Capable, Algorithms: spf strict-spf
          MSD:[SRH Max SL: 10, SRH Max End Pop: 5, SRH Max H.encaps: 3, SRH Max H.insert: 3, SRH Max End D: 0]
        3333.3333.3333 - q3, ID: 1111::3333
        4444.4444.4444 - q4, ID: 1111::4444
      Links:
        1111.1111.1111 -> 2222.2222.2222 [1200::10 -> 1200::2] Llri[5440 -> 5445]
          Metric 10
          Sid: fc00:0:1:e002:: End.X NEXT-CSID PSP & USD Algorithm: spf Weight: 0; Sid Structure:[B: 32 N: 16 F: 16 A: 64];
        1111.1111.1111 -> 3333.3333.3333 [1300::10 -> 1300::3] Llri[5441 -> 5450]
          Metric 10
          Sid: fc00:0:1:e000:: End.X NEXT-CSID PSP & USD Algorithm: spf Weight: 0; Sid Structure:[B: 32 N: 16 F: 16 A: 64];
        2222.2222.2222 -> 1111.1111.1111 [1200::2 -> 1200::10] Llri[5445 -> 5440]
          Metric 10
          Sid: fc00:0:2:e002:: End.X NEXT-CSID PSP & USD Algorithm: spf Weight: 0; Sid Structure:[B: 32 N: 16 F: 16 A: 64];
        2222.2222.2222 -> 4444.4444.4444 [4200::2 -> 4200::4] Llri[5446 -> 5455]
          Metric 10
          Sid: fc00:0:2:e000:: End.X NEXT-CSID PSP & USD Algorithm: spf Weight: 0; Sid Structure:[B: 32 N: 16 F: 16 A: 64];
        3333.3333.3333 -> 1111.1111.1111 [1300::3 -> 1300::10] Llri[5450 -> 5441]
          Metric 10
        3333.3333.3333 -> 4444.4444.4444 [4300::3 -> 4300::4] Llri[5451 -> 5456]
          Metric 10
        4444.4444.4444 -> 2222.2222.2222 [4200::4 -> 4200::2] Llri[5455 -> 5446]
          Metric 10
        4444.4444.4444 -> 3333.3333.3333 [4300::4 -> 4300::3] Llri[5456 -> 5451]
          Metric 10
      Prefixes:
        1111::1111/128 : 1111.1111.1111 - Metric 0
        1111::2222/128 : 2222.2222.2222 - Metric 0
        1111::3333/128 : 3333.3333.3333 - Metric 0
        1111::4444/128 : 4444.4444.4444 - Metric 0
        1200::/120 : 1111.1111.1111 - Metric 10
        1200::/120 : 2222.2222.2222 - Metric 10
        1300::/120 : 1111.1111.1111 - Metric 10
        1300::/120 : 3333.3333.3333 - Metric 10
        4200::/120 : 2222.2222.2222 - Metric 10
        4200::/120 : 4444.4444.4444 - Metric 10
        4300::/120 : 3333.3333.3333 - Metric 10
        4300::/120 : 4444.4444.4444 - Metric 10
        fc00:0:1::/48 : 1111.1111.1111 - Metric 1
        fc00:0:2::/48 : 2222.2222.2222 - Metric 1 Locators:[Algo: spf Metric: 1 (D): 0]
      Sids:
        fc00:0:1:: : 1111.1111.1111 - Endpoint Behavior: End NEXT-CSID PSP & USD Flags: 0 Algorithm: spf Sid Structure:[B: 32 N: 16 F: 0 A: 80];
        fc00:0:2:: : 2222.2222.2222 - Endpoint Behavior: End NEXT-CSID PSP & USD Flags: 0 Algorithm: spf Sid Structure:[B: 32 N: 16 F: 0 A: 80];

  e2e_R1_1# show isis segment-routing-srv6 topology level level-2 host 1111.1111.1111
  Instance 1
  SRv6 Topology Level-2:
    Nodes:
      1111.1111.1111 - q1, ID: 1111::1113, SRv6-Capable, Algorithms: spf strict-spf
        MSD:[SRH Max SL: 10, SRH Max End Pop: 5, SRH Max H.encaps: 3, SRH Max H.insert: 3, SRH Max End D: 0]
    Links:
      1111.1111.1111 -> 2222.2222.2222 [1200::10 -> 1200::2] Llri[5440 -> 5445]
        Metric 10
        Sid: fc00:0:1:e002:: End.X NEXT-CSID PSP & USD Algorithm: spf Weight: 0; Sid Structure:[B: 32 N: 16 F: 16 A: 64];
      1111.1111.1111 -> 3333.3333.3333 [1300::10 -> 1300::3] Llri[5441 -> 5450]
        Metric 10
        Sid: fc00:0:1:e000:: End.X NEXT-CSID PSP & USD Algorithm: spf Weight: 0; Sid Structure:[B: 32 N: 16 F: 16 A: 64];
    Prefixes:
      1111::1111/128 : 1111.1111.1111 - Metric 0
      1200::/120 : 1111.1111.1111 - Metric 10
      1300::/120 : 1111.1111.1111 - Metric 10
      fc00:0:1::/48 : 1111.1111.1111 - Metric 1
    Sids:
      fc00:0:1:: : 1111.1111.1111 - Endpoint Behavior: End NEXT-CSID PSP & USD Flags: 0 Algorithm: spf Sid Structure:[B: 32 N: 16 F: 0 A: 80];
      fc00:0:2:: : 2222.2222.2222 - Endpoint Behavior: End NEXT-CSID PSP & USD Flags: 0 Algorithm: spf Sid Structure:[B: 32 N: 16 F: 0 A: 80];

.. **Help line:**

**Command History**

+---------+-----------------------------------------------------------+
| Release | Modification                                              |
+=========+===========================================================+
| 25.2    | Command introduced                                        |
+---------+-----------------------------------------------------------+
