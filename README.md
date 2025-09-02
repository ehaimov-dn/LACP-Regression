# LACP Regression Testing Suite

This repository contains a comprehensive LACP (Link Aggregation Control Protocol) regression testing suite for network devices.

## Contents

- **Network Mapping**: Scripts to discover and map network topology
- **Test Scenarios**: Various LACP test cases including:
  - Bundle creation and deletion
  - Member addition and removal
  - System ID changes
  - Bandwidth and link constraints
  - Misconfiguration handling
- **CLI Documentation**: Comprehensive DNOS CLI command documentation
- **Logs**: Network mapping and test execution logs

## Main Components

- `main.py` - Main network mapping script
- `network_mapper.py` - Network topology discovery utilities
- `Test-Bundle_*` - Individual test scenario directories
- `dnos_cli/` - CLI command documentation and guidelines

## Usage

Run the network mapper to discover topology:
```bash
python main.py
```

Execute individual test scenarios from their respective directories.

## Documentation

See the `dnos_cli/` directory for comprehensive CLI command documentation and guidelines.
# LACP-Regression
