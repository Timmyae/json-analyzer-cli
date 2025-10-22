#!/usr/bin/env python3
"""
JSON Analyzer & Validator CLI Tool
A production-ready tool for deep JSON file analysis, validation, and manipulation.
"""

import json
import sys
import argparse
from pathlib import Path
from typing import Any, Dict, List, Union
from collections import Counter
from datetime import datetime


class JSONAnalyzer:
    """Advanced JSON analysis and validation engine."""
    
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.data: Any = None
        self.stats: Dict[str, Any] = {}
        
    def load(self) -> bool:
        """Load and parse JSON file with error handling."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
            return True
        except json.JSONDecodeError as e:
            print(f"❌ JSON Syntax Error at line {e.lineno}, col {e.colno}: {e.msg}")
            return False
        except FileNotFoundError:
            print(f"❌ File not found: {self.file_path}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error: {str(e)}")
            return False
    
    def analyze_structure(self) -> Dict[str, Any]:
        """Deep structural analysis of JSON data."""
        def recursive_analyze(obj, depth=0, max_depth=0):
            stats = {
                'type_counts': Counter(),
                'max_depth': max_depth,
                'total_keys': 0,
                'null_values': 0,
                'arrays': 0,
                'objects': 0
            }
            
            if isinstance(obj, dict):
                stats['objects'] += 1
                stats['total_keys'] += len(obj)
                for key, value in obj.items():
                    if value is None:
                        stats['null_values'] += 1
                    child_stats = recursive_analyze(value, depth + 1, max(max_depth, depth + 1))
                    for k, v in child_stats.items():
                        if k == 'type_counts':
                            stats[k].update(v)
                        elif k in ['total_keys', 'null_values', 'arrays', 'objects']:
                            stats[k] += v
                        elif k == 'max_depth':
                            stats[k] = max(stats[k], v)
                            
            elif isinstance(obj, list):
                stats['arrays'] += 1
                stats['type_counts']['array'] += 1
                for item in obj:
                    child_stats = recursive_analyze(item, depth + 1, max(max_depth, depth + 1))
                    for k, v in child_stats.items():
                        if k == 'type_counts':
                            stats[k].update(v)
                        elif k in ['total_keys', 'null_values', 'arrays', 'objects']:
                            stats[k] += v
                        elif k == 'max_depth':
                            stats[k] = max(stats[k], v)
            else:
                stats['type_counts'][type(obj).__name__] += 1
                
            return stats
        
        self.stats = recursive_analyze(self.data)
        return self.stats
    
    def validate_schema(self, required_keys: List[str]) -> Dict[str, Any]:
        """Validate JSON against required keys."""
        results = {
            'valid': True,
            'missing_keys': [],
            'found_keys': []
        }
        
        if not isinstance(self.data, dict):
            results['valid'] = False
            results['error'] = "Root must be an object for schema validation"
            return results
        
        for key in required_keys:
            if key in self.data:
                results['found_keys'].append(key)
            else:
                results['missing_keys'].append(key)
                results['valid'] = False
        
        return results
    
    def find_duplicates(self) -> List[Dict[str, Any]]:
        """Find duplicate values in arrays."""
        duplicates = []
        
        def check_array(arr, path="root"):
            if not isinstance(arr, list):
                return
            
            seen = {}
            for idx, item in enumerate(arr):
                item_str = json.dumps(item, sort_keys=True) if not isinstance(item, (list, dict)) else str(item)
                if item_str in seen:
                    duplicates.append({
                        'path': path,
                        'value': item,
                        'indices': [seen[item_str], idx]
                    })
                else:
                    seen[item_str] = idx
        
        def traverse(obj, path="root"):
            if isinstance(obj, dict):
                for key, value in obj.items():
                    traverse(value, f"{path}.{key}")
            elif isinstance(obj, list):
                check_array(obj, path)
                for idx, item in enumerate(obj):
                    traverse(item, f"{path}[{idx}]")
        
        traverse(self.data)
        return duplicates
    
    def pretty_print(self):
        """Output formatted JSON with syntax highlighting simulation."""
        print("\n" + "="*60)
        print("📄 JSON Content (Pretty Formatted)")
        print("="*60)
        print(json.dumps(self.data, indent=2, ensure_ascii=False))
        print("="*60 + "\n")
    
    def generate_report(self):
        """Generate comprehensive analysis report."""
        stats = self.analyze_structure()
        
        print("\n" + "🔍 JSON Analysis Report ".center(60, "="))
        print(f"📁 File: {self.file_path.name}")
        print(f"📏 Size: {self.file_path.stat().st_size / 1024:.2f} KB")
        print(f"📅 Modified: {datetime.fromtimestamp(self.file_path.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')}")
        print("\n" + "Structure Analysis ".center(60, "-"))
        print(f"├─ Root Type: {type(self.data).__name__}")
        print(f"├─ Max Depth: {stats['max_depth']} levels")
        print(f"├─ Total Keys: {stats['total_keys']}")
        print(f"├─ Objects: {stats['objects']}")
        print(f"├─ Arrays: {stats['arrays']}")
        print(f"└─ Null Values: {stats['null_values']}")
        
        print("\n" + "Type Distribution ".center(60, "-"))
        for dtype, count in stats['type_counts'].most_common():
            print(f"  • {dtype}: {count}")
        
        duplicates = self.find_duplicates()
        if duplicates:
            print("\n" + "⚠️  Duplicates Found ".center(60, "-"))
            for dup in duplicates[:5]:
                print(f"  • Path: {dup['path']}")
                print(f"    Indices: {dup['indices']}")
        else:
            print("\n✅ No duplicates detected")
        
        print("\n" + "="*60 + "\n")


def main():
    """CLI entry point with argument parsing."""
    parser = argparse.ArgumentParser(
        description="🔧 Advanced JSON Analyzer & Validator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s data.json --analyze
  %(prog)s config.json --validate api_key,version
  %(prog)s large.json --pretty
        """
    )
    
    parser.add_argument('file', help='Path to JSON file')
    parser.add_argument('-a', '--analyze', action='store_true', 
                        help='Generate full analysis report')
    parser.add_argument('-p', '--pretty', action='store_true',
                        help='Pretty-print formatted JSON')
    parser.add_argument('-v', '--validate', metavar='KEYS',
                        help='Validate required keys (comma-separated)')
    parser.add_argument('-d', '--duplicates', action='store_true',
                        help='Find duplicate values in arrays')
    
    args = parser.parse_args()
    
    analyzer = JSONAnalyzer(args.file)
    
    if not analyzer.load():
        sys.exit(1)
    
    if args.analyze:
        analyzer.generate_report()
    
    if args.pretty:
        analyzer.pretty_print()
    
    if args.validate:
        required_keys = [k.strip() for k in args.validate.split(',')]
        result = analyzer.validate_schema(required_keys)
        print("\n🔐 Schema Validation ".center(60, "="))
        print(f"Status: {'✅ VALID' if result['valid'] else '❌ INVALID'}")
        if result['found_keys']:
            print(f"Found: {', '.join(result['found_keys'])}")
        if result['missing_keys']:
            print(f"Missing: {', '.join(result['missing_keys'])}")
        print("="*60 + "\n")
    
    if args.duplicates:
        dups = analyzer.find_duplicates()
        print(f"\n🔎 Found {len(dups)} duplicate entries")
        for dup in dups[:10]:
            print(f"  • {dup['path']}: {dup['value']}")


if __name__ == "__main__":
    main()
