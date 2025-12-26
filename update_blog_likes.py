import codecs
import re

# Read the template from blog-post-1.html
with codecs.open('blog-post-1.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Update blog-post-2 through blog-post-12
for i in range(2, 13):
    filename = f'blog-post-{i}.html'
    
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Update hero likes to add ID and remove interactive classes
        content = re.sub(
            r'<div class="blog-hero__meta-item blog-hero__meta-item--like" id="likeButton">\s*<i class="far fa-heart" id="heartIcon"></i>\s*<span id="likeCount">(\d+) лајкова</span>\s*</div>',
            r'<div class="blog-hero__meta-item">\n                    <i class="fas fa-heart"></i>\n                    <span id="heroLikeCount">\1 лајкова</span>\n                </div>',
            content
        )
        
        # Also handle if it's just a regular meta item without like button classes
        content = re.sub(
            r'<div class="blog-hero__meta-item">\s*<i class="fas fa-heart"></i>\s*<span>(\d+) лајкова</span>\s*</div>',
            r'<div class="blog-hero__meta-item">\n                    <i class="fas fa-heart"></i>\n                    <span id="heroLikeCount">\1 лајкова</span>\n                </div>',
            content
        )
        
        # 2. Remove old hero like button CSS if it exists
        content = re.sub(
            r'\.blog-hero__meta-item--like \{[^}]+\}\s*\.blog-hero__meta-item--like:hover \{[^}]+\}\s*\.blog-hero__meta-item--like:hover i \{[^}]+\}\s*\.blog-hero__meta-item--like\.liked i \{[^}]+\}\s*\.blog-hero__meta-item--like\.liked \.fa-heart \{[^}]+\}\s*\.blog-hero__meta-item--like \.fa-heart \{[^}]+\}\s*',
            '',
            content
        )
        
        # 3. Add article-like section if it doesn't exist
        if '<!-- Like Section -->' not in content:
            share_buttons_match = re.search(r'(</div>\s*<!-- Share Buttons -->)', content)
            if share_buttons_match:
                like_section = '''
                    <!-- Like Section -->
                    <div class="article-like">
                        <p class="article-like__text">Да ли вам се свидео овај чланак?</p>
                        <button class="article-like__button" id="likeButton">
                            <i class="far fa-heart" id="heartIcon"></i>
                            <span id="likeCount">89 лајкова</span>
                        </button>
                    </div>

                    '''
                content = content.replace('<!-- Share Buttons -->', like_section + '<!-- Share Buttons -->')
        
        # 4. Add article-like CSS if it doesn't exist
        if '.article-like {' not in content:
            share_buttons_css = re.search(r'(/\* Share Buttons \*/\s*\.share-buttons \{[^}]+\})', content)
            if share_buttons_css:
                like_css = '''

        /* Article Like Button */
        .article-like {
            text-align: center;
            padding: 3rem 0;
            margin-bottom: 1.5rem;
        }

        .article-like__text {
            color: rgba(255, 255, 255, 0.6);
            font-size: 1.125rem;
            margin-bottom: 1.5rem;
        }

        .article-like__button {
            background: linear-gradient(135deg, rgba(212,175,55,0.1) 0%, rgba(184,134,11,0.1) 100%);
            border: 2px solid #D4AF37;
            border-radius: 50px;
            padding: 1.25rem 3rem;
            font-family: 'Montserrat', sans-serif;
            font-size: 1.125rem;
            font-weight: 600;
            color: #fff;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            display: inline-flex;
            align-items: center;
            gap: 0.75rem;
        }

        .article-like__button i {
            font-size: 1.5rem;
            transition: all 0.3s ease;
        }

        .article-like__button:hover {
            background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%);
            border-color: #FFD700;
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(212,175,55,0.4);
        }

        .article-like__button:hover i {
            transform: scale(1.2);
        }

        .article-like__button.liked {
            background: linear-gradient(135deg, #ff4458 0%, #d42943 100%);
            border-color: #ff4458;
        }

        .article-like__button.liked i {
            font-weight: 900;
            animation: heartBeat 0.6s ease;
        }

        @keyframes heartBeat {
            0%, 100% { transform: scale(1); }
            25% { transform: scale(1.4); }
            50% { transform: scale(1.2); }
            75% { transform: scale(1.3); }
        }
'''
                content = content.replace('/* Share Buttons */', like_css + '\n        /* Share Buttons */')
        
        # 5. Update JavaScript to sync both displays and use correct article ID
        article_id = f'blog-post-{i}'
        
        # Find and replace the Like Functionality JavaScript
        js_pattern = r'// Like Functionality.*?// Initialize like status on page load\s*checkLikeStatus\(\);'
        
        new_js = f'''// Like Functionality
        const likeButton = document.getElementById('likeButton');
        const heartIcon = document.getElementById('heartIcon');
        const likeCount = document.getElementById('likeCount');
        const heroLikeCount = document.getElementById('heroLikeCount');
        const articleId = '{article_id}'; // Unique ID for this article
        let currentLikes = 89; // Base like count
        
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
        checkLikeStatus();'''
        
        content = re.sub(js_pattern, new_js, content, flags=re.DOTALL)
        
        # Write updated content
        with codecs.open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Ажурирано: {filename}")
        
    except FileNotFoundError:
        print(f"✗ Није пронађено: {filename}")
    except Exception as e:
        print(f"✗ Грешка у {filename}: {str(e)}")

print("\nЗавршено! Свих 11 страница је ажурирано са функционалношћу лајковања.")
