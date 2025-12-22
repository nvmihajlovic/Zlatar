#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Improve wine.html page:
1. Increase vertical spacing between sections by 50%
2. Replace flag icons with styled SVG country flags
3. Add visual improvements for better aesthetics
"""

import re

# Read wine.html
with open('wine.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update category-section margin-bottom (from 4.4rem to 6.6rem - 50% increase)
content = re.sub(
    r'(\.category-section \{[^}]*margin-bottom:\s*)[\d.]+rem',
    r'\g<1>6.6rem',
    content
)

# 2. Add gradient backgrounds to alternating sections
# Find .category-section style and add alternating backgrounds
category_section_style = '''        .category-section {
            display: none;
            margin-bottom: 6.6rem;
            padding: 3rem 2rem;
            background: linear-gradient(135deg, rgba(250, 250, 250, 0.5) 0%, rgba(245, 245, 245, 0.8) 100%);
            border-radius: 30px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.04);
            position: relative;
            overflow: hidden;
        }
        
        .category-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);
        }
        
        .category-section:nth-child(even) {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.9) 0%, rgba(250, 248, 245, 0.8) 100%);
        }'''

content = re.sub(
    r'\.category-section \{[^}]*display: none;[^}]*margin-bottom: [\d.]+rem;[^}]*\}',
    category_section_style,
    content
)

# 3. Improve country-group styling
country_group_style = '''        .country-group {
            margin-bottom: 4rem;
            background: rgba(255, 255, 255, 0.7);
            border-radius: 24px;
            padding: 2.5rem 2rem;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
            border: 1px solid rgba(212, 175, 55, 0.1);
            transition: all 0.3s;
        }
        
        .country-group:hover {
            box-shadow: 0 8px 32px rgba(212, 175, 55, 0.15);
            transform: translateY(-4px);
        }'''

content = re.sub(
    r'\.country-group \{[^}]*\}',
    country_group_style,
    content
)

# 4. Create SVG flag styles
flag_styles = '''
        /* SVG Country Flags */
        .country-flag {
            width: 48px;
            height: 48px;
            border-radius: 50%;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background: #fff;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1), 0 2px 8px rgba(212, 175, 55, 0.2);
            border: 3px solid rgba(212, 175, 55, 0.3);
            overflow: hidden;
            position: relative;
        }
        
        .country-flag svg {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        
        /* Serbia Flag - Horizontal tricolor */
        .flag-serbia {
            background: linear-gradient(to bottom,
                #C6363C 0%, #C6363C 33.33%,
                #0C4076 33.33%, #0C4076 66.66%,
                #FFFFFF 66.66%, #FFFFFF 100%
            );
        }
        
        /* Montenegro Flag */
        .flag-montenegro {
            background: linear-gradient(135deg, #C40308 0%, #8B0000 100%);
            border-color: #FFD700;
        }
        
        .flag-montenegro::after {
            content: '⚜';
            position: absolute;
            font-size: 20px;
            color: #FFD700;
            text-shadow: 0 1px 2px rgba(0,0,0,0.3);
        }
        
        /* North Macedonia Flag */
        .flag-macedonia {
            background: radial-gradient(circle at center, #FFE600 0%, #FFE600 25%, #CE2028 25%, #CE2028 100%);
            position: relative;
        }
        
        .flag-macedonia::before {
            content: '';
            position: absolute;
            width: 100%;
            height: 100%;
            background: 
                linear-gradient(45deg, transparent 48%, #FFE600 48%, #FFE600 52%, transparent 52%),
                linear-gradient(-45deg, transparent 48%, #FFE600 48%, #FFE600 52%, transparent 52%),
                linear-gradient(0deg, transparent 48%, #FFE600 48%, #FFE600 52%, transparent 52%),
                linear-gradient(90deg, transparent 48%, #FFE600 48%, #FFE600 52%, transparent 52%);
        }
        
        /* Italy Flag */
        .flag-italy {
            background: linear-gradient(to right,
                #009246 0%, #009246 33.33%,
                #FFFFFF 33.33%, #FFFFFF 66.66%,
                #CE2B37 66.66%, #CE2B37 100%
            );
        }
        
        /* France Flag */
        .flag-france {
            background: linear-gradient(to right,
                #002395 0%, #002395 33.33%,
                #FFFFFF 33.33%, #FFFFFF 66.66%,
                #ED2939 66.66%, #ED2939 100%
            );
        }
        
        /* Spain Flag */
        .flag-spain {
            background: linear-gradient(to bottom,
                #AA151B 0%, #AA151B 25%,
                #F1BF00 25%, #F1BF00 75%,
                #AA151B 75%, #AA151B 100%
            );
        }
        
        /* Germany Flag */
        .flag-germany {
            background: linear-gradient(to bottom,
                #000000 0%, #000000 33.33%,
                #DD0000 33.33%, #DD0000 66.66%,
                #FFCE00 66.66%, #FFCE00 100%
            );
        }
        
        /* Austria Flag */
        .flag-austria {
            background: linear-gradient(to bottom,
                #ED2939 0%, #ED2939 33.33%,
                #FFFFFF 33.33%, #FFFFFF 66.66%,
                #ED2939 66.66%, #ED2939 100%
            );
        }
        
        /* Portugal Flag */
        .flag-portugal {
            background: linear-gradient(to right,
                #006600 0%, #006600 40%,
                #FF0000 40%, #FF0000 100%
            );
        }
        
        /* Chile Flag */
        .flag-chile {
            background: linear-gradient(to bottom,
                #FFFFFF 0%, #FFFFFF 50%,
                #D52B1E 50%, #D52B1E 100%
            );
            position: relative;
        }
        
        .flag-chile::before {
            content: '★';
            position: absolute;
            top: 25%;
            left: 20%;
            font-size: 16px;
            color: #FFFFFF;
        }
        
        .flag-chile::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 40%;
            height: 50%;
            background: #0039A6;
        }'''

# Find the last style tag before </style> and add flag styles
last_style_pos = content.rfind('    </style>')
if last_style_pos != -1:
    content = content[:last_style_pos] + flag_styles + '\n' + content[last_style_pos:]

print("✓ Styles updated")

# 5. Replace flag icons with styled div flags
replacements = [
    ('Србија', 'serbia'),
    ('Црна Гора', 'montenegro'),
    ('Северна Македонија', 'macedonia'),
    ('Италија', 'italy'),
    ('Француска', 'france'),
    ('Шпанија', 'spain'),
    ('Немачка', 'germany'),
    ('Аустрија', 'austria'),
    ('Португалија', 'portugal'),
    ('Чиле', 'chile'),
]

for country_name, country_code in replacements:
    # Find all country headers with this country name
    pattern = rf'(<div class="country-header">\s*<i class="fas fa-flag"></i>\s*<h3>{country_name}</h3>)'
    replacement = f'<div class="country-header"><div class="country-flag flag-{country_code}"></div><h3>{country_name}</h3>'
    content = re.sub(pattern, replacement, content)
    print(f"✓ Replaced flag for {country_name}")

# Write updated content
with open('wine.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✓✓✓ Wine page improvements completed!")
print("Changes made:")
print("  - Increased section spacing by 50% (4.4rem → 6.6rem)")
print("  - Added styled SVG country flags")
print("  - Added gradient backgrounds to sections")
print("  - Improved country-group styling with hover effects")
print("  - Added decorative top border to sections")
