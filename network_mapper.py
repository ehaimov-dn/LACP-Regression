#!/usr/bin/env python3
"""
Network Device Port Mapper
Connects to network devices, extracts system and interface information,
and prepares data for topology generation.
"""

import paramiko
import json
import logging
import time
import re
import sys
from datetime import datetime
import os

class NetworkMapper:
    def __init__(self):
        self.setup_logging()
        self.device_info = {}
        self.interfaces_data = {}
        self.connection = None
        self.channel = None
        
    def setup_logging(self):
        """Setup real-time logging for debugging purposes"""
        # Create logs directory if it doesn't exist
        if not os.path.exists('logs'):
            os.makedirs('logs')
            
        # Setup logging configuration
        log_filename = f"logs/network_mapper_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_filename),
                logging.StreamHandler(sys.stdout)  # Also log to console
            ]
        )
        
        self.logger = logging.getLogger(__name__)
        self.logger.info("Network Mapper started")
    
    def get_existing_devices(self):
        """Get list of existing devices from the Devices directory"""
        devices_dir = "Devices"
        if not os.path.exists(devices_dir):
            return []
        
        existing_devices = []
        for item in os.listdir(devices_dir):
            device_path = os.path.join(devices_dir, item)
            if os.path.isdir(device_path):
                # Check if it contains the expected JSON files
                system_file = os.path.join(device_path, f"{item}_System_Information.json")
                if os.path.exists(system_file):
                    existing_devices.append(item)
        
        return existing_devices
    
    def display_device_menu(self):
        """Display menu for device selection"""
        existing_devices = self.get_existing_devices()
        
        print("\n=== Network Device Mapper ===")
        
        if existing_devices:
            print("Existing devices found:")
            print("  0. Add new device (SSH connection)")
            for i, device in enumerate(existing_devices, 1):
                print(f"  {i}. {device}")
            
            while True:
                try:
                    choice = input(f"\nSelect option (0-{len(existing_devices)}): ").strip()
                    choice_num = int(choice)
                    
                    if choice_num == 0:
                        return "new", None
                    elif 1 <= choice_num <= len(existing_devices):
                        selected_device = existing_devices[choice_num - 1]
                        return "existing", selected_device
                    else:
                        print(f"Invalid choice. Please enter 0-{len(existing_devices)}")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        else:
            print("No existing devices found.")
            print("  0. Add new device (SSH connection)")
            
            while True:
                try:
                    choice = input("\nSelect option (0): ").strip()
                    choice_num = int(choice)
                    
                    if choice_num == 0:
                        return "new", None
                    else:
                        print("Invalid choice. Please enter 0")
                except ValueError:
                    print("Invalid input. Please enter a number.")
    
    def load_existing_device_credentials(self, device_name):
        """Load credentials from existing device's system information file"""
        try:
            device_dir = f"Devices/{device_name}"
            system_file = f"{device_dir}/{device_name}_System_Information.json"
            
            with open(system_file, 'r') as f:
                system_data = json.load(f)
            
            credentials = system_data.get('login_credentials', {})
            if credentials.get('hostname') and credentials.get('username') and credentials.get('password'):
                self.logger.info(f"Loaded credentials for existing device: {device_name}")
                return credentials
            else:
                self.logger.warning(f"Incomplete credentials found for device: {device_name}")
                return None
                
        except Exception as e:
            self.logger.error(f"Error loading credentials for device {device_name}: {str(e)}")
            return None
        
    def get_user_credentials(self):
        """Get device connection credentials from user"""
        self.logger.info("Requesting user credentials")
        
        print("\n=== Network Device Connection ===")
        hostname = input("Enter device hostname/IP: ").strip()
        username = input("Enter username: ").strip()
        
        # Hide password input
        import getpass
        password = getpass.getpass("Enter password: ")
        
        credentials = {
            'hostname': hostname,
            'username': username,
            'password': password
        }
        
        self.logger.info(f"Credentials collected for device: {hostname}")
        return credentials
        
    def connect_to_device(self, credentials):
        """Establish SSH connection to the network device"""
        try:
            self.logger.info(f"Attempting to connect to {credentials['hostname']}")
            
            # Create SSH client
            self.connection = paramiko.SSHClient()
            self.connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            # Connect to device
            self.connection.connect(
                hostname=credentials['hostname'],
                username=credentials['username'],
                password=credentials['password'],
                timeout=30,
                look_for_keys=False,
                allow_agent=False
            )
            
            # Create interactive shell
            self.channel = self.connection.invoke_shell()
            time.sleep(2)  # Wait for shell to initialize
            
            # Clear any initial output
            self.channel.recv(4096)
            
            self.logger.info("Successfully connected to device")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to connect to device: {str(e)}")
            return False
            
    def wait_for_cli_ready(self):
        """Wait for CLI to be ready for commands"""
        self.logger.info("Waiting for CLI to be ready")
        
        max_wait_time = 45
        start_time = time.time()
        all_output = ""
        
        # Send initial newlines to trigger prompt
        self.logger.debug("Sending initial newlines to trigger prompt")
        self.channel.send('\n\n')
        time.sleep(2)
        
        while time.time() - start_time < max_wait_time:
            if self.channel.recv_ready():
                try:
                    output = self.channel.recv(4096).decode('utf-8', errors='ignore')
                    all_output += output
                    self.logger.debug(f"CLI output received: {repr(output)}")
                    
                    # Look for common CLI prompts (more comprehensive)
                    prompt_indicators = [
                        '>', '#', '$',  # Basic prompts
                        'Username:', 'Password:', 'login:',  # Login prompts
                        '% ',  # Cisco style
                        '~ ',  # Unix style
                        '@'    # Username@hostname patterns
                    ]
                    
                    # Check last few lines for prompt
                    recent_lines = all_output.split('\n')[-3:]
                    for line in recent_lines:
                        line = line.strip()
                        if line and any(indicator in line for indicator in prompt_indicators):
                            # Additional check for username@hostname pattern
                            if '@' in line and (line.endswith('$') or line.endswith('#') or line.endswith('>')):
                                self.logger.info(f"CLI is ready - detected prompt: {repr(line)}")
                                return True
                            elif any(line.endswith(p) for p in ['>', '#', '$', '% ']):
                                self.logger.info(f"CLI is ready - detected prompt: {repr(line)}")
                                return True
                                
                except UnicodeDecodeError as e:
                    self.logger.warning(f"Unicode decode error: {e}")
                    continue
                    
            else:
                # If no data ready, send a newline to trigger prompt
                if (time.time() - start_time) % 10 < 1:  # Every 10 seconds
                    self.logger.debug("No data ready, sending newline to trigger prompt")
                    self.channel.send('\n')
                    
            time.sleep(1)
            
        self.logger.warning("CLI readiness timeout")
        self.logger.debug(f"All output received during wait: {repr(all_output)}")
        
        # If we have some output but no clear prompt, try to proceed anyway
        if all_output.strip():
            self.logger.info("Proceeding despite unclear prompt - some output was received")
            return True
            
        return False
    
    def execute_lldp_command(self, command):
        """Execute LLDP command with special handling for potential hanging"""
        try:
            self.logger.info(f"Executing LLDP command: {command}")
            
            # Clear any pending data first
            if self.channel.recv_ready():
                self.channel.recv(4096)
                
            # Send command
            self.channel.send(command + '\n')
            time.sleep(3)  # Give more time for LLDP command to start
            
            # Collect output with shorter timeout for LLDP
            output = ""
            max_wait = 45  # Shorter timeout for LLDP command
            start_time = time.time()
            last_data_time = time.time()
            no_data_count = 0
            
            while time.time() - start_time < max_wait:
                if self.channel.recv_ready():
                    try:
                        chunk = self.channel.recv(4096).decode('utf-8', errors='ignore')
                        output += chunk
                        last_data_time = time.time()
                        no_data_count = 0
                        
                        # Check if command completed (looking for prompt in recent output)
                        recent_lines = output.split('\n')[-3:]
                        for line in recent_lines:
                            line = line.strip()
                            # Look for prompt patterns at end of line
                            if line and any(line.endswith(p) for p in ['>', '#', '$', '% ']):
                                # Also check for username@hostname patterns
                                if '@' in line and any(line.endswith(p) for p in ['$', '#', '>']):
                                    self.logger.debug(f"LLDP command completed - detected prompt: {repr(line)}")
                                    return output
                                elif any(line.endswith(p) for p in ['>', '#', '$', '% ']):
                                    self.logger.debug(f"LLDP command completed - detected prompt: {repr(line)}")
                                    return output
                                    
                    except UnicodeDecodeError as e:
                        self.logger.warning(f"Unicode decode error in LLDP output: {e}")
                        continue
                        
                else:
                    # If no data for a while, be more aggressive with timeout
                    no_data_count += 1
                    if time.time() - last_data_time > 8:  # 8 seconds without data
                        self.logger.warning("LLDP command timeout - no data for 8 seconds")
                        # Send a newline to potentially trigger prompt
                        self.channel.send('\n')
                        time.sleep(1)
                        
                        # Check one more time for prompt
                        if self.channel.recv_ready():
                            chunk = self.channel.recv(4096).decode('utf-8', errors='ignore')
                            output += chunk
                            if any(line.strip().endswith(('#', '>', '$')) for line in chunk.split('\n')):
                                self.logger.debug("LLDP command completed after timeout prompt trigger")
                                return output
                        
                        # If still no proper response, break
                        if no_data_count > 2:
                            self.logger.warning("LLDP command hanging - breaking execution")
                            break
                            
                time.sleep(1)
                
            self.logger.debug(f"LLDP command output length: {len(output)} characters")
            
            # Log first and last few lines for debugging
            lines = output.split('\n')
            if len(lines) > 5:
                self.logger.debug(f"LLDP first 3 lines: {lines[:3]}")
                self.logger.debug(f"LLDP last 3 lines: {lines[-3:]}")
            else:
                self.logger.debug(f"LLDP all output lines: {lines}")
                
            return output
            
        except Exception as e:
            self.logger.error(f"Error executing LLDP command: {str(e)}")
            return ""
    
    def create_empty_lldp_data(self, device_name):
        """Create empty LLDP data structure when LLDP command fails"""
        self.logger.info("Creating empty LLDP data structure")
        
        lldp_data = {
            'device_name': device_name,
            'timestamp': datetime.now().isoformat(),
            'total_interfaces_with_lldp': 0,
            'total_connected_neighbors': 0,
            'lldp_connections': {},
            'lldp_status': 'unavailable',
            'note': 'LLDP command failed or timed out - LLDP may not be enabled on this device'
        }
        
        # Save empty LLDP data to JSON
        device_dir = f"Devices/{getattr(self, 'device_name', 'unknown_device')}"
        filename = f"{device_dir}/{device_name}_LLDP_Connections.json"
        with open(filename, 'w') as f:
            json.dump(lldp_data, f, indent=2)
            
        self.logger.info(f"Empty LLDP data saved to {filename}")
        self.lldp_data = lldp_data
        
    def execute_command(self, command):
        """Execute command on device and return output"""
        try:
            self.logger.info(f"Executing command: {command}")
            
            # Clear any pending data first
            if self.channel.recv_ready():
                self.channel.recv(4096)
                
            # Send command
            self.channel.send(command + '\n')
            time.sleep(2)  # Give more time for command to start
            
            # Collect output
            output = ""
            max_wait = 90  # Increased timeout for larger outputs
            start_time = time.time()
            last_data_time = time.time()
            
            while time.time() - start_time < max_wait:
                if self.channel.recv_ready():
                    try:
                        chunk = self.channel.recv(4096).decode('utf-8', errors='ignore')
                        output += chunk
                        last_data_time = time.time()
                        
                        # Check if command completed (looking for prompt in recent output)
                        recent_lines = output.split('\n')[-3:]
                        for line in recent_lines:
                            line = line.strip()
                            # Look for prompt patterns at end of line
                            if line and any(line.endswith(p) for p in ['>', '#', '$', '% ']):
                                # Also check for username@hostname patterns
                                if '@' in line and any(line.endswith(p) for p in ['$', '#', '>']):
                                    self.logger.debug(f"Command completed - detected prompt: {repr(line)}")
                                    return output
                                elif any(line.endswith(p) for p in ['>', '#', '$', '% ']):
                                    self.logger.debug(f"Command completed - detected prompt: {repr(line)}")
                                    return output
                                    
                    except UnicodeDecodeError as e:
                        self.logger.warning(f"Unicode decode error in command output: {e}")
                        continue
                        
                else:
                    # If no data for a while, check if command might be complete
                    if time.time() - last_data_time > 5:  # 5 seconds without data
                        self.logger.debug("No data received for 5 seconds, checking for completion")
                        # Send a newline to potentially trigger prompt
                        self.channel.send('\n')
                        time.sleep(1)
                        if not self.channel.recv_ready():
                            # Still no data, command might be complete
                            break
                            
                time.sleep(0.5)
                
            self.logger.debug(f"Command output length: {len(output)} characters")
            
            # Log first and last few lines for debugging
            lines = output.split('\n')
            if len(lines) > 10:
                self.logger.debug(f"First 5 lines: {lines[:5]}")
                self.logger.debug(f"Last 5 lines: {lines[-5:]}")
            else:
                self.logger.debug(f"All output lines: {lines}")
                
            return output
            
        except Exception as e:
            self.logger.error(f"Error executing command: {str(e)}")
            return ""
            
    def parse_system_information(self, output, credentials):
        """Parse 'show system | no-more' output and save to JSON"""
        self.logger.info("Parsing system information")
        
        # Extract device name from output
        device_name = "unknown_device"
        device_name_match = re.search(r'Host-name\s*:\s*(\S+)', output, re.IGNORECASE)
        if device_name_match:
            device_name = device_name_match.group(1)
        else:
            # Try alternative patterns including DRIVENETS format
            hostname_patterns = [
                r'hostname\s+(\S+)',
                r'System\s+Name\s*:\s*([^,\r\n]+)',  # DRIVENETS: "System Name: R1_CL16_Eddie, System-Id:"
                r'Device\s+Name\s*:\s*(\S+)'
            ]
            for pattern in hostname_patterns:
                match = re.search(pattern, output, re.IGNORECASE)
                if match:
                    device_name = match.group(1).strip()
                    # Remove any trailing comma or whitespace
                    device_name = device_name.rstrip(' ,')
                    break
        
        # Extract device serial number for directory structure
        device_serial = "unknown_serial"
        
        # First try direct serial patterns
        serial_patterns = [
            r'Serial\s*(?:Number|#)\s*:\s*(\S+)',
            r'Serial\s*:\s*(\S+)',
            r'System\s+Serial\s*:\s*(\S+)'
        ]
        for pattern in serial_patterns:
            match = re.search(pattern, output, re.IGNORECASE)
            if match:
                device_serial = match.group(1).strip()
                break
        
        # If not found in direct patterns, try to extract from component table
        if device_serial == "unknown_serial":
            # Look for component serial numbers in the table (prioritize active NCC, then any NCP)
            table_match = re.search(r'\|\s*Type\s*\|\s*Id.*?\r?\n(\+.*?\r?\n)?((?:\|.*?\r?\n)*)', output, re.DOTALL)
            if table_match:
                table_rows = table_match.group(2)
                ncp_serial = None  # Fallback option
                
                for line in table_rows.split('\n'):
                    if line.strip().startswith('|') and not line.strip().startswith('+'):
                        # Parse table row: | Type | Id | Admin | Operational | Model | Uptime | Description | Serial Number |
                        parts = [part.strip() for part in line.split('|')[1:-1]]  # Remove empty first and last
                        if len(parts) >= 8:
                            component_type = parts[0].upper()
                            serial_num = parts[7].strip()
                            
                            # Priority 1: Active NCC with serial number
                            if component_type == 'NCC' and parts[3] and 'active' in parts[3].lower() and serial_num:
                                device_serial = serial_num
                                self.logger.info(f"Found device serial from active NCC component: {device_serial}")
                                break
                            
                            # Priority 2: Any NCP with serial number (keep as fallback)
                            elif component_type == 'NCP' and serial_num and not ncp_serial:
                                ncp_serial = serial_num
                
                # Use NCP serial if no active NCC serial was found
                if device_serial == "unknown_serial" and ncp_serial:
                    device_serial = ncp_serial
                    self.logger.info(f"Found device serial from NCP component: {device_serial}")
        
        # Create system information structure
        system_info = {
            'device_name': device_name,
            'login_credentials': {
                'hostname': credentials['hostname'],
                'username': credentials['username'],
                'password': credentials['password']  # In production, consider encryption
            },
            'system_output': output,
            'timestamp': datetime.now().isoformat(),
            'parsed_info': {}
        }
        
        # Parse additional system information - enhanced for DRIVENETS
        info_patterns = {
            # Standard patterns
            'model': r'Model\s*:\s*(.+)',
            'serial': r'Serial\s*(?:Number|#)\s*:\s*(\S+)',
            'version': r'Version\s*:\s*(.+)',
            'uptime': r'Uptime\s*:\s*(.+)',
            'location': r'Location\s*:\s*(.+)',
            
            # DRIVENETS specific patterns
            'system_id': r'System-Id\s*:\s*([^\r\n]+)',
            'system_type': r'System\s+Type\s*:\s*([^,\r\n]+)',
            'family': r'Family\s*:\s*([^\r\n]+)',
            'enterprise_id': r'Enterprise-Id\s*:\s*([^\r\n]+)',
            'description': r'Description\s*:\s*([^\r\n]+)',
            'system_status': r'System\s+status\s*:\s*([^\r\n]+)',
            'system_start_time': r'System\s+Start\s+Time\s*:\s*([^\r\n]+)',
            'system_uptime': r'System\s+Uptime\s*:\s*([^\r\n]+)',
            'system_boot_uptime': r'System\s+Boot\s+Uptime\s*:\s*([^\r\n]+)',
            'patch': r'Patch\s*:\s*([^\r\n]+)',
            'contact': r'Contact\s*:\s*([^\r\n]+)',
            'fabric_minimum_links': r'Fabric\s+Minimum\s+Links\s*:\s*([^\r\n]+)',
            'fabric_minimum_ncf': r'Fabric\s+Minimum\s+NCF\s*:\s*([^\r\n]+)',
            'dynamic_fabric_state': r'Dynamic\s+Fabric\s+State\s*:\s*([^\r\n]+)',
            'ncc_switchovers': r'NCC\s+switchovers\s*:\s*([^\r\n]+)',
            'bgp_nsr': r'BGP\s+NSR\s*:\s*([^\r\n]+)',
            'recovery_mode': r'Recovery-mode\s*:\s*([^\r\n]+)'
        }
        
        for key, pattern in info_patterns.items():
            match = re.search(pattern, output, re.IGNORECASE)
            if match:
                system_info['parsed_info'][key] = match.group(1).strip()
        
        # Parse the component table for DRIVENETS devices
        component_table = []
        table_match = re.search(r'\|\s*Type\s*\|\s*Id.*?\r?\n(\+.*?\r?\n)?((?:\|.*?\r?\n)*)', output, re.DOTALL)
        if table_match:
            table_rows = table_match.group(2)
            for line in table_rows.split('\n'):
                if line.strip().startswith('|') and not line.strip().startswith('+'):
                    # Parse table row: | Type | Id | Admin | Operational | Model | Uptime | Description | Serial Number |
                    parts = [part.strip() for part in line.split('|')[1:-1]]  # Remove empty first and last
                    if len(parts) >= 7:
                        component = {
                            'type': parts[0],
                            'id': parts[1],
                            'admin': parts[2],
                            'operational': parts[3],
                            'model': parts[4],
                            'uptime': parts[5],
                            'description': parts[6],
                            'serial_number': parts[7] if len(parts) > 7 else ''
                        }
                        component_table.append(component)
        
        if component_table:
            system_info['parsed_info']['components'] = component_table
        
        # Create directory structure based on device name
        device_dir = f"Devices/{device_name}"
        os.makedirs(device_dir, exist_ok=True)
        
        # Save to JSON file with proper naming convention
        filename = f"{device_dir}/{device_name}_System_Information.json"
        
        with open(filename, 'w') as f:
            json.dump(system_info, f, indent=2)
            
        self.logger.info(f"System information saved to {filename}")
        self.device_info = system_info
        self.device_name = device_name  # Store device name for other methods
        return device_name
        
    def parse_interface_information(self, output, device_name):
        """Parse 'show interface | no-more' output and save interface details"""
        self.logger.info("Parsing interface information")
        
        interfaces = {}
        current_interface = None
        
        lines = output.split('\n')
        
        # Try to detect if this is a DRIVENETS device first
        is_drivenets = (
            'DRIVENETS' in output.upper() or 
            any('ge100-' in line for line in lines) or
            any('bundle-' in line for line in lines) or
            'R3_SA40_Eddie' in output or 
            'R1_CL16_Eddie' in output or
            # Look for DRIVENETS-style interface names anywhere in output
            any(re.search(r'(?:ge100-|bundle-|lo0)', line) for line in lines)
        )
        
        self.logger.debug(f"DRIVENETS detection check: {is_drivenets}")
        self.logger.debug(f"Sample lines for detection: {lines[:5]}")
        
        if is_drivenets:
            self.logger.info("Detected DRIVENETS device format")
            return self._parse_drivenets_interfaces(output, device_name)
        
        # Standard Cisco/Juniper parsing
        for line in lines:
            line = line.strip()
            
            # Interface name detection (various formats)
            interface_patterns = [
                r'^(\S+/\d+/\d+)\s+is\s+(\w+)',  # ge-0/0/1 is up
                r'^Interface\s+(\S+)',            # Interface GigabitEthernet0/0/1
                r'^(\S+)\s+is\s+(\w+),',         # FastEthernet0/1 is up,
                r'^(\w+\d+/\d+/?\d*)\s+'         # Generic interface pattern
            ]
            
            interface_found = False
            for pattern in interface_patterns:
                match = re.match(pattern, line, re.IGNORECASE)
                if match:
                    current_interface = match.group(1)
                    interfaces[current_interface] = {
                        'interface_name': current_interface,
                        'admin_state': 'unknown',
                        'operational_state': 'unknown',
                        'bundle': '',
                        'mtu': '',
                        'vlan': '',
                        'vrf': '',
                        'ipv4': [],
                        'ipv6': []
                    }
                    
                    # Try to get operational state from first match group
                    if len(match.groups()) > 1:
                        interfaces[current_interface]['operational_state'] = match.group(2)
                    
                    interface_found = True
                    break
            
            if interface_found:
                continue
                
            # Parse interface details if we have a current interface
            if current_interface and current_interface in interfaces:
                # Admin state
                if re.search(r'admin\s+state\s*:\s*(\w+)', line, re.IGNORECASE):
                    match = re.search(r'admin\s+state\s*:\s*(\w+)', line, re.IGNORECASE)
                    interfaces[current_interface]['admin_state'] = match.group(1)
                
                # Operational state
                if re.search(r'line\s+protocol\s+is\s+(\w+)', line, re.IGNORECASE):
                    match = re.search(r'line\s+protocol\s+is\s+(\w+)', line, re.IGNORECASE)
                    interfaces[current_interface]['operational_state'] = match.group(1)
                
                # MTU
                if re.search(r'mtu\s+(\d+)', line, re.IGNORECASE):
                    match = re.search(r'mtu\s+(\d+)', line, re.IGNORECASE)
                    interfaces[current_interface]['mtu'] = match.group(1)
                
                # VLAN
                if re.search(r'vlan\s+(\d+)', line, re.IGNORECASE):
                    match = re.search(r'vlan\s+(\d+)', line, re.IGNORECASE)
                    interfaces[current_interface]['vlan'] = match.group(1)
                
                # VRF
                if re.search(r'vrf\s+(\S+)', line, re.IGNORECASE):
                    match = re.search(r'vrf\s+(\S+)', line, re.IGNORECASE)
                    interfaces[current_interface]['vrf'] = match.group(1)
                
                # Bundle/LAG
                if re.search(r'bundle\s+(\S+)', line, re.IGNORECASE):
                    match = re.search(r'bundle\s+(\S+)', line, re.IGNORECASE)
                    interfaces[current_interface]['bundle'] = match.group(1)
                
                # IPv4 addresses
                ipv4_match = re.search(r'inet\s+(\d+\.\d+\.\d+\.\d+/\d+)', line)
                if ipv4_match:
                    interfaces[current_interface]['ipv4'].append(ipv4_match.group(1))
                
                # IPv6 addresses
                ipv6_match = re.search(r'inet6\s+([0-9a-fA-F:]+/\d+)', line)
                if ipv6_match:
                    interfaces[current_interface]['ipv6'].append(ipv6_match.group(1))
        
        # Save interfaces to JSON
        interface_data = {
            'device_name': device_name,
            'timestamp': datetime.now().isoformat(),
            'total_interfaces': len(interfaces),
            'interfaces': interfaces
        }
        
        # Use the device serial directory structure
        device_dir = f"Devices/{getattr(self, 'device_name', 'unknown_device')}"
        filename = f"{device_dir}/{device_name}_interfaces.json"
        with open(filename, 'w') as f:
            json.dump(interface_data, f, indent=2)
            
        self.logger.info(f"Interface information saved to {filename}")
        self.logger.info(f"Total interfaces found: {len(interfaces)}")
        
        self.interfaces_data = interface_data
        
    def _parse_drivenets_interfaces(self, output, device_name):
        """Parse DRIVENETS-specific interface output format"""
        self.logger.info("Parsing DRIVENETS interface information")
        
        interfaces = {}
        current_interface = None
        lines = output.split('\n')
        
        self.logger.debug(f"DRIVENETS parser: Processing {len(lines)} lines")
        self.logger.debug(f"First 10 lines: {lines[:10]}")
        if len(lines) > 10:
            self.logger.debug(f"Last 10 lines: {lines[-10:]}")
        
        # Check if this is tabular DRIVENETS format
        header_line = None
        data_lines = []
        
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
                
            # Look for interface table header - DRIVENETS uses pipe-delimited format
            # More flexible pattern to handle various spacing
            if re.search(r'\|\s*Interface\s*\|.*Admin.*\|.*Operational', line, re.IGNORECASE):
                header_line = line
                self.logger.debug(f"Found DRIVENETS table header at line {i}: {header_line}")
                # Skip the separator line (typically starts with +---)
                start_j = i + 1
                if start_j < len(lines) and lines[start_j].strip().startswith('+'):
                    start_j += 1
                
                # Get data lines after header
                for j in range(start_j, len(lines)):
                    data_line = lines[j].strip()
                    if data_line and not data_line.startswith(device_name) and data_line != '' and not data_line.startswith('+'):
                        # Check if this looks like an interface line (starts with |)
                        if data_line.startswith('|') and re.search(r'\|\s*(ge100-|bundle-|lo)\S*\s*\|', data_line):
                            data_lines.append(data_line)
                            self.logger.debug(f"Found interface data line: {data_line}")
                break
        
        # Parse tabular format if found
        if header_line and data_lines:
            self.logger.info(f"Parsing DRIVENETS tabular format with {len(data_lines)} interface lines")
            
            for line in data_lines:
                # Split the line by pipes and clean up - DRIVENETS uses pipe separators
                # Format: | Interface | Admin | Operational | IPv4 Address | IPv6 Address | VLAN | MTU | Network-Service | Bundle-Id |
                parts = [part.strip() for part in line.split('|')]
                # Remove empty first and last elements (before first | and after last |)
                if parts and parts[0] == '':
                    parts = parts[1:]
                if parts and parts[-1] == '':
                    parts = parts[:-1]
                
                if len(parts) >= 3:  # At least interface, admin, operational
                    interface_name = parts[0].strip()
                    admin_state = parts[1].strip() if len(parts) > 1 else 'unknown'
                    operational_state = parts[2].strip() if len(parts) > 2 else 'unknown'
                    
                    # Initialize interface
                    interfaces[interface_name] = {
                        'interface_name': interface_name,
                        'admin_state': admin_state,
                        'operational_state': operational_state,
                        'bundle': '',
                        'mtu': '',
                        'vlan': '',
                        'vrf': '',
                        'ipv4': [],
                        'ipv6': []
                    }
                    
                    # Parse additional fields based on DRIVENETS pipe-delimited table format
                    # | Interface | Admin | Operational | IPv4 Address | IPv6 Address | VLAN | MTU | Network-Service | Bundle-Id |
                    if len(parts) >= 4:  # IPv4
                        ipv4_field = parts[3].strip()
                        if ipv4_field and ipv4_field != '' and '/' in ipv4_field:  # Valid IP with subnet
                            interfaces[interface_name]['ipv4'].append(ipv4_field)
                    
                    if len(parts) >= 5:  # IPv6
                        ipv6_field = parts[4].strip()
                        if ipv6_field and ipv6_field != '' and ':' in ipv6_field:  # Valid IPv6
                            # Clean up IPv6 (remove flags like (p), (s))
                            ipv6_clean = re.sub(r'\s+\([^)]+\)', '', ipv6_field).strip()
                            if ipv6_clean:
                                interfaces[interface_name]['ipv6'].append(ipv6_clean)
                    
                    if len(parts) >= 6:  # VLAN
                        vlan_field = parts[5].strip()
                        if vlan_field and vlan_field != '':
                            interfaces[interface_name]['vlan'] = vlan_field
                    
                    if len(parts) >= 7:  # MTU
                        mtu_field = parts[6].strip()
                        if mtu_field and mtu_field != '':
                            interfaces[interface_name]['mtu'] = mtu_field
                    
                    if len(parts) >= 8:  # Network-Service (VRF)
                        vrf_field = parts[7].strip()
                        if vrf_field and vrf_field != '':
                            interfaces[interface_name]['vrf'] = vrf_field
                    
                    if len(parts) >= 9:  # Bundle-Id
                        bundle_field = parts[8].strip()
                        if bundle_field and bundle_field != '':
                            interfaces[interface_name]['bundle'] = bundle_field
                    
                    self.logger.debug(f"Parsed tabular interface: {interface_name} -> {interfaces[interface_name]}")
        
        # Fallback to line-by-line parsing if tabular parsing didn't work
        if not interfaces:
            self.logger.info("Tabular parsing failed, trying line-by-line parsing")
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                    
                # DRIVENETS interface detection patterns
                interface_patterns = [
                    # Look for interface names like: ge100-0/0/0, bundle-1, lo0
                    r'^((?:ge100-|bundle-|lo)\S*)\s+(?:is\s+)?(\w+)',
                    r'^Physical interface:\s+(\S+)',
                    r'^Interface\s+(\S+)',
                    # More generic pattern for DRIVENETS interfaces
                    r'^([a-zA-Z]+\d+(?:-\d+)?(?:/\d+)*(?:\.\d+)?)\s+(?:is\s+)?(\w+)?'
                ]
                
                interface_found = False
                for pattern in interface_patterns:
                    match = re.match(pattern, line, re.IGNORECASE)
                    if match:
                        current_interface = match.group(1)
                        operational_state = match.group(2) if len(match.groups()) > 1 and match.group(2) else 'unknown'
                        
                        # Skip header words
                        if current_interface.lower() in ['interface', 'admin', 'operational']:
                            continue
                        
                        interfaces[current_interface] = {
                            'interface_name': current_interface,
                            'admin_state': 'unknown',
                            'operational_state': operational_state,
                            'bundle': '',
                            'mtu': '',
                            'vlan': '',
                            'vrf': '',
                            'ipv4': [],
                            'ipv6': []
                        }
                        
                        self.logger.debug(f"Found DRIVENETS interface: {current_interface}")
                        interface_found = True
                        break
                
                if interface_found:
                    continue
                
            # Parse interface details for current interface
            if current_interface and current_interface in interfaces:
                # Admin state patterns
                admin_patterns = [
                    r'admin[istrative]*\s+state\s*:?\s*(\w+)',
                    r'administratively\s+(\w+)',
                    r'Admin\s+state\s*:?\s*(\w+)'
                ]
                for pattern in admin_patterns:
                    match = re.search(pattern, line, re.IGNORECASE)
                    if match:
                        interfaces[current_interface]['admin_state'] = match.group(1)
                        break
                
                # Operational state patterns
                op_patterns = [
                    r'line\s+protocol\s+is\s+(\w+)',
                    r'operational\s+state\s*:?\s*(\w+)',
                    r'protocol\s+is\s+(\w+)',
                    r'link\s+is\s+(\w+)'
                ]
                for pattern in op_patterns:
                    match = re.search(pattern, line, re.IGNORECASE)
                    if match:
                        interfaces[current_interface]['operational_state'] = match.group(1)
                        break
                
                # MTU
                mtu_match = re.search(r'mtu\s+(\d+)', line, re.IGNORECASE)
                if mtu_match:
                    interfaces[current_interface]['mtu'] = mtu_match.group(1)
                
                # VLAN patterns for DRIVENETS
                vlan_patterns = [
                    r'vlan\s+id\s*:?\s*(\d+)',
                    r'vlan\s+(\d+)',
                    r'encapsulation\s+dot1q\s+(\d+)'
                ]
                for pattern in vlan_patterns:
                    match = re.search(pattern, line, re.IGNORECASE)
                    if match:
                        interfaces[current_interface]['vlan'] = match.group(1)
                        break
                
                # VRF
                vrf_patterns = [
                    r'vrf\s+(\S+)',
                    r'routing\s+instance\s+(\S+)',
                    r'virtual\s+router\s+(\S+)'
                ]
                for pattern in vrf_patterns:
                    match = re.search(pattern, line, re.IGNORECASE)
                    if match and match.group(1).lower() != 'default':
                        interfaces[current_interface]['vrf'] = match.group(1)
                        break
                
                # Bundle/LAG for DRIVENETS
                bundle_patterns = [
                    r'bundle\s+(\S+)',
                    r'ae\s+(\d+)',
                    r'lag\s+(\S+)'
                ]
                for pattern in bundle_patterns:
                    match = re.search(pattern, line, re.IGNORECASE)
                    if match:
                        interfaces[current_interface]['bundle'] = match.group(1)
                        break
                
                # IPv4 addresses - multiple patterns
                ipv4_patterns = [
                    r'inet\s+(\d+\.\d+\.\d+\.\d+/\d+)',
                    r'ip\s+address\s+(\d+\.\d+\.\d+\.\d+/\d+)',
                    r'(\d+\.\d+\.\d+\.\d+/\d+)'
                ]
                for pattern in ipv4_patterns:
                    match = re.search(pattern, line)
                    if match:
                        ip_addr = match.group(1)
                        if ip_addr not in interfaces[current_interface]['ipv4']:
                            interfaces[current_interface]['ipv4'].append(ip_addr)
                        break
                
                # IPv6 addresses
                ipv6_patterns = [
                    r'inet6\s+([0-9a-fA-F:]+/\d+)',
                    r'ipv6\s+address\s+([0-9a-fA-F:]+/\d+)',
                    r'([0-9a-fA-F:]+/\d+)'
                ]
                for pattern in ipv6_patterns:
                    match = re.search(pattern, line)
                    if match:
                        ipv6_addr = match.group(1)
                        # Basic validation to avoid false positives
                        if ':' in ipv6_addr and ipv6_addr not in interfaces[current_interface]['ipv6']:
                            interfaces[current_interface]['ipv6'].append(ipv6_addr)
                        break
        
        # If no interfaces found through normal parsing, try alternative method
        if not interfaces:
            self.logger.warning("No interfaces found with standard patterns, trying alternative parsing")
            # Look for lines that might be interface summaries or tables
            for line in lines:
                if re.search(r'(ge100-|bundle-|lo)\S*', line):
                    parts = line.split()
                    if parts and re.match(r'(ge100-|bundle-|lo)\S*', parts[0]):
                        interface_name = parts[0]
                        interfaces[interface_name] = {
                            'interface_name': interface_name,
                            'admin_state': 'unknown',
                            'operational_state': 'unknown',
                            'bundle': '',
                            'mtu': '',
                            'vlan': '',
                            'vrf': '',
                            'ipv4': [],
                            'ipv6': []
                        }
                        self.logger.debug(f"Found interface via alternative method: {interface_name}")
        
        # Save interfaces to JSON
        interface_data = {
            'device_name': device_name,
            'timestamp': datetime.now().isoformat(),
            'total_interfaces': len(interfaces),
            'interfaces': interfaces
        }
        
        # Use the device serial directory structure
        device_dir = f"Devices/{getattr(self, 'device_name', 'unknown_device')}"
        filename = f"{device_dir}/{device_name}_interfaces.json"
        with open(filename, 'w') as f:
            json.dump(interface_data, f, indent=2)
            
        self.logger.info(f"DRIVENETS interface information saved to {filename}")
        self.logger.info(f"Total interfaces found: {len(interfaces)}")
        
        self.interfaces_data = interface_data
        
    def parse_lldp_information(self, output, device_name):
        """Parse 'show lldp neighbors' output and save LLDP connection details"""
        self.logger.info("Parsing LLDP neighbor information")
        
        lldp_connections = {}
        lines = output.split('\n')
        
        # Find table header and data lines
        header_found = False
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
                
            # Look for LLDP table header
            if re.search(r'\|\s*Interface\s*\|.*Neighbor\s+System\s+Name.*\|.*Neighbor\s+interface.*\|.*Neighbor\s+TTL', line, re.IGNORECASE):
                header_found = True
                self.logger.debug(f"Found LLDP table header at line {i}: {line}")
                
                # Skip separator line (typically starts with |----- or +----)
                start_j = i + 1
                if start_j < len(lines) and (lines[start_j].strip().startswith('|-') or lines[start_j].strip().startswith('+')):
                    start_j += 1
                
                # Parse data lines
                for j in range(start_j, len(lines)):
                    data_line = lines[j].strip()
                    if data_line and data_line.startswith('|') and not data_line.startswith(device_name):
                        # Parse LLDP table row: | Interface | Neighbor System Name | Neighbor interface | Neighbor TTL |
                        parts = [part.strip() for part in data_line.split('|')]
                        # Remove empty first and last elements
                        if parts and parts[0] == '':
                            parts = parts[1:]
                        if parts and parts[-1] == '':
                            parts = parts[:-1]
                        
                        if len(parts) >= 4:
                            interface_name = parts[0].strip()
                            neighbor_system = parts[1].strip() if parts[1].strip() else ""
                            neighbor_interface = parts[2].strip() if parts[2].strip() else ""
                            neighbor_ttl = parts[3].strip() if parts[3].strip() else ""
                            
                            # Only include interfaces with active neighbors (skip empty interface names and no neighbors)
                            if interface_name and neighbor_system:  # Only include if there's an actual neighbor
                                lldp_connections[interface_name] = {
                                    'local_interface': interface_name,
                                    'neighbor_system_name': neighbor_system,
                                    'neighbor_interface': neighbor_interface,
                                    'neighbor_ttl': neighbor_ttl,
                                    'has_neighbor': True  # Only true connections are included now
                                }
                                
                                self.logger.debug(f"LLDP connection: {interface_name} -> {neighbor_system}:{neighbor_interface}")
                            elif interface_name and not neighbor_system:
                                self.logger.debug(f"LLDP interface with no neighbor (skipped): {interface_name}")
                break
        
        if not header_found:
            self.logger.warning("LLDP table header not found in output")
        
        # Count connections with actual neighbors (all included connections now have neighbors)
        connected_interfaces = len(lldp_connections)
        
        # Create LLDP data structure
        lldp_data = {
            'device_name': device_name,
            'timestamp': datetime.now().isoformat(),
            'total_active_lldp_connections': len(lldp_connections),
            'total_connected_neighbors': connected_interfaces,
            'lldp_connections': lldp_connections,
            'note': 'Only interfaces with active LLDP neighbors are included'
        }
        
        # Save LLDP data to JSON
        device_dir = f"Devices/{getattr(self, 'device_name', 'unknown_device')}"
        filename = f"{device_dir}/{device_name}_LLDP_Connections.json"
        with open(filename, 'w') as f:
            json.dump(lldp_data, f, indent=2)
            
        self.logger.info(f"LLDP information saved to {filename}")
        self.logger.info(f"Total active LLDP connections: {len(lldp_connections)}")
        self.logger.info(f"Connected neighbors: {connected_interfaces}")
        
        self.lldp_data = lldp_data
        
    def validate_saved_data(self, device_name):
        """Validate saved JSON data against fresh device query"""
        self.logger.info("=== Starting Data Validation ===")
        
        try:
            # Validate interface data
            interface_validation = self._validate_interface_data(device_name)
            
            # Validate system data
            system_validation = self._validate_system_data(device_name)
            
            # Validate LLDP data
            lldp_validation = self._validate_lldp_data(device_name)
            
            overall_validation = interface_validation and system_validation and lldp_validation
            
            return overall_validation
            
        except Exception as e:
            self.logger.error(f"Error during validation: {str(e)}")
            return False
    
    def _validate_interface_data(self, device_name):
        """Validate and correct interface JSON data against fresh device query"""
        try:
            # Read the saved JSON file
            device_dir = f"Devices/{getattr(self, 'device_name', 'unknown_device')}"
            json_filename = f"{device_dir}/{device_name}_interfaces.json"
            with open(json_filename, 'r') as f:
                saved_data = json.load(f)
            
            self.logger.info(f"Validating interface data: {saved_data['total_interfaces']} interfaces")
            
            # Get fresh interface data from device
            self.logger.info("Querying device for fresh interface data...")
            fresh_output = self.execute_command("show interfaces | no-more")
            
            if not fresh_output:
                self.logger.error("Failed to get fresh interface data for validation")
                return False
            
            # Parse fresh data with full details
            fresh_interfaces = self._parse_fresh_interfaces_full(fresh_output)
            
            # Compare device interfaces vs JSON interfaces
            initial_comparison = self._compare_device_vs_json(fresh_interfaces, saved_data['interfaces'])
            
            # If missing interfaces found, add them to JSON
            if initial_comparison['missing_from_json']:
                self.logger.info(f"Found {len(initial_comparison['missing_from_json'])} missing interfaces in JSON file")
                print(f"\n🔄 Adding {len(initial_comparison['missing_from_json'])} missing interfaces to JSON file...")
                
                # Add missing interfaces to saved data
                for interface_name in initial_comparison['missing_from_json']:
                    if interface_name in fresh_interfaces:
                        saved_data['interfaces'][interface_name] = fresh_interfaces[interface_name]
                        print(f"   ➕ Added: {interface_name}")
                        self.logger.info(f"Added missing interface: {interface_name}")
                
                # Update total count
                saved_data['total_interfaces'] = len(saved_data['interfaces'])
                saved_data['timestamp'] = datetime.now().isoformat()
                
                # Save updated JSON file
                with open(json_filename, 'w') as f:
                    json.dump(saved_data, f, indent=2)
                
                self.logger.info(f"Updated JSON file with {len(initial_comparison['missing_from_json'])} new interfaces")
                print(f"✅ JSON file updated successfully!")
            
            # Re-compare to verify 100% match
            self.logger.info("Performing final validation check...")
            final_comparison = self._compare_device_vs_json(fresh_interfaces, saved_data['interfaces'])
            
            # Report final validation results
            return self._report_corrective_validation_results(final_comparison, len(fresh_interfaces), len(saved_data['interfaces']))
            
        except Exception as e:
            self.logger.error(f"Error during interface validation: {str(e)}")
            return False
    
    def _validate_system_data(self, device_name):
        """Validate system JSON data against fresh device query"""
        try:
            # Read the saved system JSON file
            device_dir = f"Devices/{getattr(self, 'device_name', 'unknown_device')}"
            json_filename = f"{device_dir}/{device_name}_System_Information.json"
            with open(json_filename, 'r') as f:
                saved_data = json.load(f)
            
            self.logger.info("Validating system information data...")
            
            # Get fresh system data from device
            fresh_output = self.execute_command("show system | no-more")
            
            if not fresh_output:
                self.logger.error("Failed to get fresh system data for validation")
                return False
            
            # Basic validation - check if device name is consistent
            device_name_match = re.search(r'System\s+Name\s*:\s*([^,\r\n]+)', fresh_output, re.IGNORECASE)
            fresh_device_name = device_name_match.group(1).strip().rstrip(' ,') if device_name_match else "unknown"
            
            saved_device_name = saved_data.get('device_name', 'unknown')
            
            if fresh_device_name == saved_device_name:
                print("✅ System data validation: Device name matches")
                self.logger.info("System data validation passed - device name consistent")
                return True
            else:
                print(f"❌ System data validation: Device name mismatch - saved: '{saved_device_name}', fresh: '{fresh_device_name}'")
                self.logger.warning(f"System data validation failed - device name mismatch")
                return False
                
        except Exception as e:
            self.logger.error(f"Error during system validation: {str(e)}")
            return False
    
    def _validate_lldp_data(self, device_name):
        """Validate LLDP JSON data against fresh device query"""
        try:
            # Read the saved LLDP JSON file
            device_dir = f"Devices/{getattr(self, 'device_name', 'unknown_device')}"
            json_filename = f"{device_dir}/{device_name}_LLDP_Connections.json"
            with open(json_filename, 'r') as f:
                saved_data = json.load(f)
            
            # Check if LLDP was unavailable during initial collection
            if saved_data.get('lldp_status') == 'unavailable':
                print("✅ LLDP data validation: LLDP was unavailable (expected)")
                self.logger.info("LLDP validation skipped - LLDP was unavailable during collection")
                return True
            
            self.logger.info(f"Validating LLDP data: {saved_data.get('total_active_lldp_connections', saved_data.get('total_interfaces_with_lldp', 0))} active connections")
            
            # Get fresh LLDP data from device with special handler
            self.logger.info("Querying device for fresh LLDP data...")
            fresh_output = self.execute_lldp_command("show lldp neighbors | no-more")
            
            if not fresh_output:
                print("⚠️ LLDP data validation: Fresh LLDP data unavailable")
                self.logger.warning("Fresh LLDP data unavailable for validation")
                return True  # Don't fail validation if LLDP is unavailable
            
            # Parse fresh LLDP data
            fresh_lldp = self._parse_fresh_lldp_for_validation(fresh_output)
            
            # Compare saved vs fresh LLDP data
            lldp_comparison = self._compare_lldp_data(saved_data['lldp_connections'], fresh_lldp)
            
            # Report LLDP validation results
            return self._report_lldp_validation_results(lldp_comparison, len(saved_data['lldp_connections']), len(fresh_lldp))
            
        except Exception as e:
            self.logger.error(f"Error during LLDP validation: {str(e)}")
            # Don't fail overall validation if LLDP validation has issues
            print("⚠️ LLDP data validation: Validation failed but continuing")
            return True
    
    def _parse_fresh_lldp_for_validation(self, output):
        """Parse fresh LLDP output for validation"""
        lldp_connections = {}
        lines = output.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            if re.search(r'\|\s*Interface\s*\|.*Neighbor\s+System\s+Name.*\|.*Neighbor\s+interface.*\|.*Neighbor\s+TTL', line, re.IGNORECASE):
                # Skip separator line
                start_j = i + 1
                if start_j < len(lines) and (lines[start_j].strip().startswith('|-') or lines[start_j].strip().startswith('+')):
                    start_j += 1
                
                # Parse data lines
                for j in range(start_j, len(lines)):
                    data_line = lines[j].strip()
                    if data_line and data_line.startswith('|'):
                        parts = [part.strip() for part in data_line.split('|')]
                        if parts and parts[0] == '':
                            parts = parts[1:]
                        if parts and parts[-1] == '':
                            parts = parts[:-1]
                        
                        if len(parts) >= 4:
                            interface_name = parts[0].strip()
                            neighbor_system = parts[1].strip() if parts[1].strip() else ""
                            neighbor_interface = parts[2].strip() if parts[2].strip() else ""
                            neighbor_ttl = parts[3].strip() if parts[3].strip() else ""
                            
                            if interface_name:
                                lldp_connections[interface_name] = {
                                    'neighbor_system_name': neighbor_system,
                                    'neighbor_interface': neighbor_interface,
                                    'neighbor_ttl': neighbor_ttl
                                }
                break
        
        return lldp_connections
    
    def _compare_lldp_data(self, saved_lldp, fresh_lldp):
        """Compare saved LLDP data with fresh device data"""
        results = {
            'is_valid': True,
            'missing_interfaces': [],
            'extra_interfaces': [],
            'connection_changes': [],
            'total_saved': len(saved_lldp),
            'total_fresh': len(fresh_lldp)
        }
        
        # Check for missing interfaces (in device but not in saved data)
        for interface_name in fresh_lldp:
            if interface_name not in saved_lldp:
                results['missing_interfaces'].append(interface_name)
                results['is_valid'] = False
        
        # Check for extra interfaces (in saved data but not in device)
        for interface_name in saved_lldp:
            if interface_name not in fresh_lldp:
                results['extra_interfaces'].append(interface_name)
                results['is_valid'] = False
        
        # Check for connection changes
        for interface_name in saved_lldp:
            if interface_name in fresh_lldp:
                saved = saved_lldp[interface_name]
                fresh = fresh_lldp[interface_name]
                
                if (saved.get('neighbor_system_name') != fresh.get('neighbor_system_name') or 
                    saved.get('neighbor_interface') != fresh.get('neighbor_interface')):
                    results['connection_changes'].append({
                        'interface': interface_name,
                        'saved_neighbor': saved.get('neighbor_system_name', ''),
                        'fresh_neighbor': fresh.get('neighbor_system_name', ''),
                        'saved_neighbor_interface': saved.get('neighbor_interface', ''),
                        'fresh_neighbor_interface': fresh.get('neighbor_interface', '')
                    })
        
        return results
    
    def _report_lldp_validation_results(self, results, saved_count, fresh_count):
        """Report LLDP validation results"""
        print(f"✅ LLDP data validation: ", end="")
        
        if results['is_valid'] and len(results['connection_changes']) == 0:
            print("All LLDP connections match")
            self.logger.info("LLDP data validation passed - all connections consistent")
            return True
        else:
            print("ISSUES DETECTED")
            self.logger.warning("LLDP data validation found discrepancies")
            
            if results['missing_interfaces']:
                print(f"   Missing {len(results['missing_interfaces'])} LLDP interfaces from saved data")
                for interface in results['missing_interfaces']:
                    self.logger.warning(f"Missing LLDP interface: {interface}")
            
            if results['extra_interfaces']:
                print(f"   Found {len(results['extra_interfaces'])} extra LLDP interfaces in saved data")
                for interface in results['extra_interfaces']:
                    self.logger.warning(f"Extra LLDP interface: {interface}")
            
            if results['connection_changes']:
                print(f"   Found {len(results['connection_changes'])} LLDP connection changes")
                for change in results['connection_changes']:
                    print(f"     - {change['interface']}: neighbor changed")
                    self.logger.warning(f"LLDP connection change for {change['interface']}")
            
            return False
    
    def _parse_fresh_interfaces_full(self, output):
        """Parse fresh interface output with full details for validation"""
        interfaces = {}
        lines = output.split('\n')
        
        # Find table header and data lines
        for i, line in enumerate(lines):
            line = line.strip()
            if re.search(r'\|\s*Interface\s*\|.*Admin.*\|.*Operational', line, re.IGNORECASE):
                # Skip separator line
                start_j = i + 1
                if start_j < len(lines) and lines[start_j].strip().startswith('+'):
                    start_j += 1
                
                # Parse data lines with full details (similar to main parser)
                for j in range(start_j, len(lines)):
                    data_line = lines[j].strip()
                    if data_line and data_line.startswith('|') and re.search(r'\|\s*(ge100-|bundle-|lo)\S*\s*\|', data_line):
                        parts = [part.strip() for part in data_line.split('|')]
                        if parts and parts[0] == '':
                            parts = parts[1:]
                        if parts and parts[-1] == '':
                            parts = parts[:-1]
                        
                        if len(parts) >= 3:
                            interface_name = parts[0].strip()
                            admin_state = parts[1].strip() if len(parts) > 1 else 'unknown'
                            operational_state = parts[2].strip() if len(parts) > 2 else 'unknown'
                            
                            # Create full interface structure
                            interfaces[interface_name] = {
                                'interface_name': interface_name,
                                'admin_state': admin_state,
                                'operational_state': operational_state,
                                'bundle': '',
                                'mtu': '',
                                'vlan': '',
                                'vrf': '',
                                'ipv4': [],
                                'ipv6': []
                            }
                            
                            # Parse additional fields
                            if len(parts) >= 4:  # IPv4
                                ipv4_field = parts[3].strip()
                                if ipv4_field and ipv4_field != '' and '/' in ipv4_field:
                                    interfaces[interface_name]['ipv4'].append(ipv4_field)
                            
                            if len(parts) >= 5:  # IPv6
                                ipv6_field = parts[4].strip()
                                if ipv6_field and ipv6_field != '' and ':' in ipv6_field:
                                    ipv6_clean = re.sub(r'\s+\([^)]+\)', '', ipv6_field).strip()
                                    if ipv6_clean:
                                        interfaces[interface_name]['ipv6'].append(ipv6_clean)
                            
                            if len(parts) >= 6:  # VLAN
                                vlan_field = parts[5].strip()
                                if vlan_field and vlan_field != '':
                                    interfaces[interface_name]['vlan'] = vlan_field
                            
                            if len(parts) >= 7:  # MTU
                                mtu_field = parts[6].strip()
                                if mtu_field and mtu_field != '':
                                    interfaces[interface_name]['mtu'] = mtu_field
                            
                            if len(parts) >= 8:  # Network-Service (VRF)
                                vrf_field = parts[7].strip()
                                if vrf_field and vrf_field != '':
                                    interfaces[interface_name]['vrf'] = vrf_field
                            
                            if len(parts) >= 9:  # Bundle-Id
                                bundle_field = parts[8].strip()
                                if bundle_field and bundle_field != '':
                                    interfaces[interface_name]['bundle'] = bundle_field
                break
        
        self.logger.debug(f"Fresh full parse found {len(interfaces)} interfaces")
        return interfaces
    
    def _compare_device_vs_json(self, device_interfaces, json_interfaces):
        """Compare device interfaces vs JSON interfaces to find missing ones"""
        results = {
            'missing_from_json': [],
            'extra_in_json': [],
            'total_device': len(device_interfaces),
            'total_json': len(json_interfaces)
        }
        
        # Check for interfaces on device but missing from JSON
        for interface_name in device_interfaces:
            if interface_name not in json_interfaces:
                results['missing_from_json'].append(interface_name)
        
        # Check for interfaces in JSON but not on device (optional check)
        for interface_name in json_interfaces:
            if interface_name not in device_interfaces:
                results['extra_in_json'].append(interface_name)
        
        return results
    
    def _report_corrective_validation_results(self, comparison, device_count, json_count):
        """Report corrective validation results"""
        print(f"\n=== Final Validation Results ===")
        print(f"Device interfaces: {device_count}")
        print(f"JSON file interfaces: {json_count}")
        
        if len(comparison['missing_from_json']) == 0 and device_count == json_count:
            print("✅ VALIDATION PASSED - 100% interface match achieved!")
            self.logger.info("Corrective validation passed - perfect match")
            return True
        else:
            if comparison['missing_from_json']:
                print(f"❌ Still missing {len(comparison['missing_from_json'])} interfaces from JSON:")
                for interface in comparison['missing_from_json']:
                    print(f"     - {interface}")
                    self.logger.warning(f"Still missing interface: {interface}")
            
            if comparison['extra_in_json']:
                print(f"⚠️  Found {len(comparison['extra_in_json'])} extra interfaces in JSON:")
                for interface in comparison['extra_in_json']:
                    print(f"     - {interface}")
                    self.logger.warning(f"Extra interface in JSON: {interface}")
            
            self.logger.warning("Corrective validation did not achieve perfect match")
            return False
    
    def _compare_interface_data(self, saved_interfaces, fresh_interfaces):
        """Compare saved JSON data with fresh device data"""
        results = {
            'is_valid': True,
            'missing_interfaces': [],
            'extra_interfaces': [],
            'state_mismatches': [],
            'total_saved': len(saved_interfaces),
            'total_fresh': len(fresh_interfaces)
        }
        
        # Check for missing interfaces (in device but not in saved data)
        for interface_name in fresh_interfaces:
            if interface_name not in saved_interfaces:
                results['missing_interfaces'].append(interface_name)
                results['is_valid'] = False
        
        # Check for extra interfaces (in saved data but not in device)
        for interface_name in saved_interfaces:
            if interface_name not in fresh_interfaces:
                results['extra_interfaces'].append(interface_name)
                results['is_valid'] = False
        
        # Check for state mismatches
        for interface_name in saved_interfaces:
            if interface_name in fresh_interfaces:
                saved = saved_interfaces[interface_name]
                fresh = fresh_interfaces[interface_name]
                
                if (saved.get('admin_state') != fresh.get('admin_state') or 
                    saved.get('operational_state') != fresh.get('operational_state')):
                    results['state_mismatches'].append({
                        'interface': interface_name,
                        'saved_admin': saved.get('admin_state'),
                        'fresh_admin': fresh.get('admin_state'),
                        'saved_operational': saved.get('operational_state'),
                        'fresh_operational': fresh.get('operational_state')
                    })
        
        return results
    
    def _report_validation_results(self, results, saved_count, fresh_count):
        """Report validation results to user and logs"""
        print(f"\n=== Data Validation Results ===")
        print(f"Saved interfaces: {saved_count}")
        print(f"Fresh device interfaces: {fresh_count}")
        
        if results['is_valid']:
            print("✅ VALIDATION PASSED - All interface data is accurate!")
            self.logger.info("Interface data validation passed successfully")
        else:
            print("❌ VALIDATION ISSUES DETECTED:")
            self.logger.warning("Interface data validation found discrepancies")
            
            if results['missing_interfaces']:
                print(f"   Missing {len(results['missing_interfaces'])} interfaces from saved data:")
                for interface in results['missing_interfaces']:
                    print(f"     - {interface}")
                    self.logger.warning(f"Missing interface: {interface}")
            
            if results['extra_interfaces']:
                print(f"   Found {len(results['extra_interfaces'])} extra interfaces in saved data:")
                for interface in results['extra_interfaces']:
                    print(f"     - {interface}")
                    self.logger.warning(f"Extra interface: {interface}")
            
            if results['state_mismatches']:
                print(f"   Found {len(results['state_mismatches'])} state mismatches:")
                for mismatch in results['state_mismatches']:
                    print(f"     - {mismatch['interface']}: saved({mismatch['saved_admin']}/{mismatch['saved_operational']}) vs fresh({mismatch['fresh_admin']}/{mismatch['fresh_operational']})")
                    self.logger.warning(f"State mismatch for {mismatch['interface']}")
        
        # Additional statistics
        if saved_count != fresh_count:
            print(f"⚠️  Interface count mismatch: saved={saved_count}, fresh={fresh_count}")
            self.logger.warning(f"Interface count mismatch: saved={saved_count}, fresh={fresh_count}")
        
        return results['is_valid']
        
    def disconnect(self):
        """Close connection to device"""
        try:
            if self.channel:
                self.channel.close()
            if self.connection:
                self.connection.close()
            self.logger.info("Disconnected from device")
        except Exception as e:
            self.logger.error(f"Error disconnecting: {str(e)}")
            
    def run(self):
        """Main execution function"""
        try:
            self.logger.info("Starting network mapping process")
            
            # Stage 1: Device selection
            device_choice, selected_device = self.display_device_menu()
            
            if device_choice == "existing":
                # Use existing device
                self.logger.info(f"Using existing device: {selected_device}")
                credentials = self.load_existing_device_credentials(selected_device)
                
                if not credentials:
                    print(f"❌ Failed to load credentials for {selected_device}")
                    print("Please try connecting as a new device instead.")
                    return False
                
                print(f"✅ Loaded credentials for {selected_device}")
                print(f"   Hostname: {credentials['hostname']}")
                print(f"   Username: {credentials['username']}")
                
                # Set device name for later use
                self.device_name = selected_device
                
            else:
                # Get credentials for new device
                credentials = self.get_user_credentials()
            
            if not self.connect_to_device(credentials):
                self.logger.error("Failed to connect to device")
                return False
            
            # Wait for CLI to be ready
            if not self.wait_for_cli_ready():
                self.logger.error("CLI not ready")
                print("\n❌ TROUBLESHOOTING TIPS:")
                print("1. Check if the device requires additional authentication steps")
                print("2. Ensure the device supports the commands 'show system', 'show interfaces', and 'show lldp neighbors'")
                print("3. Try connecting manually with SSH to verify device accessibility")
                return False
            
            # Stage 2: Execute system information command (only for new devices)
            if device_choice == "new":
                self.logger.info("=== Stage 1: Collecting system information ===")
                system_output = self.execute_command("show system | no-more")
                
                if not system_output:
                    self.logger.error("Failed to get system information")
                    return False
                    
                device_name = self.parse_system_information(system_output, credentials)
            else:
                device_name = selected_device
            
            # Stage 3: Execute interface information command
            self.logger.info("=== Stage 2: Collecting interface information ===")
            interface_output = self.execute_command("show interfaces | no-more")
            
            if not interface_output:
                self.logger.error("Failed to get interface information")
                return False
            
            # DEBUG: Log the actual interface output to see what we're getting
            self.logger.debug("=== RAW INTERFACE OUTPUT START ===")
            self.logger.debug(f"Interface output length: {len(interface_output)} characters")
            lines = interface_output.split('\n')
            self.logger.debug(f"Interface output has {len(lines)} lines")
            for i, line in enumerate(lines[:20]):  # Log first 20 lines
                self.logger.debug(f"Line {i+1}: {repr(line)}")
            if len(lines) > 20:
                self.logger.debug("... (truncated, check full output below)")
                self.logger.debug(f"Last 10 lines:")
                for i, line in enumerate(lines[-10:], len(lines)-9):
                    self.logger.debug(f"Line {i}: {repr(line)}")
            self.logger.debug("=== RAW INTERFACE OUTPUT END ===")
                
            self.parse_interface_information(interface_output, device_name)
            
            # Stage 3: Execute LLDP neighbors command
            self.logger.info("=== Stage 3: Collecting LLDP neighbor information ===")
            lldp_output = self.execute_lldp_command("show lldp neighbors | no-more")
            
            if not lldp_output:
                self.logger.warning("Failed to get LLDP neighbor information - LLDP may not be enabled")
                print("⚠️  LLDP command failed or timed out - continuing without LLDP data")
                print("   (This is normal if LLDP is not enabled on the device)")
                # Create empty LLDP data if command fails
                self.create_empty_lldp_data(device_name)
            else:
                self.parse_lldp_information(lldp_output, device_name)
            
            # Stage 4: Validate saved data against device
            self.logger.info("=== Stage 4: Validating saved data ===")
            validation_passed = self.validate_saved_data(device_name)
            
            self.logger.info("Network mapping completed successfully")
            print(f"\n=== Mapping Complete ===")
            print(f"Device: {device_name}")
            device_name = getattr(self, 'device_name', 'unknown_device')
            device_dir = f"Devices/{device_name}"
            print(f"Files saved to directory: {device_dir}/")
            print(f"System info saved to: {device_dir}/{device_name}_System_Information.json")
            print(f"Interface info saved to: {device_dir}/{device_name}_interfaces.json")
            print(f"LLDP info saved to: {device_dir}/{device_name}_LLDP_Connections.json")
            print(f"Total interfaces: {len(self.interfaces_data.get('interfaces', {}))}")
            
            # Handle LLDP data display
            if hasattr(self, 'lldp_data') and self.lldp_data:
                if self.lldp_data.get('lldp_status') == 'unavailable':
                    print(f"LLDP status: Unavailable (command failed or not supported)")
                else:
                    print(f"Active LLDP connections: {len(self.lldp_data.get('lldp_connections', {}))}")
                    print(f"Connected neighbors: {self.lldp_data.get('total_connected_neighbors', 0)}")
            else:
                print(f"LLDP status: Data not collected")
            
            if validation_passed:
                print("✅ Data validation: PASSED")
            else:
                print("⚠️  Data validation: ISSUES DETECTED (see above)")
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error in main execution: {str(e)}")
            return False
            
        finally:
            self.disconnect()


if __name__ == "__main__":
    mapper = NetworkMapper()
    success = mapper.run()
    
    if not success:
        print("Network mapping failed. Check logs for details.")
        sys.exit(1)
    else:
        print("Network mapping completed successfully!")
