#!/usr/bin/env python3
"""
Script to fix date formats in YAML front matter to be Hugo-compatible.
"""

import os
import re
from datetime import datetime
from pathlib import Path

def fix_date_format(filepath):
    """Fix date format in YAML front matter to be Hugo-compatible."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if file has YAML front matter
    if not content.startswith('---'):
        return False
    
    # Find the end of YAML front matter
    lines = content.split('\n')
    yaml_end = -1
    for i, line in enumerate(lines):
        if i > 0 and line.strip() == '---':
            yaml_end = i
            break
    
    if yaml_end == -1:
        return False
    
    # Extract YAML front matter
    yaml_lines = lines[1:yaml_end]
    rest_content = lines[yaml_end+1:]
    
    # Process YAML lines
    modified = False
    new_yaml_lines = []
    
    for line in yaml_lines:
        # Check for date field with various formats
        if line.strip().startswith('date:'):
            date_match = re.search(r'date:\s*(.+)', line)
            if date_match:
                date_value = date_match.group(1).strip()
                
                # Skip if already in correct format
                if re.match(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', date_value):
                    new_yaml_lines.append(line)
                    continue
                
                # Try to parse various date formats
                try:
                    # Format: "2020-06-28 18:49"
                    if re.match(r'\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}', date_value):
                        dt = datetime.strptime(date_value, '%Y-%m-%d %H:%M')
                        new_date = dt.strftime('%Y-%m-%dT%H:%M:00Z')
                        new_line = f"date: {new_date}"
                        new_yaml_lines.append(new_line)
                        modified = True
                        continue
                    
                    # Format: "2020-06-28"
                    elif re.match(r'\d{4}-\d{2}-\d{2}$', date_value):
                        dt = datetime.strptime(date_value, '%Y-%m-%d')
                        new_date = dt.strftime('%Y-%m-%dT00:00:00Z')
                        new_line = f"date: {new_date}"
                        new_yaml_lines.append(new_line)
                        modified = True
                        continue
                    
                    # If we can't parse it, try to extract from filename
                    else:
                        filename = os.path.basename(filepath)
                        name = filename.replace('.md', '')
                        
                        # Pattern to match: YYYYMMDDHHmmss-title
                        match = re.match(r'^(\d{14})-?(.+)$', name)
                        if match:
                            timestamp, title = match.groups()
                            try:
                                dt = datetime.strptime(timestamp, '%Y%m%d%H%M%S')
                                new_date = dt.strftime('%Y-%m-%dT%H:%M:%SZ')
                                new_line = f"date: {new_date}"
                                new_yaml_lines.append(new_line)
                                modified = True
                                continue
                            except ValueError:
                                pass
                
                except ValueError:
                    pass
                
                # If we can't fix it, keep the original
                new_yaml_lines.append(line)
            else:
                new_yaml_lines.append(line)
        else:
            new_yaml_lines.append(line)
    
    if modified:
        # Reconstruct the file
        new_content = '---\n' + '\n'.join(new_yaml_lines) + '\n---\n' + '\n'.join(rest_content)
        
        # Write back to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
    
    return False

def process_files():
    """Process all markdown files in the current directory."""
    fixed_count = 0
    total_files = 0
    
    for md_file in Path('.').rglob('*.md'):
        # Skip backup directory
        if 'backup' in str(md_file):
            continue
            
        total_files += 1
        if fix_date_format(md_file):
            fixed_count += 1
            print(f"Fixed: {md_file}")
    
    print(f"\nSummary:")
    print(f"Total files processed: {total_files}")
    print(f"Files fixed: {fixed_count}")

if __name__ == "__main__":
    process_files() 