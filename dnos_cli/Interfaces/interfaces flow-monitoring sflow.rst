interfaces flow-monitoring type sflow direction
-----------------------------------------------

**Minimum user role:** operator

The interface flow-monitoring sflow command defines a flow-monitoring sflow profile for the interface. It defines how flow-monitoring sflow is applied on the interface: which exporter-profiles to use, in which direction, which sampler profile to use, etc.

Interface can support up to 4 exporters.

To define a flow-monitoring sflow for the interface:

**Command syntax: flow-monitoring type sflow direction [direction]** exporter-profile [exporter-profile] sampler-profile [sampler-profile]

**Command mode:** config

**Hierarchies**

- interfaces

**Note**

- The command is applicable to the following interface types:

  - Bundle
  - Bundle vlan
  - Physical
  - Physical vlan.

- You can't configure both sflow and netflow/ipfix on the same interface.

- For flow-monitoring type sflow, the exporter-profile version must be configured as sflow.

- Mimimum sampling rate for sflow flow monitoring is 1:2048.

**Parameter table**

+------------------+-----------------------------------------------------------+----------------------------------------------------------+---------+
| Parameter        | Description                                               | Range                                                    | Default |
+==================+===========================================================+==========================================================+=========+
| direction        | Specify the direction for the sflow sampling.             | in                                                       | in      |
+------------------+-----------------------------------------------------------+----------------------------------------------------------+---------+
| exporter-profile | The name of an existing flow-monitoring exporter-profile. | String (see "services flow-monitoring exporter-profile") | \-      |
+------------------+-----------------------------------------------------------+----------------------------------------------------------+---------+
| sampler-profile  | The name of an existing flow-sampler.                     | String (see "services flow-monitoring sampler-profile")  | \-      |
+------------------+-----------------------------------------------------------+----------------------------------------------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces ge100-1/1/1
    dnRouter(cfg-if-ge100-1/1/1)# flow-monitoring type sflow exporter-profile myExporter direction in
    dnRouter(cfg-if-ge100-1/1/1)# flow-monitoring type sflow exporter-profile myExporter direction in sampler-profile mySampler1


**Removing Configuration**

To remove the attachment for all exporters types:
::

    dnRouter(cfg-if-ge100-1/1/1)# no flow-monitoring

To remove the sflow configuration:
::

    dnRouter(cfg-if-ge100-1/1/1)# no flow-monitoring type sflow

To remove the sampler-profile:
::

    dnRouter(cfg-if-ge100-1/1/1)# no flow-monitoring type sflow direction in sampler-profile

To remove all exporter profiles from an interface:
::

    dnRouter(cfg-if-ge100-1/1/1)# no flow-monitoring type sflow direction in exporter-profile

To remove a specific profile from an interface:
::

    dnRouter(cfg-if-ge100-1/1/1)# no flow-monitoring type sflow direction in exporter-profile myExporter

**Command History**

+---------+--------------------+
| Release | Modification       |
+=========+====================+
| 25.1    | Command introduced |
+---------+--------------------+
