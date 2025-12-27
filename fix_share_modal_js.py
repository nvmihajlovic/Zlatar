import re

# Process blog posts 2-12
for i in range(2, 13):
    filename = f'blog-post-{i}.html'
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and remove old duplicate JS code
        # Pattern: from old "shareBtn.addEventListener" to the closing of shareModal.addEventListener
        pattern = r'\n\s+closeShareModal\.addEventListener.*?\n\s+}\);'
        
        # Remove old JavaScript references to shareModal (not shareModalNew)
        content = re.sub(pattern, '', content, flags=re.DOTALL)
        
        # Also remove any remaining references to old modal variables
        content = re.sub(r'const shareModal = document\.getElementById\(\'shareModal\'\);?\n?', '', content)
        content = re.sub(r'const closeShareModal = document\.getElementById\(\'closeShareModal\'\);?\n?', '', content)
        content = re.sub(r'const shareLink = document\.getElementById\(\'shareLink\'\);?\n?', '', content)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f'✅ Cleaned {filename}')
    except Exception as e:
        print(f'❌ Error cleaning {filename}: {e}')

print('\n✨ Cleanup complete!')
