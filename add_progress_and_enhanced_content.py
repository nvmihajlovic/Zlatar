import re
from pathlib import Path

# Dodaj progress bar i poboljšane stilove
enhanced_styles = """
        /* Reading Progress Bar */
        .reading-progress {
            position: fixed;
            top: 80px;
            left: 0;
            width: 0%;
            height: 4px;
            background: linear-gradient(90deg, #FFD700 0%, #D4AF37 50%, #B8860B 100%);
            box-shadow: 0 2px 10px rgba(212,175,55,0.5);
            z-index: 9999;
            transition: width 0.1s ease;
        }
        
        .reading-progress::after {
            content: '';
            position: absolute;
            right: 0;
            top: -2px;
            width: 8px;
            height: 8px;
            background: #FFD700;
            border-radius: 50%;
            box-shadow: 0 0 15px rgba(255,215,0,0.8);
        }
"""

improved_toc_styles = """
        /* Enhanced Table of Contents */
        .toc {
            position: sticky;
            top: 120px;
            height: fit-content;
            background: linear-gradient(135deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(212,175,55,0.15);
            border-radius: 20px;
            padding: 2rem;
            box-shadow: 0 8px 32px rgba(0,0,0,0.2);
        }
        
        .toc__title {
            font-size: 1.2rem;
            font-weight: 800;
            margin-bottom: 1.5rem;
            background: linear-gradient(135deg, #FFD700 0%, #D4AF37 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .toc__list {
            list-style: none;
            padding: 0;
        }
        
        .toc__item {
            margin-bottom: 0.5rem;
        }
        
        .toc__link {
            color: rgba(255,255,255,0.65);
            text-decoration: none;
            font-size: 0.95rem;
            font-weight: 500;
            transition: all 0.3s;
            display: block;
            padding: 0.75rem 1rem;
            border-left: 3px solid transparent;
            border-radius: 0 8px 8px 0;
            position: relative;
            overflow: hidden;
        }
        
        .toc__link::before {
            content: '';
            position: absolute;
            left: 0;
            top: 0;
            width: 0;
            height: 100%;
            background: linear-gradient(90deg, rgba(212,175,55,0.1) 0%, transparent 100%);
            transition: width 0.3s;
            z-index: -1;
        }
        
        .toc__link:hover,
        .toc__link.active {
            color: #FFD700;
            border-left-color: #D4AF37;
            transform: translateX(5px);
        }
        
        .toc__link:hover::before,
        .toc__link.active::before {
            width: 100%;
        }
        
        .toc__link.active {
            font-weight: 700;
            background: rgba(212,175,55,0.08);
            border-left-color: #FFD700;
            box-shadow: inset 0 0 20px rgba(212,175,55,0.1);
        }
"""

enhanced_article_content = """
        /* Enhanced Article Content */
        .article__content {
            background: linear-gradient(135deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(212,175,55,0.12);
            border-radius: 24px;
            padding: 4rem;
            margin-bottom: 3rem;
            box-shadow: 0 8px 32px rgba(0,0,0,0.2);
        }
        
        .article__content > p:first-of-type::first-letter {
            font-size: 4.5rem;
            font-weight: 900;
            line-height: 0.9;
            float: left;
            margin: 0.1em 0.15em 0 0;
            background: linear-gradient(135deg, #FFD700 0%, #D4AF37 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .article__content p {
            font-size: 1.15rem;
            line-height: 1.9;
            color: rgba(255,255,255,0.88);
            margin-bottom: 1.8rem;
            font-weight: 400;
            letter-spacing: 0.01em;
        }
        
        .article__content p strong {
            color: #FFD700;
            font-weight: 700;
        }
        
        .article__content h2 {
            font-size: 2.2rem;
            font-weight: 800;
            color: #fff;
            margin: 4rem 0 2rem 0;
            padding-top: 1.5rem;
            position: relative;
            letter-spacing: -0.01em;
        }
        
        .article__content h2::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 60px;
            height: 4px;
            background: linear-gradient(90deg, #FFD700 0%, #D4AF37 100%);
            border-radius: 2px;
        }
        
        .article__content h3 {
            font-size: 1.65rem;
            font-weight: 700;
            color: rgba(255,255,255,0.95);
            margin: 2.5rem 0 1.25rem 0;
            position: relative;
            padding-left: 1.5rem;
        }
        
        .article__content h3::before {
            content: '◆';
            position: absolute;
            left: 0;
            color: #D4AF37;
            font-size: 0.8em;
        }
        
        .article__content ul, 
        .article__content ol {
            margin: 2rem 0;
            padding-left: 2.5rem;
        }
        
        .article__content li {
            font-size: 1.15rem;
            line-height: 1.9;
            color: rgba(255,255,255,0.85);
            margin-bottom: 1rem;
            position: relative;
        }
        
        .article__content ul li::marker {
            color: #D4AF37;
            font-size: 1.2em;
        }
        
        .article__content ol li {
            padding-left: 0.5rem;
        }
        
        .article__content ol li::marker {
            color: #D4AF37;
            font-weight: 700;
        }
        
        .article__content blockquote {
            background: linear-gradient(135deg, rgba(212,175,55,0.08) 0%, rgba(212,175,55,0.03) 100%);
            border-left: 5px solid #D4AF37;
            padding: 2rem 2.5rem;
            margin: 3rem 0;
            font-style: italic;
            font-size: 1.3rem;
            font-weight: 500;
            color: rgba(255,255,255,0.92);
            position: relative;
            border-radius: 0 16px 16px 0;
            box-shadow: 0 4px 20px rgba(212,175,55,0.1);
        }
        
        .article__content blockquote::before {
            content: '"';
            position: absolute;
            top: -10px;
            left: 15px;
            font-size: 5rem;
            color: rgba(212,175,55,0.3);
            font-family: Georgia, serif;
            line-height: 1;
        }
"""

# JavaScript za progress bar i active TOC
progress_script = """
    <!-- Reading Progress & Active TOC Script -->
    <script>
        // Reading Progress Bar
        function updateProgressBar() {
            const progressBar = document.querySelector('.reading-progress');
            if (!progressBar) return;
            
            const windowHeight = window.innerHeight;
            const documentHeight = document.documentElement.scrollHeight - windowHeight;
            const scrolled = window.pageYOffset;
            const progress = (scrolled / documentHeight) * 100;
            
            progressBar.style.width = progress + '%';
        }
        
        // Active TOC Links
        function updateActiveTocLink() {
            const sections = document.querySelectorAll('.article__content h2[id], .article__content h3[id]');
            const tocLinks = document.querySelectorAll('.toc__link');
            
            let currentSection = '';
            const scrollPosition = window.pageYOffset + 150;
            
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                if (scrollPosition >= sectionTop) {
                    currentSection = section.getAttribute('id');
                }
            });
            
            tocLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === '#' + currentSection) {
                    link.classList.add('active');
                }
            });
        }
        
        // Smooth scroll for TOC links
        document.querySelectorAll('.toc__link').forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const targetId = this.getAttribute('href');
                const targetSection = document.querySelector(targetId);
                
                if (targetSection) {
                    const offsetTop = targetSection.offsetTop - 100;
                    window.scrollTo({
                        top: offsetTop,
                        behavior: 'smooth'
                    });
                }
            });
        });
        
        // Event listeners
        window.addEventListener('scroll', () => {
            updateProgressBar();
            updateActiveTocLink();
        });
        
        window.addEventListener('load', () => {
            updateProgressBar();
            updateActiveTocLink();
        });
    </script>
"""

def enhance_blog_posts(file_path):
    """Dodaje progress bar, poboljšane TOC i tekst stilove."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # 1. Dodaj progress bar HTML ako ne postoji
    if '<div class="reading-progress"></div>' not in content:
        content = content.replace(
            '    <!-- Page Transition Overlay -->',
            '    <!-- Reading Progress Bar -->\n    <div class="reading-progress"></div>\n\n    <!-- Page Transition Overlay -->'
        )
        modified = True
    
    # 2. Dodaj progress bar stilove nakon blog-hero stilova
    if '.reading-progress {' not in content:
        content = content.replace(
            '        /* Enhanced Table of Contents */',
            enhanced_styles + '\n' + improved_toc_styles
        )
        modified = True
    
    # 3. Zameni TOC stilove ako već postoje
    if '        .toc {' in content and '.toc__link.active {' not in content:
        pattern = r'(        /\* Enhanced Table of Contents \*/\s+)(        \.toc \{[^}]+\}[\s\S]*?)(        /\* Article Main Content \*/)'
        if re.search(pattern, content):
            content = re.sub(pattern, improved_toc_styles + '\n\n' + r'        /* Article Main Content */', content)
            modified = True
    
    # 4. Zameni article__content stilove
    if '        .article__content {' in content and '::first-letter' not in content:
        pattern = r'(        /\* Article Main Content \*/[\s\S]*?)(        \.article__content \{[^}]+\}[\s\S]*?)(        /\* Like Section \*/)'
        if re.search(pattern, content):
            content = re.sub(
                pattern,
                '        /* Article Main Content */\n        .article__main {\n            max-width: 800px;\n        }\n        \n' + 
                enhanced_article_content + '\n        \n' + 
                r'        /* Like Section */',
                content
            )
            modified = True
    
    # 5. Dodaj JavaScript pre zatvarajućeg </body> taga
    if 'updateProgressBar()' not in content:
        content = content.replace('</body>', progress_script + '\n</body>')
        modified = True
    
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Procesuj sve blog post fajlove
blog_posts = list(Path('.').glob('blog-post-*.html'))
success_count = 0

for post in sorted(blog_posts):
    if enhance_blog_posts(post):
        success_count += 1
        print(f"✅ Poboljšano: {post.name}")
    else:
        print(f"⚠️  Već ažurirano ili greška: {post.name}")

print(f"\n✅ Završeno! Uspešno ažurirano {success_count}/{len(blog_posts)} stranica")
