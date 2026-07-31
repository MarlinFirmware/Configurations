# Configuration File Helpers

## Overview

Scripts here provide robust helpers to extract data from Marlin configuration files (Configuration.h and Configuration_adv.h).

## The Problem

The MarlinFirmware/Configurations repository uses the `mfconfig` script to manage configuration files. Previously, parsing and extracting data from these files required:
- Manual text parsing with regex
- No type safety or error handling
- Duplicated code across different scripts
- Fragile parsing logic that breaks with file format changes

## The Solution

Comprehensive Python module (`config_helpers.py`) providing:

1. **ConfigParser Class** - Object-oriented parser for configuration files
2. **Helper Functions** - High-level functions for common tasks
3. **Type Hints** - Clear API with proper type annotations
4. **Error Handling** - Robust error handling and fallbacks
5. **Test Suite** - Comprehensive tests demonstrating usage

## Files

### 1. `config_helpers.py`
Main helper module containing:

- **ConfigParser class** with methods:
  - `get_defines()` - Extract all #define directives
  - `get_define(name)` - Get specific define value
  - `get_version()` - Parse configuration version
  - `find_section(section_name)` - Locate section in file
  - `get_enabled_features()` - List enabled features
  - `get_disabled_features()` - List disabled features
  - `has_error_directive()` - Check for #error directives
  - `get_error_messages()` - Extract error messages
  - `get_comments_for_define(name)` - Get associated comments

- **Helper functions**:
  - `parse_configuration_file(filepath)` - Parse and extract key info
  - `compare_configurations(file1, file2)` - Compare two configs
  - `extract_settings_by_category(filepath)` - Group settings by category

### 2. `test_config_helpers.py`
Comprehensive test suite demonstrating:
- Basic parsing
- Feature detection
- Category extraction
- File comparison
- Advanced parsing

### 3. `example_usage.py`
Practical examples showing:
- Checking configuration version
- Extracting printer settings
- Checking enabled features
- Error detection
- File comparison
- Batch parsing

### 4. `README_CONFIG_HELPERS.md`
Complete documentation including:
- Usage examples
- API reference
- Integration guide
- Benefits and requirements

## Integration with Existing Code

### Updated `mfconfig` Script

The `mfconfig` script has been updated to use the new helpers:

```python
try:
    from config_helpers import ConfigParser, parse_configuration_file
except ImportError:
    ConfigParser = None

# Use ConfigParser if available
if ConfigParser:
    parser = ConfigParser(config_file)
    defines = parser.get_defines()
    # More robust parsing with error handling
```

The `add_path_labels()` function now uses `ConfigParser` for more reliable parsing with fallback to the original method if needed.

## Usage Examples

### Basic Parsing
```python
from config_helpers import ConfigParser

parser = ConfigParser('Configuration.h')
version = parser.get_version()
extruders = parser.get_define('EXTRUDERS')
```

### Feature Detection
```python
enabled = parser.get_enabled_features()
disabled = parser.get_disabled_features()
```

### File Comparison
```python
from config_helpers import compare_configurations

diff = compare_configurations('config1.h', 'config2.h')
print(f"Different values: {len(diff['different_values'])}")
```

### Batch Processing
```python
from config_helpers import parse_configuration_file

for config_file in config_files:
    data = parse_configuration_file(config_file)
    print(f"{data['filename']}: {len(data['defines'])} defines")
```

## Testing

Run the test suite:
```bash
cd bin
python3 test_config_helpers.py
```

Run the example usage:
```bash
cd bin
python3 example_usage.py
```
