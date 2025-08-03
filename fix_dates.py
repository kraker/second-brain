#!/usr/bin/env python3
"""
Script to fix empty date fields in YAML front matter by extracting date from filename.
"""

import os
import re
from datetime import datetime
from pathlib import Path

def extract_date_from_filename(filename):
    """Extract date from filename like 20200628184910-chmod.md"""
    # Remove .md extension
    name = filename.replace('.md', '')
    
    # Pattern to match: YYYYMMDDHHmmss-title
    match = re.match(r'^(\d{14})-?(.+)$', name)
    if match:
        timestamp, title = match.groups()
        try:
            # Parse the timestamp
            dt = datetime.strptime(timestamp, '%Y%m%d%H%M%S')
            return dt.strftime('%Y-%m-%dT%H:%M:%SZ')
        except ValueError:
            return None
    
    return None

def fix_yaml_frontmatter(filepath):
    """Fix YAML front matter by adding proper date from filename."""
    filename = os.path.basename(filepath)
    date_from_filename = extract_date_from_filename(filename)
    
    if not date_from_filename:
        return False
    
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
    yaml_content = '\n'.join(yaml_lines)
    
    # Check if date field is empty
    if 'date: ' in yaml_content and not re.search(r'date:\s*\S', yaml_content):
        # Replace empty date with proper date
        yaml_content = re.sub(r'date:\s*$', f'date: {date_from_filename}', yaml_content, flags=re.MULTILINE)
        
        # Reconstruct the file
        new_content = '---\n' + yaml_content + '\n---\n' + '\n'.join(lines[yaml_end + 1:])
        
        # Write back to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
    
    return False

def main():
    """Main function to process all markdown files."""
    fixed_count = 0
    total_files = 0
    
    # Process all markdown files in current directory
    for md_file in Path('.').rglob('*.md'):
        if md_file.is_file() and not str(md_file).startswith('backup_'):
            total_files += 1
            if fix_yaml_frontmatter(md_file):
                fixed_count += 1
                print(f"Fixed: {md_file}")
    
    print(f"\nSummary:")
    print(f"Total files processed: {total_files}")
    print(f"Files fixed: {fixed_count}")

if __name__ == "__main__":
    main() 