show system patches
-------------------

**Minimum user role:** viewer

To display information on DNOS patch stacks, installed and loaded to target and revert stacks:


**Command syntax: show system patches**

**Command mode:** operational


**Note**

- DNOS supports hot-patches to quickly resolve severe issues detected in a specific customer environment.

- Hot-patches can be non-traffic affecting, control-traffic affecting or traffic affecting; it depends on the specific case.

- Non-traffic and some control-traffic affecting hot-patches eliminate the need for maintenance windows. Traffic affecting hot-patches may still require a short maintenance window.


**Parameter table**

For each patch, the following information is displayed:

+-------------------+---------------------------------------------------+-------------------+
| Parameter         | Description                                       | Range             |
+===================+===================================================+===================+
| Patch Name        | The name of the patch package                     |                   |
+-------------------+---------------------------------------------------+-------------------+
| Target Component  | The software component affected by the patch      |                   |
+-------------------+---------------------------------------------------+-------------------+
| Version           | The component patch version                       |                   |
+-------------------+---------------------------------------------------+-------------------+
| Impact            | The impact of patch execution                     | NONE              |
|                   |                                                   | CONTROL           |
|                   |                                                   | TRAFFIC           |
+-------------------+---------------------------------------------------+-------------------+
| Affected Services | The services that are updated by the patch        |                   |
+-------------------+---------------------------------------------------+-------------------+
| Description       | Patch package description line                    |                   |
+-------------------+---------------------------------------------------+-------------------+

**Example**
::

	dnRouter# show system patches

	Current stack:

	| Patch Name               | Target Component   | Version           | Impact   | Affected Services   | Description            |
	|--------------------------+--------------------+-------------------+----------+---------------------+------------------------|
	| update_18.2.7.9_re_patch | DNOS               | 18.2.7.9_re_patch | CONTROL  | routing-engine      | RE_Patch_dev_18.2.7.14 |

	Target stack:

	| Patch Name               | Target Component   | Version           | Impact   | Affected Services   | Description            |
	|--------------------------+--------------------+-------------------+----------+---------------------+------------------------|
	| update_18.2.7.9_re_patch | DNOS               | 18.2.7.9_re_patch | CONTROL  | routing-engine      | RE_Patch_dev_18.2.7.14 |

	Revert stack:

	| Patch Name   | Target Component   | Version   | Impact   | Affected Services   | Description   |
	|--------------+--------------------+-----------+----------+---------------------+---------------|


.. **Help line:** show system patches

**Command History**

+---------+---------------------------------+
| Release | Modification                    |
+=========+=================================+
| 25.1    | Command introduced              |
+---------+---------------------------------+


