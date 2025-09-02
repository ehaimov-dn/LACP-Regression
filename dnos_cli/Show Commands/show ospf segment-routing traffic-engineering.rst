show ospf segment-routing traffic-engineering
---------------------------------------------

**Minimum user role:** viewer

To display the OSPF segment-routing traffic-engineering database:


**Command syntax: show ospf** instance [ospf-instance-name] **segment-routing traffic-engineering** [area <A.B.C.D or 0-4294967295>] [router-id <A.B.C.D>]

**Command mode:** operational


**Note**

    - use "instance [ospf-instance-name]" to display information from a specific OSPF instance, when not specified, display information from all OSPF instances
    - use "area <A.B.C.D or 0-4294967295>" to display information from a specific OSPF area, ignored if OSPF instance is not specified
    - use "router-id <A.B.C.D>" to display information from a specific OSPF router-id, ignored if OSPF instance or area is not specified

**Parameter table**

+--------------------+--------------------------------------------------------------------+------------------------------+----------------+
| Parameter          | Description                                                        | Values                       | Default value  |
+====================+====================================================================+==============================+================+
| ospf-instance-name | Filters the displayed information to a specific OSPF instance      | Configured instances names   | all            |
+--------------------+--------------------------------------------------------------------+------------------------------+----------------+
| area               | Filters the displayed information to a specific area               | <A.B.C.D or 0-4294967295>    | all            |
+--------------------+--------------------------------------------------------------------+------------------------------+----------------+
| router-id          | Filters the displayed information to a specific router             | <A.B.C.D>                    | all            |
+--------------------+--------------------------------------------------------------------+------------------------------+----------------+



**Example**
::

    dnRouter# show ospf segment-routing traffic-engineering
    OSPF Instance ospf-1
    Area: 0.0.0.0

    Nodes
    1.1.1.1, SRGB (Base: 16000, Range: 8000), algorithms spf strict-spf
    2.2.2.2, SRGB (Base: 16000, Range: 8000), algorithms spf strict-spf
    3.3.3.3, SRGB (Base: 16000, Range: 8000), algorithms spf
    4.4.4.4, SRGB (Base: 16000, Range: 8000), algorithms spf strict-spf

    Links
    1.1.1.1 -> 2.2.2.2 [12.1.1.1] remote address 12.1.1.2, metric 20, sids: 258 (B); 259;
        Legacy TE Params: te-metric 20, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]
        ASLA SR-TE: te-metric 30, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]
        ASLA FLEX-ALGO: te-metric 40, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]

    1.1.1.1 -> 2.2.2.2 [12.2.1.1] remote address 12.2.1.2, metric 200, sids: 260 (B); 261;
        Legacy TE Params: te-metric 200, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0
        ASLA SR-TE: te-metric 200, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0
        ASLA FLEX-ALGO: te-metric 200, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0

    1.1.1.1 -> 2.2.2.2 [12.3.1.1] remote address 12.3.1.2, metric 20, sids: 262 (B); 263;
        Legacy TE Params: te-metric 20, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]
        ASLA SR-TE: te-metric 20, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]
        ASLA FLEX-ALGO: te-metric 20, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]

    1.1.1.1 -> 4.4.4.4 [14.1.1.1] remote address 14.1.1.4, metric 5, sids: 256 (B); 257;
        Legacy TE Params: te-metric 5, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]
        ASLA SR-TE: te-metric 15, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]
        ASLA FLEX-ALGO: te-metric 25, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]

    2.2.2.2 -> 1.1.1.1 [12.1.1.2] remote address 12.1.1.1, metric 20, sids: 258 (B); 259;
    2.2.2.2 -> 1.1.1.1 [12.2.1.2] remote address 12.2.1.1, metric 200, sids: 262 (B); 263;
    2.2.2.2 -> 1.1.1.1 [12.3.1.2] remote address 12.3.1.1, metric 20, sids: 264 (B); 265;
    2.2.2.2 -> 4.4.4.4 [24.1.1.2] remote address 24.1.1.4, metric 5, sids: 256 (B); 257;
    3.3.3.3 -> 2.2.2.2 [23.1.1.3] remote address 23.1.1.2, metric <none>, sids: 24001;
        Legacy TE Params: admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]
        ASLA SR-TE: admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]

    3.3.3.3 -> 4.4.4.4 [34.1.1.3] remote address 34.1.1.4, metric <none>, sids: 24000;
    4.4.4.4 -> 1.1.1.1 [14.1.1.4] remote address 14.1.1.1, metric 5, sids: 24001;
        Legacy TE Params: admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]
        ASLA FLEX-ALGO: admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]

    4.4.4.4 -> 2.2.2.2 [24.1.1.4] remote address 24.1.1.2, metric 5, sids: 24002;
        Legacy TE Params: te-metric 200, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0
        ASLA FLEX-ALGO: te-metric 400, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0

    Prefixes
    1.1.1.1/32:1.1.1.1
    metric 1
    algo spf, sid 1 node
    algo strict-spf, sid 11 node

    2.2.2.2/32:2.2.2.2
    metric 1
    algo spf, sid 2 node
    algo strict-spf, sid 22 node

    3.3.3.3/32:3.3.3.3
    metric 1
    algo spf, sid 3 node

    4.4.4.4/32:4.4.4.4
    metric 1
    algo spf, sid 4 node
    algo strict-spf, sid 44 node

    OSPF Instance ospf-2
    Area: 0.0.0.0

    Nodes
    1.1.1.1, SRGB (Base: 16000, Range: 8000), algorithms spf strict-spf
    22.22.22.22, SRGB (Base: 16000, Range: 8000), algorithms spf strict-spf
    33.33.33.33, SRGB (Base: 16000, Range: 8000), algorithms spf

    Links
    1.1.1.1 -> 22.22.22.22 [121.1.1.1] remote address 121.1.1.2, metric 10, sids: 258 (B); 259;
        Legacy TE Params: te-metric 30, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]
        ASLA LFA: te-metric 40, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]

    1.1.1.1 -> 22.22.22.22 [121.2.1.1] remote address 121.2.1.2, metric 100, sids: 260 (B); 261;
        Legacy TE Params: te-metric 300, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0
        ASLA LFA: te-metric 300, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0

    1.1.1.1 -> 22.22.22.22 [121.3.1.1] remote address 121.3.1.2, metric 20, sids: 262 (B); 263;
        Legacy TE Params: te-metric 20, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]
        ASLA LFA: te-metric 20, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]

    22.22.22.22 -> 1.1.1.1 [121.1.1.2] remote address 121.1.1.1, metric 10, sids: 258 (B); 259;
    22.22.22.22 -> 1.1.1.1 [121.2.1.2] remote address 121.2.1.1, metric 100, sids: 262 (B); 263;
    22.22.22.22 -> 1.1.1.1 [121.3.1.2] remote address 121.3.1.1, metric 20, sids: 264 (B); 265;
    33.33.33.33 -> 22.22.22.22 [223.1.1.3] remote address 223.1.1.2, metric <none>, sids: 24001;
        Legacy TE Params: admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]
        ASLA LFA: admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111, 2222]

    Prefixes
    1.1.1.1/32:1.1.1.1
    metric 1
    algo spf, sid 1 node
    algo strict-spf, sid 11 node

    22.22.22.22/32:22.22.22.22
    metric 1
    algo spf, sid 22 node
    algo strict-spf, sid 222 node

    33.33.33.33/32:33.33.33.33
    metric 1
    algo spf, sid 33 node


    dnRouter# show ospf instance ospf-1 segment-routing traffic-engineering
    OSPF Instance ospf-1
    Area: 0.0.0.0

    Nodes
    1.1.1.1, SRGB (Base: 16000, Range: 8000), algorithms spf strict-spf
    2.2.2.2, SRGB (Base: 16000, Range: 8000), algorithms spf strict-spf
    3.3.3.3, SRGB (Base: 16000, Range: 8000), algorithms spf
    4.4.4.4, SRGB (Base: 16000, Range: 8000), algorithms spf strict-spf

    Links
    1.1.1.1 -> 2.2.2.2 [12.1.1.1] remote address 12.1.1.2, metric 20, sids: 258 (B); 259;
        Legacy TE Params: te-metric 20, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]
        ASLA SR-TE: te-metric 20, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111, 2222]

    1.1.1.1 -> 2.2.2.2 [12.2.1.1] remote address 12.2.1.2, metric 200, sids: 260 (B); 261;
        Legacy TE Params: te-metric 200, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0
        ASLA SR-TE: te-metric 200, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0

    1.1.1.1 -> 2.2.2.2 [12.3.1.1] remote address 12.3.1.2, metric 20, sids: 262 (B); 263;
        Legacy TE Params: te-metric 20, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]
        ASLA SR-TE: te-metric 20, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]

    1.1.1.1 -> 4.4.4.4 [14.1.1.1] remote address 14.1.1.4, metric 5, sids: 256 (B); 257;
        Legacy TE Params: te-metric 5, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]
        ASLA SR-TE: te-metric 10, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111, 3333]

    2.2.2.2 -> 1.1.1.1 [12.1.1.2] remote address 12.1.1.1, metric 20, sids: 258 (B); 259;
    2.2.2.2 -> 1.1.1.1 [12.2.1.2] remote address 12.2.1.1, metric 200, sids: 262 (B); 263;
    2.2.2.2 -> 1.1.1.1 [12.3.1.2] remote address 12.3.1.1, metric 20, sids: 264 (B); 265;
    2.2.2.2 -> 4.4.4.4 [24.1.1.2] remote address 24.1.1.4, metric 5, sids: 256 (B); 257;
    3.3.3.3 -> 2.2.2.2 [23.1.1.3] remote address 23.1.1.2, metric <none>, sids: 24001;
        Legacy TE Params: admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]
        ASLA SR-TE: admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]

    3.3.3.3 -> 4.4.4.4 [34.1.1.3] remote address 34.1.1.4, metric <none>, sids: 24000;
    4.4.4.4 -> 1.1.1.1 [14.1.1.4] remote address 14.1.1.1, metric 5, sids: 24001;
        Legacy TE Params: admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]
        ASLA SR-TE: admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]

    4.4.4.4 -> 2.2.2.2 [24.1.1.4] remote address 24.1.1.2, metric 5, sids: 24002;
        Legacy TE Params: te-metric 200, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0
        ASLA SR-TE: te-metric 200, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0

    Prefixes
    1.1.1.1/32:1.1.1.1
    metric 1
    algo spf, sid 1 node
    algo strict-spf, sid 11 node

    2.2.2.2/32:2.2.2.2
    metric 1
    algo spf, sid 2 node
    algo strict-spf, sid 22 node

    3.3.3.3/32:3.3.3.3
    metric 1
    algo spf, sid 3 node

    4.4.4.4/32:4.4.4.4
    metric 1
    algo spf, sid 4 node
    algo strict-spf, sid 44 node


    dnRouter# show ospf instance ospf-1 segment-routing traffic-engineering area 0
    OSPF Instance ospf-1
    Area: 0.0.0.0

    Nodes
    1.1.1.1, SRGB (Base: 16000, Range: 8000), algorithms spf strict-spf
    2.2.2.2, SRGB (Base: 16000, Range: 8000), algorithms spf strict-spf
    3.3.3.3, SRGB (Base: 16000, Range: 8000), algorithms spf
    4.4.4.4, SRGB (Base: 16000, Range: 8000), algorithms spf strict-spf

    Links
    1.1.1.1 -> 2.2.2.2 [12.1.1.1] remote address 12.1.1.2, metric 20, sids: 258 (B); 259;
        Legacy TE Params: te-metric 20, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]
        ASLA SR-TE: te-metric 40, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]

    1.1.1.1 -> 2.2.2.2 [12.2.1.1] remote address 12.2.1.2, metric 200, sids: 260 (B); 261;
        Legacy TE Params: te-metric 200, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0
        ASLA SR-TE: te-metric 200, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0

    1.1.1.1 -> 2.2.2.2 [12.3.1.1] remote address 12.3.1.2, metric 20, sids: 262 (B); 263;
        Legacy TE Params: te-metric 20, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]
        ASLA SR-TE: te-metric 40, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]

    1.1.1.1 -> 4.4.4.4 [14.1.1.1] remote address 14.1.1.4, metric 5, sids: 256 (B); 257;
        Legacy TE Params: te-metric 5, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]
        ASLA SR-TE: te-metric 5, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111, 2222]

    2.2.2.2 -> 1.1.1.1 [12.1.1.2] remote address 12.1.1.1, metric 20, sids: 258 (B); 259;
    2.2.2.2 -> 1.1.1.1 [12.2.1.2] remote address 12.2.1.1, metric 200, sids: 262 (B); 263;
    2.2.2.2 -> 1.1.1.1 [12.3.1.2] remote address 12.3.1.1, metric 20, sids: 264 (B); 265;
    2.2.2.2 -> 4.4.4.4 [24.1.1.2] remote address 24.1.1.4, metric 5, sids: 256 (B); 257;
    3.3.3.3 -> 2.2.2.2 [23.1.1.3] remote address 23.1.1.2, metric <none>, sids: 24001;
        Legacy TE Params: admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]
        ASLA SR-TE: admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]

    3.3.3.3 -> 4.4.4.4 [34.1.1.3] remote address 34.1.1.4, metric <none>, sids: 24000;
    4.4.4.4 -> 1.1.1.1 [14.1.1.4] remote address 14.1.1.1, metric 5, sids: 24001;
        Legacy TE Params: admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]
        ASLA SR-TE: admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]

    4.4.4.4 -> 2.2.2.2 [24.1.1.4] remote address 24.1.1.2, metric 5, sids: 24002;
        Legacy TE Params: te-metric 200, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0
        ASLA SR-TE: te-metric 200, admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0

    Prefixes
    1.1.1.1/32:1.1.1.1
    metric 1
    algo spf, sid 1 node
    algo strict-spf, sid 11 node

    2.2.2.2/32:2.2.2.2
    metric 1
    algo spf, sid 2 node
    algo strict-spf, sid 22 node

    3.3.3.3/32:3.3.3.3
    metric 1
    algo spf, sid 3 node

    4.4.4.4/32:4.4.4.4
    metric 1
    algo spf, sid 4 node
    algo strict-spf, sid 44 node


    dnRouter# show ospf instance ospf-1 segment-routing traffic-engineering area 0 router-id 3.3.3.3
    OSPF Instance ospf-1
    Area: 0.0.0.0

    Nodes
    3.3.3.3, SRGB (Base: 16000, Range: 8000), algorithms spf

    Links
    3.3.3.3 -> 2.2.2.2 [23.1.1.3] remote address 23.1.1.2, metric <none>, sids: 24001;
        Legacy TE Params: admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]
        ASLA SR-TE: admin-groups 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0, srlg [1111]

    3.3.3.3 -> 4.4.4.4 [34.1.1.3] remote address 34.1.1.4, metric <none>, sids: 24000;

    Prefixes
    3.3.3.3/32:3.3.3.3
    metric 1
    algo spf, sid 3 node


.. **Help line:**

**Command History**

+---------+-------------------------------------------+
| Release | Modification                              |
+=========+===========================================+
| 25.2    | Command introduced                        |
+---------+-------------------------------------------+
