#!/usr/bin/env python3
"""
Cache buster for TruLeaf Landscapes website.
Adds version query string to CSS links to force instant updates.
Usage: python3 cache-buster.py [version]
"""
import os
import sys
import datetime
import re

def get_version():
    if len(sys.argv) > 1:
        return sys.argv[1]
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S")

def update_css_links(root_dir, version):
    html_files = []
    for dirpath, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(dirpath, file))
    
    updated = 0
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = re.sub(
            r'(<link[^>]*href="([^"]*)styles\.css)(")',
            r'\1?v=' + version + r'\3',
            content
        )
        
        if new_content != content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated += 1
            print(f"  Updated: {os.path.relpath(html_file, root_dir)}")
    
    return updated

if __name__ == '__main__':
    version = get_version()
    print(f"Cache buster version: {version}")
    root = '.'
    count = update_css_links(root, version)
    print(f"Updated {count} HTML files")
