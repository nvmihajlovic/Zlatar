import re
import codecs

print("🔧 Копирам navbar CSS са blog.html на blog-post странице...\n")

# Read blog.html
with codecs.open('blog.html', 'r', encoding='utf-8') as f:
    blog_content = f.read()

# Extract mobile nav CSS from blog.html (after last closing brace before @media)
mobile_css_pattern = r'(@media \(max-width: 1281px\) \{.*?@media \(min-width: 1282px\) \{.*?\})\s*</style>'
mobile_css_match = re.search(mobile_css_pattern, blog_content, re.DOTALL)

if mobile_css_match:
    blog_mobile_css = mobile_css_match.group(1)
    print("✓ Извучен mobile CSS из blog.html")
else:
    print("✗ Нисам пронашао mobile CSS у blog.html")
    exit(1)

# Now update blog-post files
for i in range(1, 13):
    filename = f'blog-post-{i}.html'
    
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove ALL existing mobile nav CSS
        # Remove everything from first @media (max-width: 1281px) to </style>
        content = re.sub(
            r'@media \(max-width: 1281px\).*?</style>',
            blog_mobile_css + '\n\n    </style>',
            content,
            flags=re.DOTALL
        )
        
        with codecs.open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Копиран CSS у {filename}")
    
    except FileNotFoundError:
        print(f"✗ Фајл {filename} не постоји")
    except Exception as e:
        print(f"✗ Грешка код {filename}: {e}")

print("\n✅ ГОТОВО!")
print("Mobile navbar CSS са blog.html је копиран на све blog-post странице.")
