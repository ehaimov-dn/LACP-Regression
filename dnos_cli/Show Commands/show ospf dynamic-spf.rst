show ospf dynamic-spf
----------------------------------

**Minimum user role:** viewer

To display OSPF Dynamic-SPF information:


**Command syntax: show ospf** instance [ospf-instance-name] **dynamic-spf** { calculation-type [calculation-type-name] | detail }

**Command mode:** operational


..
	**Internal Note**

    - use "instance [ospf-instance-name]" to display information for a specific OSPF instance; when not specified, display information for all OSPF instances

    - use "calculation-type [calculation-type-name]" to display additional information for a specific calculation type

    - use "detail" to display additional information for all calculation types

**Parameter table**

+-----------------------+-----------------------------------------+----------------------------+------------------+
| Parameter             | Description                             | Values                     | Default value    |
+=======================+=========================================+============================+==================+
| ospf-instance-name    | Filters the displayed information       | Configured instances       | all instances    |
|                       | for a specific OSPF instance            |                            |                  |
+-----------------------+-----------------------------------------+----------------------------+------------------+
| calculation-type-name | Filters the displayed information       | unicast-spf                | all calculations |
|                       | for a specific calculation type         | ase-full-update            |                  |
|                       |                                         | sr-update                  |                  |
|                       |                                         | sr-lfa-prerun              |                  |
|                       |                                         | flex-spf                   |                  |
|                       |                                         | flex-lfa-prerun            |                  |
|                       |                                         | abr-update                 |                  |
|                       |                                         | sr-lfa-postrun             |                  |
|                       |                                         | flex-lfa-postrun           |                  |
|                       |                                         | sr-routes-install          |                  |
|                       |                                         | srte-update                |                  |
+-----------------------+-----------------------------------------+----------------------------+------------------+


**Example**
::

    dnRouter# show ospf dynamic-spf

    Dynamic-SPF Configuration:
      Dynamic-SPF: Enabled
      Maximum CPU utilization: 75%
      CPU utilization window: 10000 ms
    Dynamic-SPF information:
      Total CPU time during the current window (10.000s): 0.378s (3.78%)
      Total CPU time during the last minute (1m00s): 6.886s (11.48%)



    dnRouter# show ospf dynamic-spf detail

    Dynamic-SPF Configuration:
      Dynamic-SPF: Enabled
      Maximum CPU utilization: 75%
      CPU utilization window: 10000 ms
    Dynamic-SPF information:
      Total CPU time during the current window (10.000s): 0.378s (3.78%)
      Total CPU time during the last minute (1m00s): 6.779s (11.30%)

      Ospf Instance 1
        Last executed: 5.975s ago
        Next pending:
        CPU time during the current window (10.000s): 0.366s (3.66%)
        CPU time during the last minute (1m00s): 6.735s (11.23%)

        Unicast SPF
          Pending: no
          Last run: 6.269s ago
          Last run time: 0.014s
          Maximum run time: 0.071s
          Number of runs: 36
          Average run time: 0.029s
          Total run time during current window (10.000s): 0.033s (0.33%)
          Total run time during the last minute (1m00s): 0.476s (0.79%)

        AS External full update
          Pending: no
          Last run: 6.244s ago
          Last run time: 0.044s
          Maximum run time: 0.063s
          Number of runs: 36
          Average run time: 0.028s
          Total run time during current window (10.000s): 0.088s (0.88%)
          Total run time during the last minute (1m00s): 0.565s (0.94%)

        SR update
          Pending: no
          Last run: 6.186s ago
          Last run time: 0.104s
          Maximum run time: 0.194s
          Number of runs: 170
          Average run time: 0.042s
          Total run time during current window (10.000s): 0.180s (1.80%)
          Total run time during the last minute (1m00s): 0.918s (1.53%)

        SR LFA pre-run
          Pending: no
          Last run: 6.071s ago
          Last run time: 0.034s
          Maximum run time: 0.061s
          Number of runs: 135
          Average run time: 0.038s
          Total run time during current window (10.000s): 0.034s (0.34%)
          Total run time during the last minute (1m00s): 0.302s (0.50%)

        Flex-algo SPF
          Pending: no
          Last run: 6.013s ago
          Last run time: 0 usecs
          Maximum run time: 0.332s
          Number of runs: 71
          Average run time: 0.087s
          Total run time during current window (10.000s): 0.001s (0.01%)
          Total run time during the last minute (1m00s): 3.348s (5.58%)

        Flex-algo LFA pre-run
          Pending: no
          Last run: 45.120s ago
          Last run time: 0 usecs
          Maximum run time: 0.001s
          Number of runs: 41
          Average run time: 0 usecs
          Total run time during current window (10.000s): 0 usecs (0.00%)
          Total run time during the last minute (1m00s): 0.002s (0.00%)

        ABR update
          Pending: no
          Last run: Never
          Maximum run time: 0 usecs
          Number of runs: 0
          Average run time: 0 usecs
          Total run time during current window (10.000s): 0 usecs (0.00%)
          Total run time during the last minute (1m00s): 0 usecs (0.00%)

        SR LFA post-run
          Pending: no
          Last run: 6.006s ago
          Last run time: 0.030s
          Maximum run time: 0.077s
          Number of runs: 83
          Average run time: 0.034s
          Total run time during current window (10.000s): 0.030s (0.30%)
          Total run time during the last minute (1m00s): 0.314s (0.52%)

        Flex-algo LFA post-run
          Pending: no
          Last run: 44.807s ago
          Last run time: 0.046s
          Maximum run time: 0.061s
          Number of runs: 16
          Average run time: 0.020s
          Total run time during current window (10.000s): 0 usecs (0.00%)
          Total run time during the last minute (1m00s): 0.101s (0.17%)

        SR routes install
          Pending: no
          Last run: 5.976s ago
          Last run time: 0 usecs
          Maximum run time: 0.331s
          Number of runs: 225
          Average run time: 0.006s
          Total run time during current window (10.000s): 0 usecs (0.00%)
          Total run time during the last minute (1m00s): 0.708s (1.18%)

        SR-TE update
          Pending: no
          Last run: 5.975s ago
          Last run time: 0 usecs
          Maximum run time: 0.001s
          Number of runs: 148
          Average run time: 0 usecs
          Total run time during current window (10.000s): 0 usecs (0.00%)
          Total run time during the last minute (1m00s): 0.001s (0.00%)

      Ospf Instance 2
        Last executed: 5.970s ago
        Next pending:
        CPU time during the current window (10.000s): 0.012s (0.12%)
        CPU time during the last minute (1m00s): 0.044s (0.07%)

        Unicast SPF
          Pending: no
          Last run: 5.976s ago
          Last run time: 0 usecs
          Maximum run time: 0.003s
          Number of runs: 12
          Average run time: 0.001s
          Total run time during current window (10.000s): 0.001s (0.01%)
          Total run time during the last minute (1m00s): 0.002s (0.00%)

        AS External full update
          Pending: no
          Last run: 5.975s ago
          Last run time: 0 usecs
          Maximum run time: 0.001s
          Number of runs: 12
          Average run time: 0 usecs
          Total run time during current window (10.000s): 0 usecs (0.00%)
          Total run time during the last minute (1m00s): 0.001s (0.00%)

        SR update
          Pending: no
          Last run: 5.975s ago
          Last run time: 0.003s
          Maximum run time: 0.013s
          Number of runs: 16
          Average run time: 0.004s
          Total run time during current window (10.000s): 0.008s (0.08%)
          Total run time during the last minute (1m00s): 0.014s (0.02%)

        SR LFA pre-run
          Pending: no
          Last run: 5.972s ago
          Last run time: 0.001s
          Maximum run time: 0.002s
          Number of runs: 14
          Average run time: 0.001s
          Total run time during current window (10.000s): 0.001s (0.01%)
          Total run time during the last minute (1m00s): 0.002s (0.00%)

        Flex-algo SPF
          Pending: no
          Last run: 5.971s ago
          Last run time: 0 usecs
          Maximum run time: 0.021s
          Number of runs: 21
          Average run time: 0.005s
          Total run time during current window (10.000s): 0.001s (0.01%)
          Total run time during the last minute (1m00s): 0.009s (0.01%)

        Flex-algo LFA pre-run
          Pending: no
          Last run: 45.120s ago
          Last run time: 0 usecs
          Maximum run time: 0.001s
          Number of runs: 10
          Average run time: 0 usecs
          Total run time during current window (10.000s): 0 usecs (0.00%)
          Total run time during the last minute (1m00s): 0 usecs (0.00%)

        ABR update
          Pending: no
          Last run: Never
          Maximum run time: 0 usecs
          Number of runs: 0
          Average run time: 0 usecs
          Total run time during current window (10.000s): 0 usecs (0.00%)
          Total run time during the last minute (1m00s): 0 usecs (0.00%)

        SR LFA post-run
          Pending: no
          Last run: 5.971s ago
          Last run time: 0.001s
          Maximum run time: 0.004s
          Number of runs: 11
          Average run time: 0.001s
          Total run time during current window (10.000s): 0.001s (0.01%)
          Total run time during the last minute (1m00s): 0.001s (0.00%)

        Flex-algo LFA post-run
          Pending: no
          Last run: 44.835s ago
          Last run time: 0.002s
          Maximum run time: 0.004s
          Number of runs: 7
          Average run time: 0.001s
          Total run time during current window (10.000s): 0 usecs (0.00%)
          Total run time during the last minute (1m00s): 0.002s (0.00%)

        SR routes install
          Pending: no
          Last run: 5.970s ago
          Last run time: 0 usecs
          Maximum run time: 0.024s
          Number of runs: 30
          Average run time: 0.002s
          Total run time during current window (10.000s): 0 usecs (0.00%)
          Total run time during the last minute (1m00s): 0.013s (0.02%)

        SR-TE update
          Pending: no
          Last run: 5.970s ago
          Last run time: 0 usecs
          Maximum run time: 0 usecs
          Number of runs: 30
          Average run time: 0 usecs
          Total run time during current window (10.000s): 0 usecs (0.00%)
          Total run time during the last minute (1m00s): 0 usecs (0.00%)



    dnRouter# show ospf instance 1 dynamic-spf

    Dynamic-SPF Configuration:
      Dynamic-SPF: Enabled
      Maximum CPU utilization: 75%
      CPU utilization window: 10000 ms
    Dynamic-SPF information:
      Total CPU time during the current window (10.000s): 0.146s (1.46%)
      Total CPU time during the last minute (1m00s): 0.600s (1.00%)

      Ospf Instance 1
        Last executed: 21.123s ago
        Next pending:
        CPU time during the current window (10.000s): 0 usecs (0.00%)
        CPU time during the last minute (1m00s): 0.427s (0.71%)

        Unicast SPF
          Pending: no
          Last run: 21.417s ago
          Last run time: 0.014s
          Maximum run time: 0.071s
          Number of runs: 36
          Average run time: 0.029s
          Total run time during current window (10.000s): 0 usecs (0.00%)
          Total run time during the last minute (1m00s): 0.033s (0.06%)

        AS External full update
          Pending: no
          Last run: 21.392s ago
          Last run time: 0.044s
          Maximum run time: 0.063s
          Number of runs: 36
          Average run time: 0.028s
          Total run time during current window (10.000s): 0 usecs (0.00%)
          Total run time during the last minute (1m00s): 0.088s (0.15%)

        SR update
          Pending: no
          Last run: 21.334s ago
          Last run time: 0.104s
          Maximum run time: 0.194s
          Number of runs: 170
          Average run time: 0.042s
          Total run time during current window (10.000s): 0 usecs (0.00%)
          Total run time during the last minute (1m00s): 0.180s (0.30%)

        SR LFA pre-run
          Pending: no
          Last run: 21.219s ago
          Last run time: 0.034s
          Maximum run time: 0.061s
          Number of runs: 135
          Average run time: 0.038s
          Total run time during current window (10.000s): 0 usecs (0.00%)
          Total run time during the last minute (1m00s): 0.034s (0.06%)

        Flex-algo SPF
          Pending: no
          Last run: 21.161s ago
          Last run time: 0 usecs
          Maximum run time: 0.332s
          Number of runs: 71
          Average run time: 0.087s
          Total run time during current window (10.000s): 0 usecs (0.00%)
          Total run time during the last minute (1m00s): 0.001s (0.00%)

        Flex-algo LFA pre-run
          Pending: no
          Last run: 1m00s ago
          Last run time: 0 usecs
          Maximum run time: 0.001s
          Number of runs: 41
          Average run time: 0 usecs
          Total run time during current window (10.000s): 0 usecs (0.00%)
          Total run time during the last minute (1m00s): 0 usecs (0.00%)

        ABR update
          Pending: no
          Last run: Never
          Maximum run time: 0 usecs
          Number of runs: 0
          Average run time: 0 usecs
          Total run time during current window (10.000s): 0 usecs (0.00%)
          Total run time during the last minute (1m00s): 0 usecs (0.00%)

        SR LFA post-run
          Pending: no
          Last run: 21.154s ago
          Last run time: 0.030s
          Maximum run time: 0.077s
          Number of runs: 83
          Average run time: 0.034s
          Total run time during current window (10.000s): 0 usecs (0.00%)
          Total run time during the last minute (1m00s): 0.030s (0.05%)

        Flex-algo LFA post-run
          Pending: no
          Last run: 59.955s ago
          Last run time: 0.046s
          Maximum run time: 0.061s
          Number of runs: 16
          Average run time: 0.020s
          Total run time during current window (10.000s): 0 usecs (0.00%)
          Total run time during the last minute (1m00s): 0.046s (0.08%)

        SR routes install
          Pending: no
          Last run: 21.124s ago
          Last run time: 0 usecs
          Maximum run time: 0.331s
          Number of runs: 225
          Average run time: 0.006s
          Total run time during current window (10.000s): 0 usecs (0.00%)
          Total run time during the last minute (1m00s): 0.015s (0.03%)

        SR-TE update
          Pending: no
          Last run: 21.123s ago
          Last run time: 0 usecs
          Maximum run time: 0.001s
          Number of runs: 148
          Average run time: 0 usecs
          Total run time during current window (10.000s): 0 usecs (0.00%)
          Total run time during the last minute (1m00s): 0 usecs (0.00%)


.. **Help line:** Displays OSPF Dynamic-SPF information:


**Command History**

+---------+----------------------------+
| Release | Modification               |
+=========+============================+
| 25.2    | Command introduced         |
+---------+----------------------------+