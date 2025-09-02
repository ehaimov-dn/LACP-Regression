show ospfv3 route
-----------------

**Minimum user role:** viewer

To display OSPFv3 routes, as determined by the most recent SPF calculation.



**Command syntax: show ospfv3 route** prefix [ipv6-prefix]

**Command mode:** operational

**Parameter table**

+--------------------+--------------------------------------------------------------------+------------------------------+----------------+
| Parameter          | Description                                                        | Values                       | Default value  |
+====================+====================================================================+==============================+================+
| ipv6-prefix        | Display OSPFv3 routing information for a specific prefix           | A:B:C:D:E:F:G:H/M            | all prefixes   |
+--------------------+--------------------------------------------------------------------+------------------------------+----------------+

**Example**
::

  dnRouter# show ospfv3 route

  Codes: * - Best route via OSPFv3
         IA - Inter area, D - Discard
         E1 - External type 1, E2 - External type 2

  *      3:14:33::/120                                            cost [1/0],  area: 0.0.0.0
                                                                  via ::, ge100-0/0/0
  *      1111::1111/128                                           cost [1/0],  area: 0.0.0.0
                                                                  via fe80::a8c1:abff:fe66:bada, ge100-0/0/0
  *      2000:33::/120                                            cost [1/0],  area: 0.0.0.0
                                                                  via ::, ge100-0/0/0
  *      2222::2222/128                                           cost [0/0],  area: 0.0.0.0
                                                                  via ::, lo0
  *      4000:33::/120                                            cost [1/0],  area: 0.0.0.0
                                                                  via ::, ge100-0/0/0
  *      4444::4444/128                                           cost [1/0],  area: 0.0.0.0
                                                                  via fe80::a8c1:abff:fefc:3407, ge100-0/0/0
  *      5000:33::/120                                            cost [1/0],  area: 0.0.0.0
                                                                  via ::, ge100-0/0/0
  *      5555::5555/128                                           cost [1/0],  area: 0.0.0.0
                                                                  via fe80::1897:3ff:feff:1, ge100-0/0/0


  dnRouter# show ospfv3 route prefix  5000:33::/120

  Codes: * - Best route via OSPFv3
         IA - Inter area, D - Discard
         E1 - External type 1, E2 - External type 2

  *      5000:33::/120                                            cost [1/0],  area: 0.0.0.0
                                                                  via ::, ge100-0/0/0

.. **Help line:** Displays the OSPFv3 route information.

**Command History**

+---------+------------------------------------+
| Release | Modification                       |
+=========+====================================+
| 11.6    | Command introduced                 |
+---------+------------------------------------+
| TBD     | Added ipv6-prefix parameter        |
+---------+------------------------------------+

