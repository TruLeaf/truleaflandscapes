import re

with open('index.html', encoding='utf-8') as f:
    content = f.read()
canon = re.findall(r'<link rel="canonical"[^>]*>', content)
og = re.findall(r'<meta property="og:url"[^>]*>', content)
print('Canonical:', canon)
print('OG:', og)
