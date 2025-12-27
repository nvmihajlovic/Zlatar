import re

# Process blog posts 2-12
for i in range(2, 13):
    filename = f'blog-post-{i}.html'
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove all references to old shareModal variable (not shareModalNew)
        # This includes any remaining addEventListener calls
        content = re.sub(r'\s+shareModal\.addEventListener\([^)]+\).*?\}\);', '', content, flags=re.DOTALL)
        content = re.sub(r'\s+shareModal\.style\.display.*?;', '', content)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f'✅ Final cleanup {filename}')
    except Exception as e:
        print(f'❌ Error: {e}')

print('\n✨ Done!')
