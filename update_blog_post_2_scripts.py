import re

# Read the file
with open('blog-post-2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# New blog post scripts
new_scripts = '''    <!-- Blog Post Scripts -->
    <script>
        // Generate dynamic Table of Contents
        function generateTOC() {
            const article = document.querySelector('article');
            const headings = article.querySelectorAll('h2[id]');
            const tocList = document.getElementById('tocList');
            
            headings.forEach((heading, index) => {
                const li = document.createElement('li');
                li.style.cssText = 'margin-bottom: 0.75rem;';
                
                const a = document.createElement('a');
                a.href = `#${heading.id}`;
                a.textContent = heading.textContent;
                a.className = 'toc-link';
                a.style.cssText = 'display: block; padding: 0.75rem 1rem; color: rgba(255,255,255,0.7); text-decoration: none; border-radius: 8px; transition: all 0.3s; font-size: 0.95rem; border-left: 3px solid transparent;';
                
                a.addEventListener('click', (e) => {
                    e.preventDefault();
                    heading.scrollIntoView({ behavior: 'smooth', block: 'start' });
                });
                
                li.appendChild(a);
                tocList.appendChild(li);
            });
        }

        // Update active TOC link on scroll
        function updateActiveTOC() {
            const headings = document.querySelectorAll('h2[id]');
            const tocLinks = document.querySelectorAll('.toc-link');
            
            let current = '';
            
            headings.forEach(heading => {
                const sectionTop = heading.offsetTop;
                const scrollPosition = window.scrollY + 150;
                
                if (scrollPosition >= sectionTop) {
                    current = heading.getAttribute('id');
                }
            });
            
            tocLinks.forEach(link => {
                link.style.color = 'rgba(255,255,255,0.7)';
                link.style.background = 'transparent';
                link.style.borderLeftColor = 'transparent';
                
                if (link.getAttribute('href') === `#${current}`) {
                    link.style.color = '#D4AF37';
                    link.style.background = 'rgba(212,175,55,0.1)';
                    link.style.borderLeftColor = '#D4AF37';
                }
            });
        }

        // Update progress bar on scroll
        function updateProgressBar() {
            const windowHeight = window.innerHeight;
            const documentHeight = document.documentElement.scrollHeight - windowHeight;
            const scrolled = window.scrollY;
            const progress = (scrolled / documentHeight) * 100;
            
            document.getElementById('progressBar').style.width = progress + '%';
        }

        // Like functionality
        const likeBtn = document.getElementById('likeBtn');
        const likeCount = document.getElementById('likeCount');
        const postId = 'blog-post-2';
        
        // Check if already liked
        if (localStorage.getItem(`blog_like_${postId}`)) {
            likeBtn.classList.add('liked');
            likeBtn.querySelector('i').classList.remove('far');
            likeBtn.querySelector('i').classList.add('fas');
            likeBtn.style.background = 'rgba(212,175,55,0.2)';
            likeBtn.style.borderColor = 'rgba(212,175,55,0.4)';
            likeBtn.style.color = '#D4AF37';
        }
        
        likeBtn.addEventListener('click', function() {
            let count = parseInt(likeCount.textContent);
            const icon = this.querySelector('i');
            
            if (this.classList.contains('liked')) {
                this.classList.remove('liked');
                icon.classList.remove('fas');
                icon.classList.add('far');
                this.style.background = 'rgba(255,255,255,0.05)';
                this.style.borderColor = 'rgba(255,255,255,0.1)';
                this.style.color = 'rgba(255,255,255,0.8)';
                count--;
                localStorage.removeItem(`blog_like_${postId}`);
            } else {
                this.classList.add('liked');
                icon.classList.remove('far');
                icon.classList.add('fas');
                this.style.background = 'rgba(212,175,55,0.2)';
                this.style.borderColor = 'rgba(212,175,55,0.4)';
                this.style.color = '#D4AF37';
                count++;
                localStorage.setItem(`blog_like_${postId}`, 'true');
            }
            
            likeCount.textContent = count;
        });

        // Share modal functionality
        const shareBtn = document.getElementById('shareBtn');
        const shareModal = document.getElementById('shareModal');
        const closeShareModal = document.getElementById('closeShareModal');
        const shareLink = document.getElementById('shareLink');
        
        shareLink.value = window.location.href;
        
        shareBtn.addEventListener('click', () => {
            shareModal.style.display = 'flex';
        });
        
        closeShareModal.addEventListener('click', () => {
            shareModal.style.display = 'none';
        });
        
        shareModal.addEventListener('click', (e) => {
            if (e.target === shareModal) {
                shareModal.style.display = 'none';
            }
        });

        // Share functions
        function shareToFacebook() {
            window.open(`https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(window.location.href)}`, '_blank');
        }

        function shareToTwitter() {
            window.open(`https://twitter.com/intent/tweet?url=${encodeURIComponent(window.location.href)}&text=40 Година Традиције - Restoran Zlatar`, '_blank');
        }

        function shareToLinkedIn() {
            window.open(`https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(window.location.href)}`, '_blank');
        }

        function shareToWhatsApp() {
            window.open(`https://wa.me/?text=${encodeURIComponent('40 Година Традиције - Restoran Zlatar ' + window.location.href)}`, '_blank');
        }

        function copyLink() {
            shareLink.select();
            document.execCommand('copy');
            
            const btn = event.target.closest('button');
            const originalHTML = btn.innerHTML;
            btn.innerHTML = '<i class="fas fa-check"></i>';
            
            setTimeout(() => {
                btn.innerHTML = originalHTML;
            }, 2000);
        }

        // Smooth scrolling for back to blog button
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth' });
                }
            });
        });

        // Initialize on page load
        document.addEventListener('DOMContentLoaded', () => {
            generateTOC();
            updateProgressBar();
            updateActiveTOC();
        });

        // Update on scroll
        window.addEventListener('scroll', () => {
            updateProgressBar();
            updateActiveTOC();
        });
    </script>'''

# Find and replace the old blog scripts section
pattern = r'<!-- Blog Posts Data and Rendering -->.*?(?=<!-- Mobile Navigation -->)'
content = re.sub(pattern, new_scripts + '\n    ', content, flags=re.DOTALL)

# Write back
with open('blog-post-2.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Blog post scripts updated successfully!")
