# Configuration File Helpers

Helper functions to extract and manipulate data from Marlin configuration files (Configuration.h and Configuration_adv.h).

These utilities provide a reliable way to parse and extract settings from Marlin firmware configuration files, avoiding the need for fragile text parsing or manual inspection.

## Files

- `config_helpers.py` - Main helper module with configuration parsing utilities
- `test_config_helpers.py` - Test suite demonstrating usage of the helpers
- `mfconfig` - Main configuration management script (uses config_helpers)

## Usage

### Basic Example

```python
from pathlib import Path
from config_helpers import ConfigParser, parse_configuration_file

# Parse a configuration file
config_file = Path('path/to/Configuration.h')
parser = ConfigParser(config_file)

# Get version
version = parser.get_version()
print(f"Version: {version}")

# Get specific setting
extruders = parser.get_define('EXTRUDERS')
print(f"Extruders: {extruders}")

# Get all defines
defines = parser.get_defines()
print(f"Total defines: {len(defines)}")
```

### Parse Full Configuration

```python
from config_helpers import parse_configuration_file

data = parse_configuration_file(config_file)

print(f"Version: {data['version']}")
print(f"Total defines: {len(data['defines'])}")
print(f"Enabled features: {len(data['enabled_features'])}")
print(f"Has errors: {data['has_errors']}")
```

### Compare Two Configuration Files

```python
from pathlib import Path
from config_helpers import compare_configurations

file1 = Path('config1/Configuration.h')
file2 = Path('config2/Configuration.h')

diff = compare_configurations(file1, file2)

print(f"Settings only in file1: {len(diff['only_in_file1'])}")
print(f"Settings only in file2: {len(diff['only_in_file2'])}")
print(f"Different values: {len(diff['different_values'])}")

for key, (val1, val2) in diff['different_values'].items():
    print(f"{key}: '{val1}' != '{val2}'")
```

### Extract Settings by Category

```python
from config_helpers import extract_settings_by_category

categories = extract_settings_by_category(config_file)

for category, settings in categories.items():
    if settings:
        print(f"{category}: {len(settings)} settings")
        for key, value in list(settings.items())[:5]:
            print(f"  {key} = {value}")
```

### Feature Detection

```python
from config_helpers import ConfigParser

parser = ConfigParser(config_file)

# Get enabled features
enabled = parser.get_enabled_features()
print(f"Enabled: {enabled}")

# Get disabled features
disabled = parser.get_disabled_features()
print(f"Disabled: {disabled}")

# Check for error directives
if parser.has_error_directive():
    errors = parser.get_error_messages()
    for msg in errors:
        print(f"Error: {msg}")
```

## API Reference

### ConfigParser Class

Main class for parsing configuration files.

#### Methods

- `__init__(filepath: Path)` - Initialize parser with configuration file
- `get_defines() -> Dict[str, str]` - Extract all #define directives
- `get_define(name: str, default: Optional[str] = None) -> Optional[str]` - Get value of specific define
- `get_version() -> Optional[str]` - Get configuration version
- `find_section(section_name: str) -> Optional[Tuple[int, int]]` - Find line range of a section
- `get_enabled_features() -> List[str]` - Get list of enabled features
- `get_disabled_features() -> List[str]` - Get list of disabled features
- `has_error_directive() -> bool` - Check if file contains #error directives
- `get_error_messages() -> List[str]` - Extract all #error messages
- `get_comments_for_define(name: str) -> Optional[str]` - Get comment for a define

### Helper Functions

- `parse_configuration_file(filepath: Path) -> Dict[str, Any]` - Parse file and extract key information
- `compare_configurations(file1: Path, file2: Path) -> Dict[str, Any]` - Compare two configuration files
- `extract_settings_by_category(filepath: Path) -> Dict[str, Dict[str, str]]` - Extract settings grouped by category

## Integration with mfconfig

The `mfconfig` script uses `config_helpers` for robust parsing of configuration files:

```python
try:
    from config_helpers import ConfigParser, parse_configuration_file
except ImportError:
    ConfigParser = None

# Use ConfigParser if available
if ConfigParser:
    parser = ConfigParser(config_file)
    defines = parser.get_defines()
    # ... process configuration
```

## Benefits

1. **Reliability**: Proper parsing instead of fragile text manipulation
2. **Type Safety**: Clear return types and error handling
3. **Reusability**: Common functionality extracted into reusable functions
4. **Testability**: Easy to write unit tests for parsing logic
5. **Maintainability**: Centralized parsing logic that can be updated in one place

## Testing

Run the test suite:

```bash
cd bin
python3 test_config_helpers.py
```

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## License

Same as the Marlin Firmware Configurations repository (GPLv3)
