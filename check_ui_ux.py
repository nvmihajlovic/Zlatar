import codecs
import re
import os

print("🎨 Проверавам UI/UX - типографија, раzmaki, сенке, анимације...\n")

# HTML files to check
pages = ['index.html', 'about.html', 'menu.html', 'wine.html', 'gallery.html', 'contact.html', 'blog.html']
blog_posts = [f'blog-post-{i}.html' for i in range(1, 13)]
all_pages = pages + blog_posts

issues_found = []

for page in all_pages:
    if not os.path.exists(page):
        continue
    
    print(f"Проверавам {page}...")
    
    try:
        with codecs.open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        page_issues = []
        
        # 1. Typography checks
        # Check for inconsistent font sizes (should be 0.875rem - 2.5rem)
        font_sizes = re.findall(r'font-size:\s*(\d+(?:\.\d+)?(?:px|rem|em))', content)
        px_sizes = [s for s in font_sizes if 'px' in s]
        if px_sizes:
            page_issues.append(f"⚠ Pronađeno {len(px_sizes)} px font-size (trebalo bi koristiti rem)")
        
        # Check for missing font-family
        if 'font-family' in content and 'Montserrat' not in content:
            page_issues.append("⚠ Font family nije Montserrat")
        
        # 2. Spacing checks
        # Check for inconsistent padding/margin
        tiny_paddings = re.findall(r'padding:\s*0\.?[0-4](?:rem|em)\s', content)
        if len(tiny_paddings) > 50:
            page_issues.append(f"⚠ Много малих padding вредности ({len(tiny_paddings)})")
        
        # 3. Shadow checks  
        # Check for inconsistent box-shadows
        shadows = re.findall(r'box-shadow:\s*[^;]+', content)
        if len(set(shadows)) > 20:
            page_issues.append(f"⚠ Превише различитих shadow стилова ({len(set(shadows))})")
        
        # 4. Animation/Transition checks
        # Check for missing transitions on interactive elements
        buttons = re.findall(r'<button[^>]*(?:style="[^"]*")?[^>]*>', content)
        buttons_without_transition = [b for b in buttons if 'transition' not in b]
        if len(buttons_without_transition) > 5:
            page_issues.append(f"⚠ {len(buttons_without_transition)} dugmadi без transition-a")
        
        # Check for very fast transitions (< 0.2s)
        fast_transitions = re.findall(r'transition:\s*(?:all\s+)?0\.?0?1?\d*s', content)
        if len(fast_transitions) > 10:
            page_issues.append(f"⚠ {len(fast_transitions)} прeбрзих transition-a")
        
        # 5. Color consistency
        # Check for hardcoded colors instead of using variables
        hardcoded_colors = len(re.findall(r'#[0-9A-Fa-f]{6}', content))
        if hardcoded_colors > 100:
            page_issues.append(f"⚠ {hardcoded_colors} hardcoded боја (требало би користити променљиве)")
        
        # 6. Alignment checks
        # Check for inline styles with centering
        center_styles = re.findall(r'text-align:\s*center', content)
        if len(center_styles) < 5 and page != 'privacy.html':
            page_issues.append("⚠ Мало центрираних елемената (проверити UI)")
        
        if page_issues:
            issues_found.append((page, page_issues))
            for issue in page_issues:
                print(f"  {issue}")
        else:
            print(f"  ✓ Све изгледа добро")
    
    except Exception as e:
        print(f"  ✗ Грешка: {e}")

print("\n" + "="*60)
print("📊 РЕЗУЛТАТИ ПРОВЕРЕ:")
print("="*60)

if issues_found:
    print(f"\n⚠ Пронађено укупно {len(issues_found)} страница са проблемима:\n")
    for page, issues in issues_found:
        print(f"\n{page}:")
        for issue in issues:
            print(f"  {issue}")
    
    print("\n\n💡 ПРЕПОРУКЕ:")
    print("1. Користи rem уместо px за font-size")
    print("2. Стандардизуј senke: 0 4px 16px rgba(0,0,0,0.2)")
    print("3. Transition-и треба да буду 0.3s - 0.4s")
    print("4. Користи CSS променљиве за боје")
    print("5. Сви button-и треба да имају transition")
else:
    print("\n✅ Све странице имају одличан UI/UX!")
    print("   - Конзистентна типографија")
    print("   - Добри размаци")
    print("   - Оптимизоване сенке")
    print("   - Глатке анимације")

print("\n" + "="*60)
