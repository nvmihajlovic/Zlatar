import codecs

# Update blog-post-2 through blog-post-12
for i in range(2, 13):
    filename = f'blog-post-{i}.html'
    
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if nav-toggle already exists
        if 'id="navToggle"' in content:
            print(f"✓ {filename} - већ има nav-toggle")
            continue
        
        # Add nav-toggle button
        old_nav_actions = '''            <div class="nav-actions" style="display: flex; align-items: center; gap: 1.5rem; margin-left: auto; padding-left: 3rem;">
                <button class="btn-reserve" id="btnReserve" style="background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%); color: #fff; font-weight: 600; font-size: 0.9rem; padding: 0.75rem 1.8rem; border: none; border-radius: 50px; cursor: pointer; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); box-shadow: 0 6px 20px rgba(212,175,55,0.4), inset 0 1px 0 rgba(255,255,255,0.3); letter-spacing: 0.5px;">
                    <i class="fas fa-calendar-check" style="margin-right: 0.5rem;"></i>
                    <span data-i18n="nav.reserve">Резервација</span>
                </button>
            </div>'''
        
        new_nav_actions = '''            <div class="nav-actions" style="display: flex; align-items: center; gap: 1.5rem; margin-left: auto; padding-left: 3rem;">
                <button class="btn-reserve" id="btnReserve" style="background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%); color: #fff; font-weight: 600; font-size: 0.9rem; padding: 0.75rem 1.8rem; border: none; border-radius: 50px; cursor: pointer; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); box-shadow: 0 6px 20px rgba(212,175,55,0.4), inset 0 1px 0 rgba(255,255,255,0.3); letter-spacing: 0.5px;">
                    <i class="fas fa-calendar-check" style="margin-right: 0.5rem;"></i>
                    <span data-i18n="nav.reserve">Резервација</span>
                </button>
                <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation" style="margin-left: 0.5rem;">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
            </div>'''
        
        content = content.replace(old_nav_actions, new_nav_actions)
        
        # Write updated content
        with codecs.open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Додат nav-toggle у {filename}")
        
    except FileNotFoundError:
        print(f"✗ Није пронађено: {filename}")
    except Exception as e:
        print(f"✗ Грешка у {filename}: {str(e)}")

print("\nЗавршено! Nav-toggle додат на свим страницама.")
