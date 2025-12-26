import re
from pathlib import Path

# Poboljšan JavaScript za dinamički TOC
improved_javascript = """    <!-- Reading Progress & Active TOC Script -->
    <script>
        // Reading Progress Bar
        function updateProgressBar() {
            const progressBar = document.querySelector('.reading-progress');
            if (!progressBar) return;
            
            const windowHeight = window.innerHeight;
            const documentHeight = document.documentElement.scrollHeight - windowHeight;
            const scrolled = window.pageYOffset || window.scrollY;
            const progress = (scrolled / documentHeight) * 100;
            
            progressBar.style.width = Math.min(progress, 100) + '%';
        }
        
        // Active TOC Links - Improved
        function updateActiveTocLink() {
            const sections = document.querySelectorAll('.article__content h2[id]');
            const tocLinks = document.querySelectorAll('.toc__link');
            
            if (sections.length === 0 || tocLinks.length === 0) return;
            
            let currentSection = '';
            const scrollPosition = window.pageYOffset || window.scrollY;
            const offset = 200; // Offset for navbar
            
            // Find the current section based on scroll position
            sections.forEach(section => {
                const sectionTop = section.getBoundingClientRect().top + scrollPosition;
                const sectionId = section.getAttribute('id');
                
                if (scrollPosition + offset >= sectionTop) {
                    currentSection = sectionId;
                }
            });
            
            // If at the very top, highlight first section
            if (scrollPosition < 300 && sections.length > 0) {
                currentSection = sections[0].getAttribute('id');
            }
            
            // Update active class on TOC links
            tocLinks.forEach(link => {
                link.classList.remove('active');
                const href = link.getAttribute('href');
                if (href === '#' + currentSection) {
                    link.classList.add('active');
                }
            });
        }
        
        // Smooth scroll for TOC links
        function initSmoothScroll() {
            document.querySelectorAll('.toc__link').forEach(link => {
                link.addEventListener('click', function(e) {
                    e.preventDefault();
                    const targetId = this.getAttribute('href');
                    const targetSection = document.querySelector(targetId);
                    
                    if (targetSection) {
                        const offsetTop = targetSection.getBoundingClientRect().top + window.pageYOffset - 120;
                        window.scrollTo({
                            top: offsetTop,
                            behavior: 'smooth'
                        });
                        
                        // Update active state immediately
                        setTimeout(() => updateActiveTocLink(), 100);
                    }
                });
            });
        }
        
        // Throttle function to improve performance
        function throttle(func, limit) {
            let inThrottle;
            return function() {
                const args = arguments;
                const context = this;
                if (!inThrottle) {
                    func.apply(context, args);
                    inThrottle = true;
                    setTimeout(() => inThrottle = false, limit);
                }
            }
        }
        
        // Debounce function for resize events
        function debounce(func, wait) {
            let timeout;
            return function() {
                const context = this;
                const args = arguments;
                clearTimeout(timeout);
                timeout = setTimeout(() => func.apply(context, args), wait);
            };
        }
        
        // Initialize on DOM ready
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', function() {
                initSmoothScroll();
                updateProgressBar();
                updateActiveTocLink();
            });
        } else {
            initSmoothScroll();
            updateProgressBar();
            updateActiveTocLink();
        }
        
        // Event listeners with throttling for better performance
        const throttledUpdate = throttle(() => {
            updateProgressBar();
            updateActiveTocLink();
        }, 50);
        
        window.addEventListener('scroll', throttledUpdate, { passive: true });
        window.addEventListener('resize', debounce(() => {
            updateProgressBar();
            updateActiveTocLink();
        }, 200));
        
        // Update on window load (for images and other content)
        window.addEventListener('load', () => {
            setTimeout(() => {
                updateProgressBar();
                updateActiveTocLink();
            }, 100);
        });
    </script>
"""

def fix_toc_javascript(file_path):
    """Zamenjuje postojeći JavaScript sa poboljšanom verzijom."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern za pronalaženje postojećeg progress & TOC scripta
    pattern = r'    <!-- Reading Progress & Active TOC Script -->[\s\S]*?</script>'
    
    new_content = re.sub(pattern, improved_javascript.rstrip(), content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# Procesuj sve blog post fajlove
blog_posts = list(Path('.').glob('blog-post-*.html'))
success_count = 0

for post in sorted(blog_posts):
    if fix_toc_javascript(post):
        success_count += 1
        print(f"✅ Ažuriran TOC u: {post.name}")
    else:
        print(f"⚠️  Nije pronađen script u: {post.name}")

print(f"\n✅ Završeno! Uspešno ažurirano {success_count}/{len(blog_posts)} stranica")
