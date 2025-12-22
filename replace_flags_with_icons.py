#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Replace all CSS country flags with Flag Icon CSS library icons
"""

# Flag mappings: CSS class -> ISO 3166-1 alpha-2 code
FLAG_MAPPINGS = {
    'flag-serbia': 'fi-rs',          # Serbia
    'flag-montenegro': 'fi-me',       # Montenegro
    'flag-croatia': 'fi-hr',          # Croatia
    'flag-slovenia': 'fi-si',         # Slovenia
    'flag-macedonia': 'fi-mk',        # North Macedonia
    'flag-italy': 'fi-it',            # Italy
    'flag-france': 'fi-fr',           # France
    'flag-spain': 'fi-es',            # Spain
    'flag-germany': 'fi-de',          # Germany
    'flag-austria': 'fi-at',          # Austria
    'flag-portugal': 'fi-pt',         # Portugal
    'flag-chile': 'fi-cl',            # Chile
    'flag-argentina': 'fi-ar',        # Argentina
}

def replace_flags_in_html(file_path):
    """Replace all CSS flag classes with Flag Icon CSS classes"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Replace all flag references in HTML
    for old_class, new_class in FLAG_MAPPINGS.items():
        # Pattern: <div class="country-flag flag-xxx"></div>
        # Replace with: <div class="country-flag"><span class="fi fi-xxx"></span></div>
        old_pattern = f'<div class="country-flag {old_class}"></div>'
        new_pattern = f'<div class="country-flag"><span class="fi {new_class}"></span></div>'
        
        count = content.count(old_pattern)
        if count > 0:
            content = content.replace(old_pattern, new_pattern)
            print(f"✓ Replaced {count} instance(s) of {old_class} with {new_class}")
    
    # Remove all CSS flag definitions (between /* Serbia Flag */ and the end of flag styles)
    # Find and remove the old CSS flag styles
    css_start_markers = [
        '/* Serbia Flag - Horizontal tricolor */',
        '/* Serbia Flag */',
    ]
    
    css_end_marker = '</style>'
    
    # Find the start of flag CSS
    flag_css_start = -1
    for marker in css_start_markers:
        idx = content.find(marker)
        if idx != -1:
            flag_css_start = idx
            break
    
    if flag_css_start != -1:
        # Find the corresponding closing style tag
        style_end = content.find(css_end_marker, flag_css_start)
        
        if style_end != -1:
            # Check if there's a closing brace before </style>
            last_brace = content.rfind('}', flag_css_start, style_end)
            
            if last_brace != -1:
                # Remove everything from the flag CSS start to after the last closing brace
                # But keep everything after it (the </style> tag and script)
                content = content[:flag_css_start] + content[last_brace + 1:]
                print(f"\n✓ Removed all CSS flag definitions")
    
    # Write back
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n✓ Successfully updated {file_path}")
        return True
    else:
        print(f"\n✗ No changes made to {file_path}")
        return False

if __name__ == '__main__':
    file_path = 'wine.html'
    success = replace_flags_in_html(file_path)
    
    if success:
        print("\n" + "="*60)
        print("REPLACEMENTS COMPLETED SUCCESSFULLY")
        print("="*60)
        print("\nAll country flags now use Flag Icon CSS library (fi fi-xx)")
        print("Old CSS flag definitions have been removed")
        print("\nFlag Icon CSS codes used:")
        for old_class, new_class in FLAG_MAPPINGS.items():
            country = old_class.replace('flag-', '').title()
            print(f"  • {country}: {new_class}")
