show segment-routing srv6-local-sids
------------------------------------         

**Minimum user role:** viewer

To display segment-routing srv6 local-sids:

**Command syntax: show segment-routing policy** {locator [locator] owner [owner] prefix [prefix]}

**Command mode:** operational

**Parameter table**

+---------------------+---------------------------------------------------------------------------+
| Parameter           | Description                                                               |
+=====================+===========================================================================+
| locator             | Filters output per locator name.                                          |
+---------------------+---------------------------------------------------------------------------+
| owner               | Filters output per owner name.                                            |
+---------------------+---------------------------------------------------------------------------+
| prefix              | Filters output per specific prefix.                                       |
+---------------------+---------------------------------------------------------------------------+

**Example**
::

  dnRouter# show segment-routing srv6-local-sids


  dnRouter# show segment-routing srv6-local-sids locator loc1


  dnRouter# show segment-routing srv6-local-sids owner ISIS

  
  dnRouter# show segment-routing srv6-local-sids prefix fc00:0:1::/48


.. **Help line:** Displays segment-routing srv6 local-sids information

**Command History**

+---------+-----------------------------------------------------------------------------------------------+
| Release | Modification                                                                                  |
+=========+===============================================================================================+
| 25.2    | Command introduced                                                                            |
+---------+-----------------------------------------------------------------------------------------------+
