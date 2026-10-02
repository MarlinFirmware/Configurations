#!/usr/bin/env python3
"""
Test script for config_helpers module.

Demonstrates various ways to use the configuration file parsing helpers.
"""

from pathlib import Path
import sys

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from config_helpers import (
    ConfigParser,
    parse_configuration_file,
    compare_configurations,
    extract_settings_by_category
)


def test_basic_parsing():
    """Test basic configuration file parsing."""
    print("=" * 60)
    print("TEST 1: Basic Parsing")
    print("=" * 60)
    
    config_file = Path('../config/default/Configuration.h')
    parser = ConfigParser(config_file)
    
    # Get version
    version = parser.get_version()
    print(f"\nConfiguration Version: {version}")
    
    # Get specific defines
    extruders = parser.get_define('EXTRUDERS')
    print(f"Number of Extruders: {extruders}")
    
    baudrate = parser.get_define('BAUDRATE')
    print(f"Baudrate: {baudrate}")
    
    # Get all defines
    defines = parser.get_defines()
    print(f"\nTotal #define directives: {len(defines)}")
    
    # Check for errors
    if parser.has_error_directive():
        print("\n⚠️  Warning: File contains #error directives!")
        for msg in parser.get_error_messages():
            print(f"  - {msg}")
    
    print()


def test_feature_detection():
    """Test detection of enabled/disabled features."""
    print("=" * 60)
    print("TEST 2: Feature Detection")
    print("=" * 60)
    
    config_file = Path('../config/default/Configuration.h')
    parser = ConfigParser(config_file)
    
    enabled = parser.get_enabled_features()
    disabled = parser.get_disabled_features()
    
    print(f"\nEnabled features ({len(enabled)}):")
    for feature in sorted(enabled)[:10]:  # Show first 10
        print(f"  - {feature}")
    if len(enabled) > 10:
        print(f"  ... and {len(enabled) - 10} more")
    
    print(f"\nDisabled features ({len(disabled)}):")
    for feature in sorted(disabled)[:10]:  # Show first 10
        print(f"  - {feature}")
    if len(disabled) > 10:
        print(f"  ... and {len(disabled) - 10} more")
    
    print()


def test_category_extraction():
    """Test extraction of settings by category."""
    print("=" * 60)
    print("TEST 3: Category Extraction")
    print("=" * 60)
    
    config_file = Path('../config/default/Configuration.h')
    categories = extract_settings_by_category(config_file)
    
    print(f"\nFound {len(categories)} categories:\n")
    
    for category, settings in sorted(categories.items()):
        if settings:  # Only show categories with settings
            print(f"  {category}: {len(settings)} settings")
            # Show a few examples
            for key, value in list(settings.items())[:3]:
                print(f"    {key} = {value}")
            if len(settings) > 3:
                print(f"    ... and {len(settings) - 3} more")
            print()


def test_file_comparison():
    """Test comparison of two configuration files."""
    print("=" * 60)
    print("TEST 4: File Comparison")
    print("=" * 60)
    
    file1 = Path('../config/default/Configuration.h')
    file2 = Path('../config/default/Configuration_adv.h')
    
    diff = compare_configurations(file1, file2)
    
    print(f"\nFile 1: {diff['file1']}")
    print(f"  Version: {diff['file1_version']}")
    print(f"\nFile 2: {diff['file2']}")
    print(f"  Version: {diff['file2_version']}")
    
    print(f"\nSettings only in {file1.name}: {len(diff['only_in_file1'])}")
    print(f"Settings only in {file2.name}: {len(diff['only_in_file2'])}")
    print(f"Settings with different values: {len(diff['different_values'])}")
    
    if diff['different_values']:
        print("\nDifferent settings:")
        for key, (val1, val2) in list(diff['different_values'].items())[:10]:
            print(f"  {key}:")
            print(f"    {file1.name}: {val1}")
            print(f"    {file2.name}: {val2}")
        if len(diff['different_values']) > 10:
            print(f"  ... and {len(diff['different_values']) - 10} more")
    
    print()


def test_advanced_parsing():
    """Test advanced parsing features."""
    print("=" * 60)
    print("TEST 5: Advanced Parsing")
    print("=" * 60)
    
    config_file = Path('../config/default/Configuration.h')
    parser = ConfigParser(config_file)
    
    # Get comment for a specific define
    comment = parser.get_comments_for_define('EXTRUDERS')
    print(f"\nComment for EXTRUDERS: {comment}")
    
    # Find a specific section
    section = parser.find_section('Axis Settings')
    if section:
        start, end = section
        print(f"\n'Axis Settings' section found at lines {start}-{end}")
    
    # Parse full configuration
    print("\nParsing full configuration...")
    data = parse_configuration_file(config_file)
    
    print(f"  File: {data['filename']}")
    print(f"  Version: {data['version']}")
    print(f"  Total defines: {len(data['defines'])}")
    print(f"  Enabled features: {len(data['enabled_features'])}")
    print(f"  Disabled features: {len(data['disabled_features'])}")
    print(f"  Has errors: {data['has_errors']}")
    
    print()


def main():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("Configuration Helpers Test Suite")
    print("=" * 60 + "\n")
    
    try:
        test_basic_parsing()
        test_feature_detection()
        test_category_extraction()
        test_file_comparison()
        test_advanced_parsing()
        
        print("=" * 60)
        print("All tests completed successfully! ✓")
        print("=" * 60 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error during tests: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
