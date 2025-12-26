import re
from pathlib import Path

# JavaScript sa debug informacijama
debug_javascript = """    <!-- Reading Progress & Active TOC Script (Debug) -->
    <script>
        console.log('🔍 TOC Script loaded');
        
        // Reading Progress Bar
        function updateProgressBar() {
            const progressBar = document.querySelector('.reading-progress');
            if (!progressBar) {
                console.warn('⚠️ Progress bar element not found');
                return;
            }
            
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
            
            console.log(`📚 Found ${sections.length} sections and ${tocLinks.length} TOC links`);
            
            if (sections.length === 0 || tocLinks.length === 0) {
                console.warn('⚠️ No sections or TOC links found');
                return;
            }
            
            let currentSection = '';
            const scrollPosition = window.pageYOffset || window.scrollY;
            const offset = 200;
            
            sections.forEach((section, index) => {
                const sectionTop = section.getBoundingClientRect().top + scrollPosition;
                const sectionId = section.getAttribute('id');
                
                if (index === 0) {
                    console.log(`📍 Section "${sectionId}" top: ${sectionTop}, scroll: ${scrollPosition + offset}`);
                }
                
                if (scrollPosition + offset >= sectionTop) {
                    currentSection = sectionId;
                }
            });
            
            if (scrollPosition < 300 && sections.length > 0) {
                currentSection = sections[0].getAttribute('id');
            }
            
            console.log(`✅ Active section: ${currentSection}`);
            
            tocLinks.forEach(link => {
                link.classList.remove('active');
                const href = link.getAttribute('href');
                if (href === '#' + currentSection) {
                    link.classList.add('active');
                    console.log(`🎯 Activated TOC link: ${href}`);
                }
            });
        }
        
        // Smooth scroll for TOC links
        function initSmoothScroll() {
            const tocLinks = document.querySelectorAll('.toc__link');
            console.log(`🔗 Initializing smooth scroll for ${tocLinks.length} TOC links`);
            
            tocLinks.forEach(link => {
                link.addEventListener('click', function(e) {
                    e.preventDefault();
                    const targetId = this.getAttribute('href');
                    const targetSection = document.querySelector(targetId);
                    
                    console.log(`🖱️ Clicked TOC link: ${targetId}`);
                    
                    if (targetSection) {
                        const offsetTop = targetSection.getBoundingClientRect().top + window.pageYOffset - 120;
                        console.log(`📜 Scrolling to: ${offsetTop}`);
                        window.scrollTo({
                            top: offsetTop,
                            behavior: 'smooth'
                        });
                        
                        setTimeout(() => updateActiveTocLink(), 100);
                    } else {
                        console.warn(`⚠️ Target section not found: ${targetId}`);
                    }
                });
            });
        }
        
        // Check if TOC is sticky
        function checkStickyStatus() {
            const toc = document.querySelector('.toc');
            if (!toc) {
                console.warn('⚠️ TOC element not found');
                return;
            }
            
            const styles = window.getComputedStyle(toc);
            console.log('📋 TOC Styles:', {
                position: styles.position,
                top: styles.top,
                display: styles.display,
                visibility: styles.visibility
            });
            
            const rect = toc.getBoundingClientRect();
            console.log('📐 TOC Position:', {
                top: rect.top,
                left: rect.left,
                width: rect.width,
                height: rect.height
            });
        }
        
        // Throttle function
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
        
        // Initialize on DOM ready
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', function() {
                console.log('📄 DOM loaded');
                initSmoothScroll();
                updateProgressBar();
                updateActiveTocLink();
                checkStickyStatus();
            });
        } else {
            console.log('📄 DOM already loaded');
            initSmoothScroll();
            updateProgressBar();
            updateActiveTocLink();
            checkStickyStatus();
        }
        
        // Event listeners
        const throttledUpdate = throttle(() => {
            updateProgressBar();
            updateActiveTocLink();
        }, 50);
        
        window.addEventListener('scroll', throttledUpdate, { passive: true });
        
        window.addEventListener('load', () => {
            console.log('🎉 Window fully loaded');
            setTimeout(() => {
                updateProgressBar();
                updateActiveTocLink();
                checkStickyStatus();
            }, 100);
        });
        
        // Log on every scroll (first 5 times only)
        let scrollCount = 0;
        window.addEventListener('scroll', () => {
            if (scrollCount < 5) {
                scrollCount++;
                console.log(`📜 Scroll event #${scrollCount}, position: ${window.pageYOffset}`);
            }
        });
    </script>
"""

def add_debug_script(file_path):
    """Zamenjuje postojeći JavaScript sa debug verzijom."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern za pronalaženje postojećeg progress & TOC scripta
    pattern = r'    <!-- Reading Progress & Active TOC Script[^>]*-->[\s\S]*?</script>'
    
    new_content = re.sub(pattern, debug_javascript.rstrip(), content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# Procesuj samo blog-post-1.html za testiranje
file_path = Path('blog-post-1.html')
if add_debug_script(file_path):
    print(f"✅ Dodat debug script u: {file_path.name}")
    print("\n📋 Otvori blog-post-1.html u browseru i pritisni F12 za Console")
    print("Videćeš detaljne informacije o tome šta radi ili ne radi!")
else:
    print(f"⚠️ Nije moguće dodati debug script")
