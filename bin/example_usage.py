#!/usr/bin/env python3
"""
Example usage of config_helpers module.

This script demonstrates practical use cases for the configuration
file parsing helpers in real-world scenarios.
"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))

from config_helpers import ConfigParser, parse_configuration_file, compare_configurations


def example_1_check_version():
    """Example: Check configuration version."""
    print("\n" + "=" * 60)
    print("Example 1: Check Configuration Version")
    print("=" * 60)
    
    config_file = Path('../config/default/Configuration.h')
    parser = ConfigParser(config_file)
    
    version = parser.get_version()
    print(f"\nConfiguration version: {version}")
    
    # Check if it's a specific version
    if version and version.startswith('2.1'):
        print("✓ This is a Marlin 2.1.x configuration")
    else:
        print("⚠️  This is not a Marlin 2.1.x configuration")


def example_2_extract_printer_settings():
    """Example: Extract key printer settings."""
    print("\n" + "=" * 60)
    print("Example 2: Extract Key Printer Settings")
    print("=" * 60)
    
    config_file = Path('../config/default/Configuration.h')
    parser = ConfigParser(config_file)
    
    # Define the settings we want to extract
    key_settings = {
        'EXTRUDERS': 'Number of extruders',
        'MOTHERBOARD': 'Motherboard type',
        'X_DRIVER_TYPE': 'X axis driver',
        'Y_DRIVER_TYPE': 'Y axis driver',
        'Z_DRIVER_TYPE': 'Z axis driver',
        'BAUDRATE': 'Serial baudrate',
        'TEMP_SENSOR_0': 'Hotend sensor',
        'TEMP_SENSOR_BED': 'Bed sensor',
        'DEFAULT_NOMINAL_FILAMENT_DIA': 'Filament diameter',
    }
    
    print("\nKey Printer Settings:")
    print("-" * 40)
    
    for setting, description in key_settings.items():
        value = parser.get_define(setting)
        if value:
            print(f"{description:25s}: {value}")
        else:
            print(f"{description:25s}: Not defined")


def example_3_check_enabled_features():
    """Example: Check which features are enabled."""
    print("\n" + "=" * 60)
    print("Example 3: Check Enabled Features")
    print("=" * 60)
    
    config_file = Path('../config/default/Configuration.h')
    parser = ConfigParser(config_file)
    
    enabled = parser.get_enabled_features()
    
    # Features we're interested in
    interesting_features = [
        'PREVENT_COLD_EXTRUSION',
        'PREVENT_LENGTHY_EXTRUDE',
        'THERMAL_PROTECTION_HOTENDS',
        'THERMAL_PROTECTION_BED',
        'HOMING_Z_FIRST',
        'Z_SAFE_HOMING',
        'AUTO_BED_LEVELING_BILINEAR',
        'AUTO_BED_LEVELING_UBL',
        'BLTOUCH',
    ]
    
    print("\nFeature Status:")
    print("-" * 40)
    
    for feature in interesting_features:
        status = "✓ Enabled" if feature in enabled else "✗ Disabled"
        print(f"{feature:35s}: {status}")


def example_4_check_for_errors():
    """Example: Check for error directives in config."""
    print("\n" + "=" * 60)
    print("Example 4: Check for Configuration Errors")
    print("=" * 60)
    
    config_file = Path('../config/default/Configuration.h')
    parser = ConfigParser(config_file)
    
    if parser.has_error_directive():
        print("\n⚠️  WARNING: Configuration file contains #error directives!\n")
        
        errors = parser.get_error_messages()
        for i, error in enumerate(errors, 1):
            print(f"  Error {i}: {error}")
        
        print("\n  These errors must be resolved before building!")
    else:
        print("\n✓ No #error directives found in configuration file")


def example_5_compare_configs():
    """Example: Compare two configuration files."""
    print("\n" + "=" * 60)
    print("Example 5: Compare Configuration Files")
    print("=" * 60)
    
    file1 = Path('../config/default/Configuration.h')
    file2 = Path('../config/default/Configuration_adv.h')
    
    print(f"\nComparing:")
    print(f"  File 1: {file1.name}")
    print(f"  File 2: {file2.name}")
    
    diff = compare_configurations(file1, file2)
    
    print(f"\nComparison Results:")
    print(f"  Settings only in {file1.name}: {len(diff['only_in_file1'])}")
    print(f"  Settings only in {file2.name}: {len(diff['only_in_file2'])}")
    print(f"  Settings with different values: {len(diff['different_values'])}")
    
    # Show some examples of settings only in each file
    if diff['only_in_file1']:
        print(f"\n  Examples only in {file1.name}:")
        for key in list(diff['only_in_file1'].keys())[:5]:
            print(f"    - {key}")
    
    if diff['only_in_file2']:
        print(f"\n  Examples only in {file2.name}:")
        for key in list(diff['only_in_file2'].keys())[:5]:
            print(f"    - {key}")


def example_6_get_setting_with_comment():
    """Example: Get a setting with its comment."""
    print("\n" + "=" * 60)
    print("Example 6: Get Setting with Comment")
    print("=" * 60)
    
    config_file = Path('../config/default/Configuration.h')
    parser = ConfigParser(config_file)
    
    settings_to_check = ['EXTRUDERS', 'BAUDRATE', 'MOTHERBOARD']
    
    print("\nSettings with Comments:")
    print("-" * 40)
    
    for setting in settings_to_check:
        value = parser.get_define(setting)
        comment = parser.get_comments_for_define(setting)
        
        print(f"\n  {setting} = {value}")
        if comment:
            print(f"    Comment: {comment}")


def example_7_batch_parse():
    """Example: Parse multiple configuration files."""
    print("\n" + "=" * 60)
    print("Example 7: Batch Parse Configuration Files")
    print("=" * 60)
    
    config_files = [
        Path('../config/default/Configuration.h'),
        Path('../config/default/Configuration_adv.h'),
    ]
    
    print("\nParsing multiple files:")
    print("-" * 40)
    
    for config_file in config_files:
        if config_file.exists():
            data = parse_configuration_file(config_file)
            
            print(f"\n  {data['filename']}:")
            print(f"    Version: {data['version']}")
            print(f"    Total defines: {len(data['defines'])}")
            print(f"    Enabled features: {len(data['enabled_features'])}")
            print(f"    Has errors: {data['has_errors']}")
        else:
            print(f"\n  {config_file.name}: File not found")


def main():
    """Run all examples."""
    print("\n" + "=" * 60)
    print("Configuration Helpers - Example Usage")
    print("=" * 60)
    
    examples = [
        example_1_check_version,
        example_2_extract_printer_settings,
        example_3_check_enabled_features,
        example_4_check_for_errors,
        example_5_compare_configs,
        example_6_get_setting_with_comment,
        example_7_batch_parse,
    ]
    
    for example in examples:
        try:
            example()
        except Exception as e:
            print(f"\n❌ Error in {example.__name__}: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "=" * 60)
    print("All examples completed!")
    print("=" * 60 + "\n")


if __name__ == '__main__':
    main()
