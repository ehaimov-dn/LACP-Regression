show system nodes stack
-----------------------

**Minimum user role:** operator

Displays detailed information about packages in current, revert and target stacks relevant per each node in the cluster.

**Command syntax: show system nodes stack**

**Command mode:** operational

**Example:**
::

	dnRouter# show system nodes stack

	Current stack:

    | Node | ID | Component       | HW Model      | HW Revision   | Version     | Package name                         | Size    | Authenticity        | MD5           |
    |------+----|-----------------+---------------+---------------+-------------+--------------------------------------+---------+---------------------+---------------|
    | NCC  | 0  | DNOS            |     -         |     -         | 14.0.1      | drivenets_dnos_14.0.1.tar            | 2.8 GB  | signature-verified  | azn32564asv   |
    | NCC  | 0  | BaseOS          |     -         |     -         | 2.304       | drivenets_baseos_2.304.tar           | 1.0 GB  | signature-verified  | 2467asdghfs   |
    | NCC  | 0  | BaseOS packages |     -         |     -         | 1.100       | drivenets_baseos_packages_1.100.tar  | 0.7 GB  | signature-verified  | 5437asdghfs   |
    | NCM  | A0 | NCM-NOS         |     -         |     _         | 3.0.0       | drivenets_stratax_3.0.0.tar          | 3.0 GB  | signature-verified  | hsjgj63478x   |
    | NCP  | 0  | DNOS            |     -         |     -         | 14.0.1      | drivenets_dnos_14.0.1.tar            | 2.8 GB  | signature-verified  | azn32564asv   |
    | NCP  | 0  | BaseOS          |     -         |     -         | 2.304       | drivenets_baseos_2.304.tar           | 1.0 GB  | signature-verified  | 2467asdghfs   |
    | NCP  | 0  | Firmware        | S9700-53DX    | 1             | 7.80        | ufi-wbx-fw-7.80                      | 40 MB   | hash-verified       | jhsdgsdj674   |
    | NCF  | 0  | DNOS            |     -         |     -         | 14.0.1      | drivenets_dnos_14.0.1.tar            | 2.8 GB  | signature-verified  | azn32564asv   |
    | NCF  | 0  | BaseOS          |     -         |     -         | 2.304       | drivenets_baseos_2.304.tar           | 1.0 GB  | signature-verified  | 2467asdghfs   |
    | NCF  | 0  | Firmware        | S9700-23D-J   | 3             | 7.80        | ufi-wbx-fw-7.80                      | 40 MB   | hash-verified       | jhsdgsdj674   |

	Target stack:

    | Node | ID | Component       | HW Model      | HW Revision   | Version     | Package name                         | Size    | Authenticity        | MD5           |
    |------+----|-----------------+---------------+---------------+-------------+--------------------------------------+---------+---------------------+---------------|
    | NCC  | 0  | DNOS            |     -         |     -         | 14.0.1      | drivenets_dnos_16.1.1.tar            | 2.8 GB  | signature-verified  | azn32564asv   |
    | NCC  | 0  | BaseOS          |     -         |     -         | 2.304       | drivenets_baseos_2.506.tar           | 1.0 GB  | signature-verified  | 2467asdghfs   |
    | NCC  | 0  | BaseOS packages |     -         |     -         | 1.100       | drivenets_baseos_packages_1.200.tar  | 0.7 GB  | signature-verified  | 5437asdghfs   |
    | NCM  | A0 | NCM-NOS         |     -         |     _         | 3.0.0       | drivenets_stratax_3.0.0.tar          | 3.0 GB  | signature-verified  | hsjgj63478x   |
    | NCP  | 0  | DNOS            |     -         |     -         | 14.0.1      | drivenets_dnos_16.1.1.tar            | 2.8 GB  | signature-verified  | azn32564asv   |
    | NCP  | 0  | BaseOS          |     -         |     -         | 2.304       | drivenets_baseos_2.506.tar           | 1.0 GB  | signature-verified  | 2467asdghfs   |
    | NCP  | 0  | Firmware        | S9700-53DX    | 1             | 7.80        | ufi-wbx-fw-8.10                      | 40 MB   | hash-verified       | jhsdgsdj674   |
    | NCF  | 0  | DNOS            |     -         |     -         | 14.0.1      | drivenets_dnos_16.1.1.tar            | 2.8 GB  | signature-verified  | azn32564asv   |
    | NCF  | 0  | BaseOS          |     -         |     -         | 2.304       | drivenets_baseos_2.506.tar           | 1.0 GB  | signature-verified  | 2467asdghfs   |


	Revert stack:

    | Node | ID | Component       | HW Model      | HW Revision   | Version     | Package name                         | Size    | Authenticity        | MD5           |
    |------+----|-----------------+---------------+---------------+-------------+--------------------------------------+---------+---------------------+---------------|
    | NCC  | 0  | DNOS            |     -         |     -         | 14.0.1      | drivenets_dnos_13.0.2.tar            | 2.8 GB  | signature-verified  | azn32564asv   |
    | NCC  | 0  | BaseOS packages |     -         |     -         | 1.150       | drivenets_baseos_packages_1.100.tar  | 0.6 GB  | signature-verified  | 54322234hfs   |
    | NCM  | A0 | NCM-NOS         |     -         |     _         | 2.0.0       | drivenets_stratax_2.0.0.tar          | 3.0 GB  | signature-verified  | hsjgj63478x   |
    | NCP  | 0  | DNOS            |     -         |     -         | 14.0.1      | drivenets_dnos_13.0.2.tar            | 2.8 GB  | signature-verified  | azn32564asv   |
    | NCP  | 0  | BaseOS          |     -         |     -         | 2.304       | drivenets_baseos_2.304.tar           | 1.0 GB  | signature-verified  | 2467asdghfs   |
    | NCP  | 0  | Firmware        | S9700-53DX    | 1             | 7.80        | ufi-wbx-fw-7.80                      | 40 MB   | hash-verified       | jhsdgsdj674   |
    | NCF  | 0  | DNOS            |     -         |     -         | 14.0.1      | drivenets_dnos_13.0.2.tar            | 2.8 GB  | signature-verified  | azn32564asv   |
    | NCF  | 0  | Firmware        | S9700-23D-J   | 3             | 7.80        | ufi-wbx-fw-7.80                      | 40 MB   | hash-verified       | jhsdgsdj674   |


**Outputs table:**

+----------------------+-------------------------+----------+
| Parameter            | Values                  | Comments |
+======================+=========================+==========+
| Authenticity         | signature-verified      |          |
|                      | hash-verified           |          |
|                      | unverified              |          |
+----------------------+-------------------------+----------+

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 17.1    | Command introduced |
+---------+--------------------+
