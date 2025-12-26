import codecs
import re

# Blog post data with their like counts from blog.html
blog_data = [
    {'id': 2, 'likes': 187},
    {'id': 3, 'likes': 134},
    {'id': 4, 'likes': 156},
    {'id': 5, 'likes': 178},
    {'id': 6, 'likes': 145},
    {'id': 7, 'likes': 129},
    {'id': 8, 'likes': 201},
    {'id': 9, 'likes': 167},
    {'id': 10, 'likes': 143},
    {'id': 11, 'likes': 189},
    {'id': 12, 'likes': 176},
]

for post in blog_data:
    post_id = post['id']
    likes = post['likes']
    filename = f'blog-post-{post_id}.html'
    
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if Like Functionality already exists
        if '// Like Functionality' in content:
            print(f"✓ {filename} - већ има JavaScript за лајковање")
            continue
        
        # Add Like Functionality JavaScript before "// Page Transition"
        like_js = f'''
        // Like Functionality
        const likeButton = document.getElementById('likeButton');
        const heartIcon = document.getElementById('heartIcon');
        const likeCount = document.getElementById('likeCount');
        const heroLikeCount = document.getElementById('heroLikeCount');
        const articleId = 'blog-post-{post_id}'; // Unique ID for this article
        let currentLikes = {likes}; // Base like count
        
        // Check if user has liked this article
        function checkLikeStatus() {{
            const liked = localStorage.getItem('liked_' + articleId);
            if (liked === 'true') {{
                likeButton.classList.add('liked');
                currentLikes = parseInt(localStorage.getItem('likes_' + articleId)) || currentLikes + 1;
                updateLikeDisplay();
            }}
        }}
        
        // Update like count display (both button and hero)
        function updateLikeDisplay() {{
            const likeText = currentLikes === 1 ? 'лајк' : (currentLikes % 10 === 1 && currentLikes !== 11) ? 'лајк' : 'лајкова';
            const displayText = currentLikes.toLocaleString('sr-RS') + ' ' + likeText;
            likeCount.textContent = displayText;
            if (heroLikeCount) {{
                heroLikeCount.textContent = displayText;
            }}
        }}
        
        // Handle like button click
        likeButton.addEventListener('click', () => {{
            const isLiked = likeButton.classList.contains('liked');
            
            if (isLiked) {{
                // Unlike
                likeButton.classList.remove('liked');
                currentLikes--;
                localStorage.removeItem('liked_' + articleId);
                localStorage.removeItem('likes_' + articleId);
            }} else {{
                // Like
                likeButton.classList.add('liked');
                currentLikes++;
                localStorage.setItem('liked_' + articleId, 'true');
                localStorage.setItem('likes_' + articleId, currentLikes);
            }}
            
            updateLikeDisplay();
        }});
        
        // Initialize like status on page load
        checkLikeStatus();

        '''
        
        content = content.replace('// Page Transition', like_js + '// Page Transition')
        
        # Write updated content
        with codecs.open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Додат JavaScript за лајковање у {filename}")
        
    except FileNotFoundError:
        print(f"✗ Није пронађено: {filename}")
    except Exception as e:
        print(f"✗ Грешка у {filename}: {str(e)}")

print("\nЗавршено! JavaScript за лајковање је додат на свим страницама.")
