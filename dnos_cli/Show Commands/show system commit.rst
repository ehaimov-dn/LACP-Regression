show system commit
------------------

**Minimum user role:** viewer

To view the current confirmed-commit activity and commit history information on the system, use the following command:

**Command syntax: show system commit**

**Command mode:** operational

**Note**
- The commit history table displays commit information from the last successful commit operations. The information in the table is sorted from the latest to the oldest.

**Parameter table**

The following commit information is displayed in the table:

+---------------------+------------------------------------------------------------------------------+----------------+
| Parameter Name      | Description                                                                  | Values         |
+=====================+==============================================================================+================+
| Rollback ID         | The rollback-id of the commit transaction file.                              | Integer        |
+---------------------+------------------------------------------------------------------------------+----------------+
| Version             | running-configuration version after the commit                               | Integer        |
+---------------------+------------------------------------------------------------------------------+----------------+
| User                | The user that performed the commit                                           | String         |
+---------------------+------------------------------------------------------------------------------+----------------+
| Commit time         | The time when the commit was performed                                       | Timestamp      |
+---------------------+------------------------------------------------------------------------------+----------------+
| Commit origin       | The type of session that performed the commit                                | CLI/Netconf/.. |
+---------------------+------------------------------------------------------------------------------+----------------+
| Commit log message  | Optional commit log message provided by the user                             | String         |
+---------------------+------------------------------------------------------------------------------+----------------+

**Example**
::

	dnRouter# show system commit
	[14-Jul-2024 22:11:00 UTC] admin via cli confirmed-commit, rollback in 9 minutes

	Commit history:

	| Rollback ID | Version      | User       | Commit time                 | Commit origin   | Commit log message                                                           |
	|-------------+--------------+------------+-----------------------------+-----------------+------------------------------------------------------------------------------|
	| 0           | 42342        | admin      | 14-Jul-2024 22:11:00 UTC    | cli             |                                                                              |
	| 1           | 42341        | admin      | 12-Jul-2024 11:32:40 UTC    | cli             | user configuration log message                                               |
	| 2           | 42340        | john       | 11-Jul-2024 15:11:42 UTC    | cli             | my important commit                                                          |
	| 3           | 42339        | admin      | 10-Jul-2024 22:57:15 UTC    | netconf         |                                                                              |

	dnRouter# show system commit

	Commit history:

	| Rollback ID | Version      | User       | Commit time                 | Commit origin   | Commit log message                                                           |
	|-------------+--------------+------------+-----------------------------+-----------------+------------------------------------------------------------------------------|
	| 0           | 42342        | admin      | 14-Jul-2024 22:11:00 UTC    | cli             |                                                                              |
	| 1           | 42341        | admin      | 12-Jul-2024 11:32:40 UTC    | cli             | user configuration log message                                               |
	| 2           | 42340        | john       | 11-Jul-2024 15:11:42 UTC    | cli             | my important commit                                                          |
	| 3           | 42339        | admin      | 10-Jul-2024 22:57:15 UTC    | netconf         |                                                                              |

	dnRouter# show system commit
	no commits

.. **Help line:** display current confirmed-commit activity or running commit by other users and system commit history

**Command History**

+---------+----------------------------+
| Release | Modification               |
+=========+============================+
| 6.0     | Command introduced         |
+---------+----------------------------+
| 19.3    | Added commit history table |
+---------+----------------------------+

