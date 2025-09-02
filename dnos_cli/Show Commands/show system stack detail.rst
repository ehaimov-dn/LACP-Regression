show system stack detail
------------------------

**Minimum user role:** viewer

To display detailed information about packages in current, revert and target stacks:

**Command syntax: show system stack detail**
**Command syntax: show system stack detail os-packages**

**Command mode:** operational

**Note**

	- When the os-packages flag is used, the command displays the details of the OS packages in the current, revert, and target stacks.

**Parameter table**

For each trap, the following information is displayed:

+-------------+-------------------------------------------------------------------------+
| Field       | Description                                                             |
+=============+=========================================================================+
| os-packages | Display a detailed view of OS packages                                  |
+-------------+-------------------------------------------------------------------------+

**Example**
::

	dnRouter# show system stack detail

	Current stack:

	  | Component       | HW Model      | HW Revision   | Version     | Package name                         | Size    | Authenticity        | MD5           | Estimated Time |
	  |-----------------+---------------+---------------+-------------+--------------------------------------+---------+---------------------+---------------|----------------|
	  | DNOS            |     -         |     -         | 14.0.1      | drivenets_dnos_14.0.1.tar            | 2.8 GB  | signature-verified  | azn32564asv   | 0:16:40        |
	  | BaseOS          |     -         |     -         | 2.304       | drivenets_baseos_2.304.tar           | 1.0 GB  | signature-verified  | 2467asdghfs   | 0:16:40        |
	  | BaseOS packages |     -         |     -         | 1.100       | drivenets_baseos_packages_1.100.tar  | 0.7 GB  | signature-verified  | 5437asdghfs   | 0:15:40        |
	  | NCM-NOS         |     -         |     _         | 3.0.0       | drivenets_stratax_3.0.0.tar          | 3.0 GB  | signature-verified  | hsjgj63478x   | 0:16:40        |
	  | Firmware        | S9700-53DX    | 1             | 7.80        | ufi-wbx-fw-7.80                      | 40 MB   | hash-verified       | jhsdgsdj674   | 0:16:40        |
	  | Firmware        | S9700-23D-J   | 3             | 7.80        | ufi-wbx-fw-7.80                      | 40 MB   | hash-verified       | jhsdgsdj674   | 0:16:40        |


	Target stack 
	  | Component       | HW Model      | HW Revision   | Version     | Package name                         | Size    | Authenticity        | MD5           | Estimated Time |
	  |-----------------+---------------+---------------+-------------+--------------------------------------+---------+---------------------+---------------|----------------|
	  | DNOS            |     -         |     -         | 14.0.1      | drivenets_dnos_15.1.0.tar            | 2.8 GB  | signature-verified  | azn32564asv   | 0:16:40        |
	  | BaseOS          |     -         |     -         | 2.304       | drivenets_baseos_2.506.tar           | 1.0 GB  | signature-verified  | 2467asdghfs   | 0:16:40        |
	  | BaseOS packages |     -         |     -         | 1.100       | drivenets_baseos_packages_1.200.tar  | 0.7 GB  | signature-verified  | 5437asdghfs   | 0:15:40        |
	  | NCM-NOS         |     -         |     _         | 3.50        | drivenets_stratax_4.0.0.tar          | 3.0 GB  | signature-verified  | hsjgj63478x   | 0:16:40        |
	  | Firmware        | S9700-53DX    | 1             | 8.0         | ufi-wbx-fw-8.0                       | 40 MB   | hash-verified       | jhsdgsdj674   | 0:16:40        |
	  | Firmware        | S9700-23D-J   | 3             | 8.0         | ufi-wbx-fw-8.0                       | 50 MB   | unverified          | hkdfddhsfk7   | 0:16:40        |

	Revert stack:

	  | Component       | Version     | Package name                         | Size    | Authenticity        | MD5           | Estimated Time |
	  |-----------------+-------------+--------------------------------------+---------+---------------------+---------------|----------------|
	  | DNOS            | 13.0.2      | drivenets_dnos_v13.0.2.tar           | 2.8 GB  | signature-verified  | azn32564asv   | 0:16:40        |
	  | BaseOS          | 1.507       | drivenets_baseos_1.507.tar           | 1.0 GB  | signature-verified  | 2467asdghfs   | 0:16:40        |
	  | BaseOS packages | 1.100       | drivenets_baseos_packages_1.100.tar  | 0.6 GB  | signature-verified  | 54322234hfs   | 0:15:40        |
	  | NCM-NOS         | 2.1.0       | drivenets_stratax_2.1.0.tar          | 3.0 GB  | signature-verified  | hsjgj63478x   | 0:16:40        |


**Example**
::

	dnRouter# show system stack detail os-packages

	Current stack:

	OS Package: drivenets_baseos_packages_1.150.tar

	  | Component       | Version     | OS Package Name                                       |
	  |-----------------+-------------+-------------------------------------------------------+
	  | openssl         | 2.20        | openssl_1.1.1f-1ubuntu2.20_amd64.deb                  |
	  | binutils        | 1.9         | binutils_2.34-6ubuntu1.9_amd64.deb                    |


	Target stack:

	OS Package: drivenets_baseos_packages_1.200.tar

	  | Component       | Version     | OS Package Name                                       |
	  |-----------------+-------------+-------------------------------------------------------+
	  | openssl         | 2.23        | openssl_1.1.1f-1ubuntu2.23_amd64.deb                  |
	  | binutils        | 2.0         | binutils_2.34-6ubuntu2.0_amd64.deb                    |

	Revert stack:

	OS Package: drivenets_baseos_packages_1.100.tar

	  | Component       | Version     | OS Package Name                                       |
	  |-----------------+-------------+-------------------------------------------------------+
	  | openssl         | 2.17        | openssl_1.1.1f-1ubuntu2.17_amd64.deb                  |
	  | binutils        | 1.9         | binutils_2.34-6ubuntu1.9_amd64.deb                    |

**Example**
::

	dnRouter# show system stack detail os-packages

	OS Package: drivenets_baseos_packages_1.150.tar

	  | Component       | Version     | OS Package Name                                       |
	  |-----------------+-------------+-------------------------------------------------------+
	  | openssl         | 2.20        | openssl_1.1.1f-1ubuntu2.20_amd64.deb                  |
	  | binutils        | 1.9         | binutils_2.34-6ubuntu1.9_amd64.deb                    |


	Target stack:

	OS Package: drivenets_baseos_packages_1.200.tar

	  | Component       | Version     | OS Package Name                                       |
	  |-----------------+-------------+-------------------------------------------------------+
	  | openssl         | 2.23        | openssl_1.1.1f-1ubuntu2.23_amd64.deb                  |
	  | binutils        | 2.0         | binutils_2.34-6ubuntu2.0_amd64.deb                    |

	Revert stack:

	OS Package: BaseOS packages

	  | Component       | Version     | OS Package Name                                       |
	  |-----------------+-------------+-------------------------------------------------------+
	  | openssl         | 2.17        | openssl_1.1.1f-1ubuntu2.17_amd64.deb                  |
	  | binutils        | 1.9         | binutils_2.34-6ubuntu1.9_amd64.deb                    |

.. **Help line:** Show details about packages in current, revert and target stacks

**Output table:**

+----------------------+-------------------------+----------+
| Parameter            | Values                  | Comments |
+======================+=========================+==========+
| Authenticity         | signature-verified      |          |
|                      | hash-verified           |          |
|                      | unverified              |          |
+----------------------+-------------------------+----------+


**Command History**

+---------+---------------------------+
| Release | Modification              |
+=========+===========================+
| 16.1    | Command introduced        |
+---------+---------------------------+
| 18.2.1  | Added estimated time      |
+---------+---------------------------+
| TBD     | Added os-packages support |
+---------+---------------------------+
