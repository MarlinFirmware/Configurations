#!/usr/bin/env python3
"""
Configuration File Helpers

Helper functions to extract and manipulate data from Marlin configuration files
(Configuration.h and Configuration_adv.h).

These utilities provide a reliable way to parse and extract settings from
Marlin firmware configuration files, avoiding the need for fragile text
parsing or manual inspection.
"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any


class ConfigParser:
    """Parser for Marlin configuration files."""

    def __init__(self, filepath: Path):
        """Initialize parser with a configuration file.
        
        Args:
            filepath: Path to the configuration file (Configuration.h or Configuration_adv.h)
        """
        self.filepath = Path(filepath)
        self._content = None
        self._lines = None

    def _read_file(self) -> str:
        """Read and cache file content."""
        if self._content is None:
            with open(self.filepath, 'r') as f:
                self._content = f.read()
        return self._content

    def _read_lines(self) -> List[str]:
        """Read and cache file lines."""
        if self._lines is None:
            with open(self.filepath, 'r') as f:
                self._lines = f.readlines()
        return self._lines

    def get_defines(self) -> Dict[str, str]:
        """Extract all #define directives from the file.
        
        Returns:
            Dictionary mapping define names to their values (as strings).
        """
        content = self._read_file()
        defines = {}
        
        # Match #define NAME value (with optional comments)
        # Handles both simple values and complex expressions
        pattern = r'^\s*#define\s+(\w+)\s+(.+?)(?:\s*//.*)?$'
        
        for match in re.finditer(pattern, content, re.MULTILINE):
            name = match.group(1)
            value = match.group(2).strip()
            defines[name] = value
        
        return defines

    def get_define(self, name: str, default: Optional[str] = None) -> Optional[str]:
        """Get the value of a specific #define.
        
        Args:
            name: The name of the define to look up.
            default: Default value to return if not found.
            
        Returns:
            The value of the define, or default if not found.
        """
        defines = self.get_defines()
        return defines.get(name, default)

    def get_version(self) -> Optional[str]:
        """Get the configuration version from CONFIGURATION_H_VERSION.
        
        Returns:
            Version string, or None if not found.
        """
        version = self.get_define('CONFIGURATION_H_VERSION')
        if version:
            # Format: 02010300 -> 2.1.3.0
            if version.isdigit() and len(version) >= 8:
                major = int(version[0:2])
                minor = int(version[2:4])
                patch = int(version[4:6])
                sub = int(version[6:8])
                return f"{major}.{minor}.{patch}.{sub}"
        return version

    def find_section(self, section_name: str) -> Optional[Tuple[int, int]]:
        """Find the line range of a configuration section.
        
        Args:
            section_name: Name of the section to find (e.g., "Axis Settings").
            
        Returns:
            Tuple of (start_line, end_line) or None if not found.
        """
        lines = self._read_lines()
        start = None
        
        for i, line in enumerate(lines):
            # Look for section headers (comment lines with ===)
            if section_name in line and '===' in line:
                start = i
                break
        
        if start is None:
            return None
        
        # Find the end of the section (next section or end of file)
        for i in range(start + 1, len(lines)):
            line = lines[i]
            # Check if this is a new section header
            if re.match(r'^\s*//\s*-+', line) and '===' in line:
                return (start, i)
        
        return (start, len(lines))

    def get_enabled_features(self) -> List[str]:
        """Get a list of enabled features (defines set to true/1).
        
        Returns:
            List of feature names that are enabled.
        """
        defines = self.get_defines()
        enabled = []
        
        for name, value in defines.items():
            # Check if value is true, 1, or similar
            if value.upper() in ('1', 'TRUE', 'YES', 'ON', 'ENABLED'):
                enabled.append(name)
            # Also check for defines without explicit values (just #define NAME)
            elif value == '':
                enabled.append(name)
        
        return enabled

    def get_disabled_features(self) -> List[str]:
        """Get a list of disabled features (defines set to false/0).
        
        Returns:
            List of feature names that are disabled.
        """
        defines = self.get_defines()
        disabled = []
        
        for name, value in defines.items():
            if value.upper() in ('0', 'FALSE', 'NO', 'OFF', 'DISABLED'):
                disabled.append(name)
        
        return disabled

    def has_error_directive(self) -> bool:
        """Check if the file contains #error directives.
        
        Returns:
            True if #error directives are present.
        """
        content = self._read_file()
        return bool(re.search(r'^\s*#error', content, re.MULTILINE))

    def get_error_messages(self) -> List[str]:
        """Extract all #error messages from the file.
        
        Returns:
            List of error message strings.
        """
        content = self._read_file()
        errors = []
        
        for match in re.finditer(r'^\s*#error\s+(.+?)$', content, re.MULTILINE):
            errors.append(match.group(1).strip())
        
        return errors

    def get_comments_for_define(self, name: str) -> Optional[str]:
        """Get the comment associated with a specific #define.
        
        Args:
            name: The name of the define.
            
        Returns:
            The comment text, or None if not found.
        """
        lines = self._read_lines()
        
        for i, line in enumerate(lines):
            if re.match(rf'^\s*#define\s+{name}\b', line):
                # Check for inline comment
                inline_match = re.search(r'//(.+)$', line)
                if inline_match:
                    return inline_match.group(1).strip()
                
                # Check previous lines for comments
                for j in range(i - 1, max(-1, i - 5), -1):
                    prev_line = lines[j].strip()
                    if prev_line.startswith('//'):
                        return prev_line[2:].strip()
                    elif prev_line and not prev_line.startswith('*'):
                        break
        
        return None


def parse_configuration_file(filepath: Path) -> Dict[str, Any]:
    """Parse a Marlin configuration file and extract key information.
    
    Args:
        filepath: Path to the configuration file.
        
    Returns:
        Dictionary containing parsed configuration data.
    """
    # Ensure filepath is a Path object
    filepath = Path(filepath)
    parser = ConfigParser(filepath)
    
    return {
        'filepath': str(filepath),
        'filename': filepath.name,
        'version': parser.get_version(),
        'defines': parser.get_defines(),
        'enabled_features': parser.get_enabled_features(),
        'disabled_features': parser.get_disabled_features(),
        'has_errors': parser.has_error_directive(),
        'error_messages': parser.get_error_messages(),
    }


def compare_configurations(file1: Path, file2: Path) -> Dict[str, Any]:
    """Compare two configuration files and identify differences.
    
    Args:
        file1: Path to first configuration file.
        file2: Path to second configuration file.
        
    Returns:
        Dictionary containing the differences.
    """
    # Ensure file paths are Path objects
    file1 = Path(file1)
    file2 = Path(file2)
    parser1 = ConfigParser(file1)
    parser2 = ConfigParser(file2)
    
    defines1 = parser1.get_defines()
    defines2 = parser2.get_defines()
    
    # Find differences
    only_in_file1 = {k: v for k, v in defines1.items() if k not in defines2}
    only_in_file2 = {k: v for k, v in defines2.items() if k not in defines1}
    
    different_values = {
        k: (defines1[k], defines2[k])
        for k in defines1.keys() & defines2.keys()
        if defines1[k] != defines2[k]
    }
    
    return {
        'file1': str(file1),
        'file2': str(file2),
        'only_in_file1': only_in_file1,
        'only_in_file2': only_in_file2,
        'different_values': different_values,
        'file1_version': parser1.get_version(),
        'file2_version': parser2.get_version(),
    }


def extract_settings_by_category(filepath: Path) -> Dict[str, Dict[str, str]]:
    """Extract settings grouped by configuration category.
    
    Attempts to group defines based on section headers in the file.
    
    Args:
        filepath: Path to the configuration file.
        
    Returns:
        Dictionary mapping section names to their defines.
    """
    # Ensure filepath is a Path object
    filepath = Path(filepath)
    parser = ConfigParser(filepath)
    lines = parser._read_lines()
    
    categories = {}
    current_category = 'Uncategorized'
    categories[current_category] = {}
    
    for i, line in enumerate(lines):
        # Check for section headers (lines with === or ---)
        if re.match(r'^\s*//\s*[=-]{3,}', line):
            # Look for category name in nearby lines
            for j in range(max(0, i - 3), min(len(lines), i + 2)):
                if j != i and lines[j].strip().startswith('//'):
                    cat_name = lines[j].strip()[2:].strip()
                    if cat_name and not cat_name.startswith('===') and not cat_name.startswith('---'):
                        current_category = cat_name
                        if current_category not in categories:
                            categories[current_category] = {}
                        break
        
        # Check for #define directives
        define_match = re.match(r'^\s*#define\s+(\w+)\s+(.+?)(?:\s*//.*)?$', line)
        if define_match:
            name = define_match.group(1)
            value = define_match.group(2).strip()
            categories[current_category][name] = value
    
    return categories


if __name__ == '__main__':
    # Example usage
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: config_helpers.py <config_file> [config_file2]")
        sys.exit(1)
    
    config_file = Path(sys.argv[1])
    
    if not config_file.exists():
        print(f"Error: File '{config_file}' not found")
        sys.exit(1)
    
    print(f"\n=== Parsing {config_file} ===\n")
    
    data = parse_configuration_file(config_file)
    
    print(f"Version: {data['version']}")
    print(f"Total defines: {len(data['defines'])}")
    print(f"Enabled features: {len(data['enabled_features'])}")
    print(f"Has errors: {data['has_errors']}")
    
    if data['error_messages']:
        print(f"\nError messages:")
        for msg in data['error_messages']:
            print(f"  - {msg}")
    
    # Show some key settings
    key_settings = [
        'EXTRUDERS', 'X_DRIVER_TYPE', 'Y_DRIVER_TYPE', 'Z_DRIVER_TYPE',
        'BAUDRATE', 'SERIAL_PORT', 'TEMP_SENSOR_0', 'TEMP_SENSOR_BED'
    ]
    
    print(f"\nKey settings:")
    for key in key_settings:
        if key in data['defines']:
            print(f"  {key} = {data['defines'][key]}")
    
    # If a second file is provided, compare them
    if len(sys.argv) > 2:
        config_file2 = Path(sys.argv[2])
        if config_file2.exists():
            print(f"\n\n=== Comparing with {config_file2} ===\n")
            
            diff = compare_configurations(config_file, config_file2)
            
            print(f"Different values: {len(diff['different_values'])}")
            for key, (val1, val2) in diff['different_values'].items():
                print(f"  {key}: '{val1}' != '{val2}'")
    
    print()
