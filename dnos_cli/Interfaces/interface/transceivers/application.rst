interfaces transceiver application
----------------------------------

**Minimum user role:** operator

Sets the operational mode according to CMIS application. To configure the transceiver application:

**Command syntax: application {media-name [media-name], media-code [media-code], host-name [host-name], host-code [host-code], class-name [class-name]}**

**Command mode:** config

**Hierarchies**

- interfaces transceiver

**Note**

- Both Media and Host applications could be configured using either name or code. If both are configured, code value will be used and the configured name will be ignored.

**Parameter table**

+------------+---------------------------------------------------+-----------------------+---------+
| Parameter  | Description                                       | Range                 | Default |
+============+===================================================+=======================+=========+
| media-name | Optical module CMIS application name              | | UNDEFINED           | \-      |
|            |                                                   | | 10GBASE-SW          |         |
|            |                                                   | | 10GBASE-SR          |         |
|            |                                                   | | 25GBASE-SR          |         |
|            |                                                   | | 40GBASE-SR4         |         |
|            |                                                   | | 40GE-SWDM4          |         |
|            |                                                   | | 40GE-BiDi           |         |
|            |                                                   | | 50GBASE-SR          |         |
|            |                                                   | | 100GBASE-SR10       |         |
|            |                                                   | | 100GBASE-SR4        |         |
|            |                                                   | | 100GE-SWDM4         |         |
|            |                                                   | | 100GE-BiDi          |         |
|            |                                                   | | 100GBASE-SR2        |         |
|            |                                                   | | 100GBASE-SR         |         |
|            |                                                   | | 100GBASE-VR         |         |
|            |                                                   | | 200GBASE-SR4        |         |
|            |                                                   | | 200GBASE-SR2        |         |
|            |                                                   | | 200GBASE-VR2        |         |
|            |                                                   | | 400GBASE-SR16       |         |
|            |                                                   | | 400GBASE-SR8        |         |
|            |                                                   | | 400GBASE-SR4        |         |
|            |                                                   | | 400GBASE-VR4        |         |
|            |                                                   | | 800G-SR8            |         |
|            |                                                   | | 800G-VR8            |         |
|            |                                                   | | 400GBASE-SR4.2      |         |
|            |                                                   | | 800GBASE-VR4.2      |         |
|            |                                                   | | 800GBASE-SR4.2      |         |
|            |                                                   | | 10GBASE-LW          |         |
|            |                                                   | | 10GBASE-EW          |         |
|            |                                                   | | 10G-ZW              |         |
|            |                                                   | | 10GBASE-LR          |         |
|            |                                                   | | 10GBASE-ER          |         |
|            |                                                   | | 10GBASE-BR          |         |
|            |                                                   | | 10G-ZR              |         |
|            |                                                   | | 25GBASE-LR          |         |
|            |                                                   | | 25GBASE-ER          |         |
|            |                                                   | | 25GBASE-BR          |         |
|            |                                                   | | 40GBASE-LR4         |         |
|            |                                                   | | 40GBASE-FR          |         |
|            |                                                   | | 50GBASE-FR          |         |
|            |                                                   | | 50GBASE-LR          |         |
|            |                                                   | | 50GBASE-ER          |         |
|            |                                                   | | 50GBASE-BR          |         |
|            |                                                   | | 100GBASE-LR4        |         |
|            |                                                   | | 100GBASE-ER4        |         |
|            |                                                   | | 100G-PSM4           |         |
|            |                                                   | | 100G-CWDM4-OCP      |         |
|            |                                                   | | 100G-CWDM4          |         |
|            |                                                   | | 100G-4WDM-10        |         |
|            |                                                   | | 100G-4WDM-20        |         |
|            |                                                   | | 100G-4WDM-40        |         |
|            |                                                   | | 100GBASE-DR         |         |
|            |                                                   | | 100GBASE-FR         |         |
|            |                                                   | | 100GBASE-LR         |         |
|            |                                                   | | 100G-LR1-20         |         |
|            |                                                   | | 100G-ER1-30         |         |
|            |                                                   | | 100G-ER1-40         |         |
|            |                                                   | | 100GBASE-ZR         |         |
|            |                                                   | | 200GBASE-DR4        |         |
|            |                                                   | | 200GBASE-FR4        |         |
|            |                                                   | | 200GBASE-LR4        |         |
|            |                                                   | | 200GBASE-ER4        |         |
|            |                                                   | | 400GBASE-FR8        |         |
|            |                                                   | | 400GBASE-LR8        |         |
|            |                                                   | | 400GBASE-ER8        |         |
|            |                                                   | | 400GBASE-DR4        |         |
|            |                                                   | | 400GBASE-FR4        |         |
|            |                                                   | | 400GBASE-LR4-6      |         |
|            |                                                   | | 400GBASE-LR4-10     |         |
|            |                                                   | | 400GBASE-ZR         |         |
|            |                                                   | | 800GBASE-DR8        |         |
|            |                                                   | | 800GBASE-DR8-2      |         |
|            |                                                   | | 400ZR-amplified     |         |
|            |                                                   | | 400ZR-unamplified   |         |
|            |                                                   | | ZR400-OFEC-16QAM    |         |
|            |                                                   | | ZR300-OFEC-8QAM     |         |
|            |                                                   | | ZR200-OFEC-QPSK     |         |
|            |                                                   | | ZR100-OFEC-QPSK     |         |
|            |                                                   | | UNSUPPORTED         |         |
+------------+---------------------------------------------------+-----------------------+---------+
| media-code | Optical module CMIS application media code in hex | \-                    | \-      |
+------------+---------------------------------------------------+-----------------------+---------+
| host-name  | Optical module CMIS host application name         | | UNDEFINED           | \-      |
|            |                                                   | | 400GAUI-8-C2M       |         |
|            |                                                   | | 400GBASE-CR8        |         |
|            |                                                   | | 200GAUI-4-C2M       |         |
|            |                                                   | | 200GBASE-CR4        |         |
|            |                                                   | | 100GAUI-2-C2M       |         |
|            |                                                   | | 100GBASE-CR2        |         |
|            |                                                   | | CAUI-4-C2M          |         |
|            |                                                   | | 100GBASE-CR4        |         |
|            |                                                   | | 100GAUI-4-C2M       |         |
+------------+---------------------------------------------------+-----------------------+---------+
| host-code  | Optical module CMIS application host code in hex  | \-                    | \-      |
+------------+---------------------------------------------------+-----------------------+---------+
| class-name | User defined application identifier               | | string              | \-      |
|            |                                                   | | length 1-255        |         |
+------------+---------------------------------------------------+-----------------------+---------+

**Example**
::

    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-4/1/1
    dnRouter(cfg-if-ge400-4/1/1)# transceiver
    dnRouter(cfg-if-ge400-4/1/1-trns)# application media-name ZR400-OFEC-16QAM
    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-4/1/1
    dnRouter(cfg-if-ge400-4/1/1)# transceiver
    dnRouter(cfg-if-ge400-4/1/1-trns)# application media-code C8
    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-4/1/1
    dnRouter(cfg-if-ge400-4/1/1)# transceiver
    dnRouter(cfg-if-ge400-4/1/1-trns)# application host-name 400GAUI-8-C2M
    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-4/1/1
    dnRouter(cfg-if-ge400-4/1/1)# transceiver
    dnRouter(cfg-if-ge400-4/1/1-trns)# application host-code 11
    dnRouter# configure
    dnRouter(cfg)# interfaces
    dnRouter(cfg-if)# ge400-4/1/1
    dnRouter(cfg-if-ge400-4/1/1)# transceiver
    dnRouter(cfg-if-ge400-4/1/1-trns)# application class-name my-400GZR+


**Removing Configuration**

::

    dnRouter(cfg-if-ge400-4/1/1-trns)# no application

**Command History**

+---------+------------------------------------------------------+
| Release | Modification                                         |
+=========+======================================================+
| 16.2    | Command introduced                                   |
+---------+------------------------------------------------------+
| 17.1    | Added support for more transceivers                  |
+---------+------------------------------------------------------+
| TBD     | added option for media and host name and code config |
+---------+------------------------------------------------------+
