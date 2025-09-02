interfaces priority-flow-control deadlock
-----------------------------------------

**Minimum user role:** operator

PFC deadlock is a network state in which congestion occurs on multiple switches simultaneously due to a loop or other causes. The interface buffer usage of each switch 
exceeds the threshold, the switches wait for each other to release resources, and data flows on all switches are permanently blocked consequently. 
This feature periodically detects whether the device is in the PFC deadlock state. If an interface is always in the PFC XOFF state within the PFC deadlock detection 
interval, the device enters the PFC deadlock state. If PFC deadlock detection is recovered in automatic mode, the device automatically releases the deadlock state and 
recovers PFC and PFC deadlock detection after the delay timer expires. During the delay timer period, the device disables PFC and PFC deadlock detection on the interface,
so that packets can be forwarded properly.

To enter the PFC deadlock configuration on an interface:

**Command syntax: deadlock**

**Command mode:** config

**Hierarchies**

- interfaces priority-flow-control

**Note**
- The command is applicable to physical interface types.

- You can view the PFC administrative state on an interface using the show interfaces detail command. See "show interfaces detail".

- To view PFC counters use the show PFC counters command. See "show priority-flow-control interfaces counters".

- To view PFC queues use the show PFC queues command. See "show priority-flow-control interfaces queues".

- The PFC deadlock configuration is applied for all traffic classes on the interface.

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-0/0/0
    dnRouter(cfg-if-ge100-0/0/0)# priority-flow-control
    dnRouter(cfg-if-ge100-0/0/0-pfc-deadlock)# deadlock


**Removing Configuration**

To revert all PFC deadlock settings to their default values:
::

    dnRouter(cfg-if-ge100-0/0/0-pfc)# no deadlock

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+
