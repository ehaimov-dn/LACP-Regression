interfaces access-list eth direction
------------------------------------

**Minimum user role:** operator

After creating an access-list, you can link it to an interface. 
When applying an access-list to an interface, you must specify whether it is to be applied to inbound or outbound traffic. 
You can configure only one access-list per direction for each access-list type.
The attachment of the policy to the interface will be rejected.

To apply an access-list to an interface, use the following command:

**Command syntax: access-list eth [access-list-name] direction [direction]**

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Bundle
  - Bundle vlan
  - Physical
  - Physical vlan
  - IRB.

**Parameter table**

+------------------+----------------------------------------------------------------------------------+-------+---------+
| Parameter        | Description                                                                      | Range | Default |
+==================+==================================================================================+=======+=========+
| access-list-name | Specify the name of an existing access-list. This access-list will serve as a    | \-    | \-      |
|                  | global access-list.                                                              |       |         |
+------------------+----------------------------------------------------------------------------------+-------+---------+
| direction        | The direction of the traffic to which to apply the access-list. For mgmt         | in    | \-      |
|                  | interfaces, you can configure only an ingress access-list.                       |       |         |
+------------------+----------------------------------------------------------------------------------+-------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# bundle-1
    dnRouter(cfg-if-bundle-1)# access-list eth MyAccess-list-eth direction in

    dnRouter(cfg-if)# bundle-1.10
    dnRouter(cfg-if-bundle-1.10)# access-list eth MyAccess-list-eth direction in

    dnRouter(cfg-if)# ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# access-list eth MyAccess-list-eth direction in

    dnRouter(cfg-if)# ge100-1/1/1.20
    dnRouter(cfg-if-ge100-1/1/1.20)# access-list eth MyAccess-list-eth direction in

    dnRouter(cfg-if)# irb0
    dnRouter(cfg-if-irb0)# access-list eth MyAccess-listeth direction in


**Removing Configuration**

To remove all the access lists from the interface:
::

    dnRouter(cfg-if-ge100-1/1/1)# # no access-list

To remove all eth access-lists from the interface:
::

    dnRouter(cfg-if-ge100-1.20)# no access-list eth

To remove a specific access-list from the interface:
::

    dnRouter(cfg-if-bundle-2)# no access-list eth MyAccess-listeth

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 19.3    | Command introduced |
+---------+--------------------+
