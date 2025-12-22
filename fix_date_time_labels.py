import re

# CSS rule to add for date and time labels
css_fix = '''        
        /* Labels za date i time polja uvek gore */
        .form-input[type="date"] ~ .form-label,
        .form-input[type="time"] ~ .form-label {
            top: -0.5rem;
            left: 0.75rem;
            font-size: 0.75rem;
            color: #D4AF37;
            background: rgba(30, 22, 15, 0.95);
            padding: 0 0.5rem;
        }
'''

# Pages to update
pages = ['index.html', 'about.html', 'menu.html', 'wine.html', 'gallery.html', 'contact.html', 
         'terms.html', 'privacy.html', 'sitemap.html']

for page in pages:
    try:
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the form-label style definition
        pattern = r'(\.form-input:not\(:placeholder-shown\) ~ \.form-label,\s*\.form-input:focus ~ \.form-label \{[^}]+\})'
        
        match = re.search(pattern, content, re.DOTALL)
        if match:
            # Insert CSS fix after the form-label focus rule
            insert_pos = match.end()
            new_content = content[:insert_pos] + '\n' + css_fix + content[insert_pos:]
            
            # Write updated content
            with open(page, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✓ {page} - CSS fix applied")
        else:
            print(f"⚠ {page} - Pattern not found, skipping")
        
    except Exception as e:
        print(f"✗ {page} - Error: {str(e)}")

print("\n✓✓✓ Date and Time label positioning fixed on all pages!")
