# 🔧 JSON Analyzer CLI

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-production--ready-brightgreen.svg)

Advanced CLI tool for JSON file analysis, validation, and manipulation with deep structural insights.

## ✨ Features

- ✅ **Deep Structural Analysis** - Recursively analyze JSON structure with detailed statistics
- 🔍 **Duplicate Detection** - Find duplicate values in arrays at any nesting level
- 🔐 **Schema Validation** - Validate JSON against required keys
- 📊 **Type Distribution** - Get comprehensive type statistics
- 🎨 **Pretty Printing** - Format JSON with clean, readable output
- ⚡ **Performance** - Efficiently handles files up to 100MB
- 🛡️ **Error Handling** - Detailed error messages for JSON syntax issues

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/Timmyae/json-analyzer-cli.git
cd json-analyzer-cli

# Make executable
chmod +x json_analyzer.py
```

### Basic Usage

```bash
# Analyze JSON file
./json_analyzer.py data.json --analyze

# Pretty print
./json_analyzer.py config.json --pretty

# Validate schema
./json_analyzer.py api_config.json --validate "api_key,endpoint,version"

# Find duplicates
./json_analyzer.py large_data.json --duplicates

# Combine multiple operations
./json_analyzer.py file.json -a -p -d
```

## 📖 Command Reference

```
usage: json_analyzer.py [-h] [-a] [-p] [-v KEYS] [-d] file

🔧 Advanced JSON Analyzer & Validator

positional arguments:
  file                  Path to JSON file

options:
  -h, --help            show this help message and exit
  -a, --analyze         Generate full analysis report
  -p, --pretty          Pretty-print formatted JSON
  -v KEYS, --validate KEYS
                        Validate required keys (comma-separated)
  -d, --duplicates      Find duplicate values in arrays
```

## 📊 Example Output

### Analysis Report
```
🔍 JSON Analysis Report ========================================
📁 File: config.json
📏 Size: 2.45 KB
📅 Modified: 2025-01-22 15:30:00

─────────────────── Structure Analysis ────────────────────────
├─ Root Type: dict
├─ Max Depth: 4 levels
├─ Total Keys: 23
├─ Objects: 5
├─ Arrays: 3
└─ Null Values: 1

──────────────────── Type Distribution ────────────────────────
  • str: 15
  • int: 8
  • bool: 3
  • array: 2

✅ No duplicates detected
================================================================
```

### Schema Validation
```
🔐 Schema Validation ==========================================
Status: ✅ VALID
Found: api_key, version, endpoint
===============================================================
```

## 🔍 Use Cases

- **API Configuration Validation** - Ensure all required keys exist
- **Data Quality Checks** - Find duplicates and inconsistencies  
- **JSON Structure Documentation** - Generate reports for data schemas
- **Debug Complex JSON** - Analyze deeply nested structures
- **Pre-deployment Validation** - Verify config files before production

## 🧪 Testing

Create a test JSON file:

```bash
echo '{"name": "Test", "items": [1, 2, 2, 3]}' > test.json
./json_analyzer.py test.json --duplicates
```

Expected output:
```
🔎 Found 1 duplicate entries
  • root.items: 2
```

## 🛠️ Requirements

- Python 3.7 or higher
- No external dependencies (uses only standard library)

## 📝 License

MIT License - see LICENSE file for details

## 🤝 Contributing

Contributions welcome! Feel free to:
- Report bugs via Issues
- Submit feature requests
- Create pull requests

## 💡 Tips

- Use `--analyze` for comprehensive insights
- Combine `-a -p -v` for full validation workflow  
- Process large files efficiently (tested up to 100MB)
- JSON syntax errors show exact line and column numbers

## 🔗 Links

- **Repository**: https://github.com/Timmyae/json-analyzer-cli
- **Issues**: https://github.com/Timmyae/json-analyzer-cli/issues

---

**Made with ❤️ for JSON developers**
