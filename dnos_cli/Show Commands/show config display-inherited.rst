show config display-inherited
-----------------------------

**Minimum user role:** viewer

To view an output of all the user configuration including the inherited config from configuration groups.


**Command syntax: show config [level-1] [level-2] | display-inherited**

**Command mode:** operational



**Note**

- The output of this command displays only commands that have been explicitly configured (i.e. changed from the default) or inherited from Configuration Groups.

- The following CLI command extends the show config existing command with inherited config.

- * The configuration output is wrapped with **start** and **end** clauses as follows:

- The inherited configuraiton should be embedded inside the show config output marked with ## a line before the inherited block.

- During the inheritance calculation the command will be rejected with the following message "Inheritance rearrangement in-progress, please try again"

::

	# <system-name> config-start [%d-%b-%Y %H:%M:%S <timezone>]

	...
	## Inherited config from group <group-name>
	...

	# <system-name> config-end



The following are the features on which you can view the configuration:

+-------------+----------------------------------------------------------------------------------------------+------------------------------------------------+
| Feature     | Description                                                                                  | Reference                                      |
+=============+==============================================================================================+================================================+
| level       | Level 1 - The main menu hierarchy level (e.g. interfaces)                                    | See examples below                             |
|             | Level 2 - main menu sub-menu hierarchy (e.g. protocols ospf)                                 |                                                |
+-------------+----------------------------------------------------------------------------------------------+------------------------------------------------+
| defaults    | Display all configuration in the system, including ones with default values.                 | See Example 3 below                            |
|             | The default value of a changed parameter appears in square brackets alongside the new value. |                                                |
+-------------+----------------------------------------------------------------------------------------------+------------------------------------------------+
| interfaces  | Display interface configuration                                                              | show config interfaces                         |
+-------------+----------------------------------------------------------------------------------------------+------------------------------------------------+
| system      | Display system configuration                                                                 | show config system/show config defaults system |
+-------------+----------------------------------------------------------------------------------------------+------------------------------------------------+



**Example**
::

	dnRouter# show config

	# dnRouter config-start [30-Nov-2020 10:10:30 UTC]

	system
	  name dnRouter
	  login
	    user RootUser
	      description MyrootUser
	    !
	  !
	!

	#dnRouter config-end

	dnRouter# show config defaults | display-inherited

	# dnRouter config-start [30-Nov-2020 10:10:30 UTC]

	system
	  name dnRouter
	  login
	    user RootUser
	      description MyrootUser
	    !
	  !
	  logging
	    syslog
	      event-group all severity alert [warning]
	      facility local7
	    !
	  !
	!
	...
	interfaces
	  ge100-1/1/1
	    mtu 9200 [1514]
	    mpls enabled [disabled]
	    ## 'description' inherited from group 'group1'
	    ## 'speed' inherited from group 'group1'
	    description "group1 interface description"
	  !
	!

	#dnRouter config-end

	dnRouter# show config system | display-inherited

	# dnRouter config-start [30-Nov-2020 10:10:30 UTC]

	system
	  name dnRouter
	  login
	    user RootUser
	      description MyrootUser
	    !
	  !
	  ssh
	    server
	      ## 'admin-state' inherited from group 'group2'
	      admin-state enabled
	      !
        !
      !
	!

	#dnRouter config-end

.. **Help line:** show configuration with configuration inherited from Configuration Groups.

**Command History**

+---------+----------------------------------------------------------+
| Release | Modification                                             |
+=========+==========================================================+
| TBD     | Command introduced                                       |
+---------+----------------------------------------------------------+
