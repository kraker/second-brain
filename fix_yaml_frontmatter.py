#!/usr/bin/env python3
"""
Script to fix YAML front matter issues in markdown files.
"""

import os
import re
import shutil
from pathlib import Path

def fix_yaml_frontmatter(filepath):
    """Fix YAML front matter by adding proper values for empty fields."""
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
    content_lines = lines[yaml_end + 1:]
    
    # Fix empty title field
    fixed_yaml = []
    title_fixed = False
    date_fixed = False
    
    for line in yaml_lines:
        if line.strip() == 'title:' or line.strip() == 'title: ':
            # Extract title from filename or first heading
            filename = Path(filepath).stem
            # Remove timestamp prefix if present
            if re.match(r'^\d{14}', filename):
                title = filename[15:]  # Remove timestamp and dash
            else:
                title = filename
            
            # Convert to title case and replace hyphens/underscores with spaces
            title = title.replace('-', ' ').replace('_', ' ').title()
            fixed_yaml.append(f'title: {title}')
            title_fixed = True
        elif line.strip() == 'date:' or line.strip() == 'date: ':
            # Extract date from filename if it has timestamp
            filename = Path(filepath).stem
            if re.match(r'^\d{14}', filename):
                timestamp = filename[:14]
                year = timestamp[:4]
                month = timestamp[4:6]
                day = timestamp[6:8]
                hour = timestamp[8:10]
                minute = timestamp[10:12]
                second = timestamp[12:14]
                date_str = f'{year}-{month}-{day}T{hour}:{minute}:{second}Z'
                fixed_yaml.append(f'date: {date_str}')
            else:
                fixed_yaml.append('date: 2020-01-01T00:00:00Z')
            date_fixed = True
        else:
            fixed_yaml.append(line)
    
    # If no title was found, add one
    if not title_fixed:
        filename = Path(filepath).stem
        if re.match(r'^\d{14}', filename):
            title = filename[15:]  # Remove timestamp and dash
        else:
            title = filename
        title = title.replace('-', ' ').replace('_', ' ').title()
        fixed_yaml.insert(0, f'title: {title}')
    
    # If no date was found, add one
    if not date_fixed:
        filename = Path(filepath).stem
        if re.match(r'^\d{14}', filename):
            timestamp = filename[:14]
            year = timestamp[:4]
            month = timestamp[4:6]
            day = timestamp[6:8]
            hour = timestamp[8:10]
            minute = timestamp[10:12]
            second = timestamp[12:14]
            date_str = f'{year}-{month}-{day}T{hour}:{minute}:{second}Z'
            fixed_yaml.insert(1, f'date: {date_str}')
        else:
            fixed_yaml.insert(1, 'date: 2020-01-01T00:00:00Z')
    
    # Reconstruct the file
    new_content = '---\n' + '\n'.join(fixed_yaml) + '\n---\n' + '\n'.join(content_lines)
    
    # Write back to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def main():
    """Main function to fix all markdown files."""
    # Get all markdown files in the second-brain directory
    second_brain_dir = Path('second-brain')
    markdown_files = list(second_brain_dir.glob('*.md'))
    
    fixed_count = 0
    
    for filepath in markdown_files:
        if fix_yaml_frontmatter(filepath):
            print(f"Fixed YAML front matter in: {filepath.name}")
            fixed_count += 1
    
    print(f"\nTotal files fixed: {fixed_count}")

if __name__ == '__main__':
    main() 