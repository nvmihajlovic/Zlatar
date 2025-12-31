import re

with open('menu.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern za CSS koji treba ukloniti (samo deo sa .nav-menu pozicioniranjem)
pattern = r'\.nav-menu\s*\{[^}]*position:\s*fixed[^}]*right:\s*-320px[^}]*\}[^}]*\.nav-menu\.active\s*\{[^}]*\}[^}]*\.nav-menu\s*\.nav-item\s*\{[^}]*opacity:\s*0[^}]*\}[^}]*\.nav-menu\.active\s*\.nav-item\s*\{[^}]*\}[^}]*\.nav-menu\.active\s*\.nav-item:nth-child\(1\)[^}]*\}[^}]*\.nav-menu\.active\s*\.nav-item:nth-child\(2\)[^}]*\}[^}]*\.nav-menu\.active\s*\.nav-item:nth-child\(3\)[^}]*\}[^}]*\.nav-menu\.active\s*\.nav-item:nth-child\(4\)[^}]*\}[^}]*\.nav-menu\.active\s*\.nav-item:nth-child\(5\)[^}]*\}[^}]*\.nav-menu\.active\s*\.nav-item:nth-child\(6\)[^}]*\}'

# Ukloni pattern
content = re.sub(pattern, '', content, flags=re.DOTALL)

# Sada ukloni pojedinačno pravila koja su ostala
rules_to_remove = [
    r'\.nav-menu\s*\{[^}]*position:\s*fixed\s*!important[^}]*\}',
    r'\.nav-menu\.active\s*\{[^}]*right:\s*0\s*!important[^}]*\}',
]

for rule in rules_to_remove:
    content = re.sub(rule, '', content, flags=re.DOTALL)

with open('menu.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ CSS conflicts removed from menu.html")
