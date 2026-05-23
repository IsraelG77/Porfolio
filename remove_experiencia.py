import re
import os

files = [
    r'c:/Códigos/Porfolio/index.html',
    r'c:/Códigos/Porfolio/index-en.html'
]

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove nav link
    content = re.sub(r'[ \t]*<li><a href="#experiencia">.*?</a></li>\n?', '', content)
    
    # Remove section
    content = re.sub(r'([ \t]*)<!-- ═══ EXPERIÊNCIA ═══ -->.*?<!-- ═══ PROJETOS ═══ -->', r'\1<!-- ═══ PROJETOS ═══ -->', content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done removing 'experiencia'")
