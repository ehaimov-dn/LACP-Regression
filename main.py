#!/usr/bin/env python3
"""
LACP Regression Test Suite Runner
Runs all test cases in sequence to validate LACP functionality.
"""

import os
import sys
import subprocess
import glob

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

if __name__ == "__main__":
    success = run_test_suite()
    sys.exit(0 if success else 1)
