interfaces priority-flow-control traffic-class deadlock recovery-timer
----------------------------------------------------------------------

**Minimum user role:** operator

During PFC deadlock recovery, PFC frames received by the interface are ignored. The internal scheduler resumes traffic sending in the specified priority queue. 
After the recovery period expires, the normal flow control mechanism of PFC is resumed. If the system still determines that a deadlock occurs in the next deadlock 
detection period, the deadlock recovery process is performed again.

To configure the priority-based flow control deadlock recovery-timer on the interface:

**Command syntax: deadlock recovery-timer [deadlock-recovery-timer]**

**Command mode:** config

**Hierarchies**

- interfaces priority-flow-control traffic-class

**Note**
- The PFC deadlock detection-timer must be enabled (greater than 0) for the PFC deadlock feature to be enabled and for the recovery-timer configuration to be valid.
- If the PFC deadlock recovery timer is set to 0, then no action will be performed in case that a deadlock condition is detected.

**Parameter table**

+-------------------------+----------------------------------------------------------------------------------+---------+---------+
| Parameter               | Description                                                                      | Range   | Default |
+=========================+==================================================================================+=========+=========+
| deadlock-recovery-timer | The priority-based flow control deadlock recovery timer in milliseconds.         | 0-10000 | 0       |
|                         | Specifies the duration to ignore the PFC XOFF state and keep transmitting        |         |         |
|                         | traffic after entering PFC deadlock state.                                       |         |         |
+-------------------------+----------------------------------------------------------------------------------+---------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge100-1/0/1
    dnRouter(cfg-if-ge100-1/0/1)# priority-flow-control
    dnRouter(cfg-if-ge100-1/0/1-pfc)# traffic-class 5
    dnRouter(cfg-if-ge100-1/0/1-pfc-tc5)# deadlock recovery-timer 100


**Removing Configuration**

To revert to the default value:
::

    dnRouter(cfg-if-ge100-1/0/12-pfc-tc5)# no deadlock recovery-timer

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+
