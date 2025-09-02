show interfaces counters drops
------------------------------

**Minimum user role:** viewer

This command displays L2 and L3 forwarding statistics, showing only interfaces that have drops. You can further filter to show only interfaces with RX drops, TX drops, or both.

**Command syntax: show interfaces counters drops** [rx] [tx]

**Command mode:** operational

**Parameter table**

+----------------+----------------------------------------------------------+---------------------------------------+---------+
| Parameter      | Description                                              | Range                                 | Default |
+================+==========================================================+=======================================+=========+
| rx             | Show only interfaces with RX drops                       | -                                     | -       |
+----------------+----------------------------------------------------------+---------------------------------------+---------+
| tx             | Show only interfaces with TX drops                       | -                                     | -       |
+----------------+----------------------------------------------------------+---------------------------------------+---------+

The following information is displayed per interface:

+-----------------+-------------------------------------------------------------------------------------+
| Attribute       | Description                                                                         |
+=================+=====================================================================================+
| Interface       | The name of the interface                                                           |
+-----------------+-------------------------------------------------------------------------------------+
| Operational     | The state of the link (up/down)                                                     |
+-----------------+-------------------------------------------------------------------------------------+
| Rx (Mbps)       | The received Megabits per second                                                    |
+-----------------+-------------------------------------------------------------------------------------+
| Tx (Mbps)       | The transmitted Megabits per second                                                 |
+-----------------+-------------------------------------------------------------------------------------+
| Rx (pkts)       | The received packets                                                                |
+-----------------+-------------------------------------------------------------------------------------+
| Tx (pkts)       | The transmitted packets                                                             |
+-----------------+-------------------------------------------------------------------------------------+
| Rx drops (pkts) | The number of received packets that were dropped                                    |
+-----------------+-------------------------------------------------------------------------------------+
| Tx drops (pkts) | The number of transmitted packets that were dropped                                 |
+-----------------+-------------------------------------------------------------------------------------+

**Usage Guidelines:**

- If no optional parameters are specified, the command shows all interfaces that have either RX or TX drops
- If 'rx' is specified, only interfaces with RX drops are shown
- If 'tx' is specified, only interfaces with TX drops are shown
- If both 'rx' and 'tx' are specified, only interfaces with both RX and TX drops are shown

**Example**
::

	dnRouter# show interfaces counters drops

	| Interface    | Operational | RX[Mbps] | TX[Mbps] | RX[pkts] | TX[pkts] | RX drops[pkts] | TX drops[pkts] |
	|--------------+-------------+----------+----------+----------+----------+----------------+----------------|
	| ge100-1/0/1  | up          | 100      | 50       | 1000     | 500      | 10             | 5              |
	| bundle-2     | up          | 200      | 150      | 2000     | 1500     | 20             | 0              |
	| ge100-1/1/2  | up          | 150      | 100      | 1500     | 1000     | 0              | 15             |

	dnRouter# show interfaces counters drops rx

	| Interface    | Operational | RX[Mbps] | TX[Mbps] | RX[pkts] | TX[pkts] | RX drops[pkts] | TX drops[pkts] |
	|--------------+-------------+----------+----------+----------+----------+----------------+----------------|
	| ge100-1/0/1  | up          | 100      | 50       | 1000     | 500      | 10             | 5              |
	| bundle-2     | up          | 200      | 150      | 2000     | 1500     | 20             | 0              |

	dnRouter# show interfaces counters drops tx

	| Interface    | Operational | RX[Mbps] | TX[Mbps] | RX[pkts] | TX[pkts] | RX drops[pkts] | TX drops[pkts] |
	|--------------+-------------+----------+----------+----------+----------+----------------+----------------|
	| ge100-1/0/1  | up          | 100      | 50       | 1000     | 500      | 10             | 5              |
	| bundle-2     | up          | 200      | 150      | 2000     | 1500     | 20             | 0              |

	dnRouter# show interfaces counters drops rx tx

	| Interface    | Operational | RX[Mbps] | TX[Mbps] | RX[pkts] | TX[pkts] | RX drops[pkts] | TX drops[pkts] |
	|--------------+-------------+----------+----------+----------+----------+----------------+----------------|
	| ge100-1/0/1  | up          | 100      | 50       | 1000     | 500      | 10             | 5              |

**Command History**

+---------+----------------------------------------------------------+
| Release | Modification                                             |
+=========+==========================================================+
| TBD     | Command introduced                                       |
+---------+----------------------------------------------------------+

.. **Help line:** Displays counters for the interface(s) with drops