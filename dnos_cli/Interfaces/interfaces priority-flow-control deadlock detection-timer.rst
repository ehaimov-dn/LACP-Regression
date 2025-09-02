interfaces priority-flow-control deadlock detection-timer
---------------------------------------------------------

**Minimum user role:** operator

If the queue is always in the PFC-XOFF (flow-controlled) state within the specified PFC deadlock detection period, the system determines that a PFC deadlock occurs. 
In this case, the PFC deadlock recovery process needs to be performed.

To configure the priority-based flow control deadlock detection-timer on the interface:

**Command syntax: detection-timer [detection-timer]**

**Command mode:** config

**Hierarchies**

- interfaces priority-flow-control deadlock

**Note**
- The user-configured value is in milliseconds, but the actual value that is set in the hardware is converted to the closest power of 2 in core clock cycles.
- The PFC deadlock detection-timer must be enabled (greater than 0) for the PFC deadlock feature to be enabled and for the recovery-timer configuration to be valid.
- This configuration must be set with the same value on all applicable ports sharing the same CDU (e.g., breakout interfaces), so that it will not be overriden.

**Parameter table**

+-----------------+----------------------------------------------------------------------------------+-------+---------+
| Parameter       | Description                                                                      | Range | Default |
+=================+==================================================================================+=======+=========+
| detection-timer | The priority-based flow control deadlock detecction timer in milliseconds.       | 0-512 | 0       |
|                 | Specifies the duration of the PFC XOFF state to indicate the PFC deadlock        |       |         |
|                 | condition is present.                                                            |       |         |
+-----------------+----------------------------------------------------------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/0/1
    dnRouter(cfg-if-ge100-1/0/1)# priority-flow-control
    dnRouter(cfg-if-ge100-1/0/1-pfc)# deadlock
    dnRouter(cfg-if-ge100-1/0/1-pfc-deadlock)# detection-timer 8


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-ge100-1/0/12-pfc-deadlock)# no detection-timer

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+
