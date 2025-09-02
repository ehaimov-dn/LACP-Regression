#!/usr/bin/env python3
"""
LACP Regression Test Suite Runner
Runs all test cases in sequence to validate LACP functionality.
"""

import os
import sys
import subprocess
import glob
import json
from typing import Dict, List, Optional, Any

class DeviceManager:
    """Manages access to saved device information"""
    
    def __init__(self, devices_dir: str = None):
        """Initialize the device manager
        
        Args:
            devices_dir: Path to the devices directory. If None, uses default relative path.
        """
        if devices_dir is None:
            # Get the directory where main.py is located
            base_dir = os.path.dirname(os.path.abspath(__file__))
            self.devices_dir = os.path.join(base_dir, "Devices")
        else:
            self.devices_dir = devices_dir
            
        if not os.path.exists(self.devices_dir):
            print(f"⚠️  Warning: Devices directory not found at {self.devices_dir}")
    
    def list_devices(self) -> List[str]:
        """Get a list of all available device names
        
        Returns:
            List of device names (directory names in Devices folder)
        """
        if not os.path.exists(self.devices_dir):
            return []
            
        devices = []
        for item in os.listdir(self.devices_dir):
            device_path = os.path.join(self.devices_dir, item)
            if os.path.isdir(device_path):
                devices.append(item)
        
        return sorted(devices)
    
    def get_device_files(self, device_name: str) -> Dict[str, str]:
        """Get all available files for a specific device
        
        Args:
            device_name: Name of the device
            
        Returns:
            Dictionary mapping file types to file paths
        """
        device_dir = os.path.join(self.devices_dir, device_name)
        if not os.path.exists(device_dir):
            return {}
            
        files = {}
        for file_name in os.listdir(device_dir):
            if file_name.endswith('.json'):
                file_path = os.path.join(device_dir, file_name)
                if 'interfaces' in file_name.lower():
                    files['interfaces'] = file_path
                elif 'lldp' in file_name.lower():
                    files['lldp'] = file_path
                elif 'system' in file_name.lower():
                    files['system'] = file_path
                else:
                    files[file_name] = file_path
        
        return files
    
    def load_device_data(self, device_name: str, data_type: str = 'all') -> Dict[str, Any]:
        """Load device data from JSON files
        
        Args:
            device_name: Name of the device
            data_type: Type of data to load ('interfaces', 'lldp', 'system', or 'all')
            
        Returns:
            Dictionary containing the requested device data
        """
        device_files = self.get_device_files(device_name)
        
        if not device_files:
            print(f"❌ No data files found for device: {device_name}")
            return {}
        
        device_data = {}
        
        if data_type == 'all':
            # Load all available data types
            for file_type, file_path in device_files.items():
                try:
                    with open(file_path, 'r') as f:
                        device_data[file_type] = json.load(f)
                except Exception as e:
                    print(f"⚠️  Error loading {file_type} data for {device_name}: {e}")
        else:
            # Load specific data type
            if data_type in device_files:
                try:
                    with open(device_files[data_type], 'r') as f:
                        device_data[data_type] = json.load(f)
                except Exception as e:
                    print(f"⚠️  Error loading {data_type} data for {device_name}: {e}")
            else:
                print(f"❌ Data type '{data_type}' not available for device: {device_name}")
                print(f"Available types: {list(device_files.keys())}")
        
        return device_data
    
    def get_device_credentials(self, device_name: str) -> Optional[Dict[str, str]]:
        """Get login credentials for a device
        
        Args:
            device_name: Name of the device
            
        Returns:
            Dictionary with hostname, username, password or None if not found
        """
        system_data = self.load_device_data(device_name, 'system')
        
        if 'system' in system_data and 'login_credentials' in system_data['system']:
            return system_data['system']['login_credentials']
        
        return None
    
    def get_device_interfaces(self, device_name: str) -> List[Dict[str, Any]]:
        """Get all interfaces for a device
        
        Args:
            device_name: Name of the device
            
        Returns:
            List of interface dictionaries
        """
        interfaces_data = self.load_device_data(device_name, 'interfaces')
        
        if 'interfaces' in interfaces_data:
            return interfaces_data['interfaces'].get('interfaces', [])
        
        return []
    
    def get_device_lldp_neighbors(self, device_name: str) -> List[Dict[str, Any]]:
        """Get LLDP neighbors for a device
        
        Args:
            device_name: Name of the device
            
        Returns:
            List of LLDP neighbor dictionaries
        """
        lldp_data = self.load_device_data(device_name, 'lldp')
        
        if 'lldp' in lldp_data:
            return lldp_data['lldp'].get('neighbors', [])
        
        return []
    
    def find_lacp_interfaces(self, device_name: str) -> List[Dict[str, Any]]:
        """Find all LACP-enabled interfaces on a device
        
        Args:
            device_name: Name of the device
            
        Returns:
            List of LACP-enabled interface dictionaries
        """
        interfaces = self.get_device_interfaces(device_name)
        lacp_interfaces = []
        
        for interface in interfaces:
            # Check if interface has LACP configuration
            if any(key in str(interface).lower() for key in ['lacp', 'bundle', 'lag']):
                lacp_interfaces.append(interface)
        
        return lacp_interfaces
    
    def print_device_summary(self, device_name: str):
        """Print a summary of device information
        
        Args:
            device_name: Name of the device
        """
        print(f"\n📋 Device Summary: {device_name}")
        print("=" * 50)
        
        # Load system information
        system_data = self.load_device_data(device_name, 'system')
        if 'system' in system_data and 'parsed_info' in system_data['system']:
            info = system_data['system']['parsed_info']
            print(f"System Type: {info.get('system_type', 'Unknown')}")
            print(f"Family: {info.get('family', 'Unknown')}")
            print(f"Version: {info.get('version', 'Unknown')}")
            print(f"Status: {info.get('system_status', 'Unknown')}")
            print(f"Uptime: {info.get('uptime', 'Unknown')}")
        
        # Count interfaces
        interfaces = self.get_device_interfaces(device_name)
        print(f"Total Interfaces: {len(interfaces)}")
        
        # Count LLDP neighbors
        neighbors = self.get_device_lldp_neighbors(device_name)
        print(f"LLDP Neighbors: {len(neighbors)}")
        
        # Find LACP interfaces
        lacp_interfaces = self.find_lacp_interfaces(device_name)
        print(f"LACP Interfaces: {len(lacp_interfaces)}")
        
        # Show credentials (hostname only for security)
        credentials = self.get_device_credentials(device_name)
        if credentials:
            print(f"Hostname: {credentials.get('hostname', 'Unknown')}")


def list_available_devices():
    """List all available devices and their summary"""
    device_manager = DeviceManager()
    devices = device_manager.list_devices()
    
    if not devices:
        print("❌ No devices found in Devices directory")
        return
    
    print(f"\n📱 Available Devices ({len(devices)} found):")
    print("=" * 60)
    
    for device in devices:
        device_manager.print_device_summary(device)
        print()


def access_device(device_name: str, data_type: str = 'all') -> Dict[str, Any]:
    """Access specific device data
    
    Args:
        device_name: Name of the device
        data_type: Type of data to access ('interfaces', 'lldp', 'system', or 'all')
        
    Returns:
        Device data dictionary
    """
    device_manager = DeviceManager()
    return device_manager.load_device_data(device_name, data_type)


def run_lacp_tests_on_device(device_name: str, test_filter: str = None) -> bool:
    """Run LACP tests on a specific device
    
    Args:
        device_name: Name of the device to test
        test_filter: Optional filter to run specific tests (e.g., "bundle", "creation")
        
    Returns:
        True if all tests passed, False otherwise
    """
    device_manager = DeviceManager()
    
    # Verify device exists
    if device_name not in device_manager.list_devices():
        print(f"❌ Device '{device_name}' not found")
        print("Available devices:", device_manager.list_devices())
        return False
    
    # Get device information
    print("=" * 80)
    print(f"🧪 Running LACP Tests on Device: {device_name}")
    print("=" * 80)
    
    device_manager.print_device_summary(device_name)
    
    # Check if device has LACP interfaces
    lacp_interfaces = device_manager.find_lacp_interfaces(device_name)
    if not lacp_interfaces:
        print(f"\n⚠️  Warning: No LACP interfaces found on {device_name}")
        print("Proceeding with tests anyway...")
    else:
        print(f"\n✅ Found {len(lacp_interfaces)} LACP interfaces on {device_name}")
    
    # Get device credentials for test execution
    credentials = device_manager.get_device_credentials(device_name)
    if not credentials:
        print("⚠️  Warning: No credentials found for device")
    else:
        print(f"🔐 Using hostname: {credentials.get('hostname', 'Unknown')}")
    
    print("\n" + "=" * 80)
    print("Starting LACP Test Execution...")
    print("=" * 80)
    
    # Get the current directory (where main.py is located)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Find all Test-Bundle_* directories
    test_dirs = glob.glob(os.path.join(base_dir, "Test-Bundle_*"))
    test_dirs.sort()
    
    # Filter tests if specified
    if test_filter:
        filtered_dirs = []
        for test_dir in test_dirs:
            test_name = os.path.basename(test_dir).lower()
            if test_filter.lower() in test_name:
                filtered_dirs.append(test_dir)
        test_dirs = filtered_dirs
        
        if not test_dirs:
            print(f"❌ No tests found matching filter: {test_filter}")
            return False
        print(f"🔍 Running {len(test_dirs)} tests matching filter '{test_filter}'")
    else:
        print(f"🔍 Running all {len(test_dirs)} LACP tests")
    
    if not test_dirs:
        print("❌ No test directories found!")
        return False
    
    passed_tests = 0
    failed_tests = 0
    device_specific_env = os.environ.copy()
    
    # Set environment variables for the tests to use device information
    device_specific_env['LACP_TEST_DEVICE'] = device_name
    if credentials:
        device_specific_env['LACP_TEST_HOSTNAME'] = credentials.get('hostname', '')
        device_specific_env['LACP_TEST_USERNAME'] = credentials.get('username', '')
        device_specific_env['LACP_TEST_PASSWORD'] = credentials.get('password', '')
    
    # Run each test with device context
    for test_dir in test_dirs:
        test_name = os.path.basename(test_dir)
        main_py_path = os.path.join(test_dir, "main.py")
        
        if not os.path.exists(main_py_path):
            print(f"⚠️  SKIPPED: {test_name} (main.py not found)")
            continue
        
        print(f"\n🔄 Running: {test_name} on {device_name}")
        print("-" * 60)
        
        try:
            # Run the test's main.py file with device environment
            result = subprocess.run([sys.executable, main_py_path], 
                                  capture_output=True, 
                                  text=True, 
                                  timeout=60,  # Increased timeout for device tests
                                  env=device_specific_env)
            
            if result.returncode == 0:
                print(f"✅ PASSED: {test_name}")
                if result.stdout.strip():
                    print(f"   Output: {result.stdout.strip()}")
                passed_tests += 1
            else:
                print(f"❌ FAILED: {test_name} (exit code: {result.returncode})")
                if result.stderr.strip():
                    print(f"   Error: {result.stderr.strip()}")
                if result.stdout.strip():
                    print(f"   Output: {result.stdout.strip()}")
                failed_tests += 1
                
        except subprocess.TimeoutExpired:
            print(f"⏰ TIMEOUT: {test_name} (exceeded 60 seconds)")
            failed_tests += 1
        except Exception as e:
            print(f"💥 ERROR: {test_name} - {str(e)}")
            failed_tests += 1
    
    # Print test summary
    print("\n" + "=" * 80)
    print(f"LACP TEST RESULTS FOR {device_name}")
    print("=" * 80)
    print(f"Total tests: {passed_tests + failed_tests}")
    print(f"✅ Passed: {passed_tests}")
    print(f"❌ Failed: {failed_tests}")
    
    if failed_tests == 0:
        print(f"\n🎉 All LACP tests passed on {device_name}!")
        return True
    else:
        print(f"\n⚠️  {failed_tests} test(s) failed on {device_name}!")
        return False


def interactive_device_selection():
    """Interactive device selection and test execution"""
    device_manager = DeviceManager()
    devices = device_manager.list_devices()
    
    if not devices:
        print("❌ No devices found in Devices directory")
        return
    
    print("\n🎯 LACP Test Device Selection")
    print("=" * 50)
    print("Available devices:")
    
    for i, device in enumerate(devices, 1):
        print(f"  {i}. {device}")
    
    try:
        choice = input(f"\nSelect device (1-{len(devices)}) or 'q' to quit: ").strip()
        
        if choice.lower() == 'q':
            print("👋 Goodbye!")
            return
        
        device_index = int(choice) - 1
        if 0 <= device_index < len(devices):
            selected_device = devices[device_index]
            
            print(f"\n✅ Selected device: {selected_device}")
            
            # Ask for test filter
            test_filter = input("\nEnter test filter (optional, press Enter for all tests): ").strip()
            
            # Run tests on selected device
            success = run_lacp_tests_on_device(selected_device, test_filter if test_filter else None)
            
            if success:
                print(f"\n🎉 All tests completed successfully on {selected_device}!")
            else:
                print(f"\n⚠️  Some tests failed on {selected_device}")
                
        else:
            print("❌ Invalid selection")
            
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
    except KeyboardInterrupt:
        print("\n\n👋 Test execution cancelled by user")
    except Exception as e:
        print(f"❌ Error: {e}")


def run_test_suite():
    """Run all test files in the Test-Bundle_* directories"""
    print("=" * 60)
    print("LACP Regression Test Suite")
    print("=" * 60)
    
    # Get the current directory (where main.py is located)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Find all Test-Bundle_* directories
    test_dirs = glob.glob(os.path.join(base_dir, "Test-Bundle_*"))
    test_dirs.sort()  # Sort alphabetically for consistent execution order
    
    if not test_dirs:
        print("❌ No test directories found!")
        return False
    
    print(f"Found {len(test_dirs)} test directories:")
    for test_dir in test_dirs:
        print(f"  - {os.path.basename(test_dir)}")
    
    print("\n" + "=" * 60)
    print("Starting test execution...")
    print("=" * 60)
    
    passed_tests = 0
    failed_tests = 0
    
    # Run each test
    for test_dir in test_dirs:
        test_name = os.path.basename(test_dir)
        main_py_path = os.path.join(test_dir, "main.py")
        
        if not os.path.exists(main_py_path):
            print(f"⚠️  SKIPPED: {test_name} (main.py not found)")
            continue
        
        print(f"\n🔄 Running: {test_name}")
        print("-" * 40)
        
        try:
            # Run the test's main.py file
            result = subprocess.run([sys.executable, main_py_path], 
                                  capture_output=True, 
                                  text=True, 
                                  timeout=30)
            
            if result.returncode == 0:
                print(f"✅ PASSED: {test_name}")
                if result.stdout.strip():
                    print(f"   Output: {result.stdout.strip()}")
                passed_tests += 1
            else:
                print(f"❌ FAILED: {test_name} (exit code: {result.returncode})")
                if result.stderr.strip():
                    print(f"   Error: {result.stderr.strip()}")
                if result.stdout.strip():
                    print(f"   Output: {result.stdout.strip()}")
                failed_tests += 1
                
        except subprocess.TimeoutExpired:
            print(f"⏰ TIMEOUT: {test_name} (exceeded 30 seconds)")
            failed_tests += 1
        except Exception as e:
            print(f"💥 ERROR: {test_name} - {str(e)}")
            failed_tests += 1
    
    # Print summary
    print("\n" + "=" * 60)
    print("TEST SUITE SUMMARY")
    print("=" * 60)
    print(f"Total tests: {passed_tests + failed_tests}")
    print(f"✅ Passed: {passed_tests}")
    print(f"❌ Failed: {failed_tests}")
    
    if failed_tests == 0:
        print("\n🎉 All tests passed!")
        return True
    else:
        print(f"\n⚠️  {failed_tests} test(s) failed!")
        return False

def main():
    """Main entry point with command line argument handling"""
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "devices":
            # List all available devices
            list_available_devices()
            
        elif command == "device" and len(sys.argv) > 2:
            # Access specific device or run tests on device
            device_name = sys.argv[2]
            action = sys.argv[3].lower() if len(sys.argv) > 3 else 'info'
            
            device_manager = DeviceManager()
            if device_name in device_manager.list_devices():
                
                if action == "test":
                    # Run LACP tests on the specific device
                    test_filter = sys.argv[4] if len(sys.argv) > 4 else None
                    success = run_lacp_tests_on_device(device_name, test_filter)
                    sys.exit(0 if success else 1)
                    
                elif action in ['interfaces', 'lldp', 'system', 'all']:
                    # Load specific data type
                    device_manager.print_device_summary(device_name)
                    print(f"\n🔍 Loading {action} data for {device_name}...")
                    data = device_manager.load_device_data(device_name, action)
                    
                    if data:
                        print(f"✅ Successfully loaded {action} data")
                    else:
                        print(f"❌ No {action} data found")
                        
                else:
                    # Default - show device summary
                    device_manager.print_device_summary(device_name)
                    
            else:
                print(f"❌ Device '{device_name}' not found")
                print("Available devices:", device_manager.list_devices())
                
        elif command == "test":
            if len(sys.argv) > 2:
                device_name = sys.argv[2]
                test_filter = sys.argv[3] if len(sys.argv) > 3 else None
                success = run_lacp_tests_on_device(device_name, test_filter)
                sys.exit(0 if success else 1)
            else:
                # Interactive device selection
                interactive_device_selection()
                
        elif command == "interactive":
            # Interactive device selection and testing
            interactive_device_selection()
            
        elif command == "help":
            print_help()
            
        else:
            print(f"❌ Unknown command: {command}")
            print_help()
            sys.exit(1)
    else:
        # Default behavior - interactive device selection
        interactive_device_selection()


def print_help():
    """Print usage help"""
    print("\n📖 LACP Regression Test Suite - Usage:")
    print("=" * 60)
    print("🎯 DEVICE TESTING:")
    print("python main.py                           - Interactive device selection & testing")
    print("python main.py interactive               - Interactive device selection & testing")
    print("python main.py test                      - Interactive device selection & testing")
    print("python main.py test <device>             - Run all LACP tests on device")
    print("python main.py test <device> <filter>    - Run filtered LACP tests on device")
    print("python main.py device <name> test        - Run all LACP tests on device")
    print("python main.py device <name> test <filter> - Run filtered LACP tests on device")
    print()
    print("📋 DEVICE INFORMATION:")
    print("python main.py devices                   - List all available devices")
    print("python main.py device <name>             - Show device summary")
    print("python main.py device <name> <type>      - Load specific data type")
    print()
    print("❓ HELP:")
    print("python main.py help                      - Show this help")
    print()
    print("📊 Data types: 'interfaces', 'lldp', 'system', 'all'")
    print("🔍 Test filters: 'bundle', 'creation', 'member', 'systemid', etc.")
    print()
    print("💡 Examples:")
    print("  python main.py                          # Interactive mode")
    print("  python main.py devices                  # List all devices")
    print("  python main.py test R1_CL16_Eddie       # Run all tests on R1_CL16_Eddie")
    print("  python main.py test R1_CL16_Eddie bundle # Run bundle tests on R1_CL16_Eddie")
    print("  python main.py device R2_SA40_Eddie test # Run all tests on R2_SA40_Eddie")
    print("  python main.py device R3_SA40_Eddie interfaces # Show interfaces")
    print()
    print("🌟 Environment Variables (set automatically for tests):")
    print("  LACP_TEST_DEVICE   - Current device name")
    print("  LACP_TEST_HOSTNAME - Device hostname")
    print("  LACP_TEST_USERNAME - Device username") 
    print("  LACP_TEST_PASSWORD - Device password")


if __name__ == "__main__":
    main()
