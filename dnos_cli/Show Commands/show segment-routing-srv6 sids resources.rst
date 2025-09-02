show segment-routing-srv6 sids resources
----------------------------------------

**Minimum user role:** viewer

To display segment-routing srv6 sids resources:

**Command syntax: show segment-routing-srv6 sids resources**

**Command mode:** operational

..
	**Internal Note**
	
	-  

**Example**
::

  dnRouter# show segment-routing-srv6 sids resources
  CSID Blocks:
    fc00:0:/32
      Locators
        loc1, loc2
      Node range: 0x1 - 0xDFFF (57343)
      Dynamic alloctions
        range: 0xE000 - 0xFDFF (7680)
        BGP: 5
        ISIS: 60
        Total: 70
      Static allocations:
        range: 0xFE00 - 0xFFF0 (496)
        BGP: 5
        ISIS: 0
        Total: 5

    fc00:1:/32
      Locators
        loc3, loc4
      Node range: 0x1 - 0xDFFF (57343)
      Dynamic alloctions
        range: 0xE000 - 0xFDFF (7680)
        BGP: 5
        ISIS: 60
        Total: 70
      Static allocations:
        range: 0xFE00 - 0xFFF0 (496)
        BGP: 5
        ISIS: 0
        Total: 5
      
  Local SIDs Installed:
    BGP: 10
    ISIS: 120
    Connected: 3
    Total: 143

  Hardware Resources:
    TCAM: 123/2000
    ISEM: 140/8000
 
.. **Help line:** Displays segment-routing SRv6 sid resources information

**Command History**

+---------+-----------------------------------------------------------------------------------------------+
| Release | Modification                                                                                  |
+=========+===============================================================================================+
| 25.3    | Command introduced                                                                            |
+---------+-----------------------------------------------------------------------------------------------+
