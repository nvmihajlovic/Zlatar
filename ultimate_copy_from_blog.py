import codecs

print("🔧 Копирам КОМПЛЕТНУ структуру са blog.html...\n")

# Read entire blog.html
with codecs.open('blog.html', 'r', encoding='utf-8') as f:
    blog_html = f.read()

# Extract everything from <!DOCTYPE> to end of <body> tag start
head_and_nav = blog_html.split('<section class="hero-blog">')[0]

print("✓ Извучен head + navbar из blog.html")
print(f"  Дужина: {len(head_and_nav)} карактера\n")

# Now for each blog-post file, keep only the content after navbar
for i in range(1, 13):
    filename = f'blog-post-{i}.html'
    
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find where the actual article content starts (after navbar)
        # Look for the blog hero section
        if '<section class="blog-hero">' in content:
            article_start = content.find('<section class="blog-hero">')
            article_content = content[article_start:]
            
            # Combine blog.html head+nav with this article's content
            new_content = head_and_nav + article_content
            
            with codecs.open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✓ Поправљен {filename}")
        else:
            print(f"⚠ Нисам пронашао <section class=\"blog-hero\"> у {filename}")
    
    except FileNotFoundError:
        print(f"✗ Фајл {filename} не постоји")
    except Exception as e:
        print(f"✗ Грешка код {filename}: {e}")

print("\n✅ ГОТОВО!")
print("\nСве blog-post странице сада имају:")
print("  ✓ Идентичан <head> као blog.html")
print("  ✓ Идентичан navbar као blog.html")  
print("  ✓ Исти CSS линкови")
print("  ✓ Исти JavaScript")
