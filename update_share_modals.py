import re

# New share modal HTML and CSS
new_share_modal = '''    <!-- Share Modal -->
    <style>
        .share-modal-overlay {
            display: none;
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            right: 0 !important;
            bottom: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
            background: rgba(0, 0, 0, 0.85) !important;
            z-index: 999999 !important;
            padding: 20px;
            overflow-y: auto;
        }
        
        .share-modal-overlay.active {
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
        }
        
        .share-modal-content {
            background: linear-gradient(135deg, rgba(30,22,15,0.98) 0%, rgba(40,30,20,0.98) 100%);
            padding: 2.5rem;
            border-radius: 20px;
            max-width: 650px;
            width: 100%;
            position: relative;
            border: 1px solid rgba(212,175,55,0.2);
            margin: auto;
        }
        
        .share-modal-close {
            position: absolute;
            top: 1rem;
            right: 1rem;
            background: rgba(255,255,255,0.1);
            border: none;
            border-radius: 50%;
            width: 36px;
            height: 36px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #fff;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .share-modal-close:hover {
            background: rgba(212,175,55,0.3);
            transform: rotate(90deg);
        }
        
        .share-modal-title {
            font-size: 1.75rem;
            color: #D4AF37;
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            gap: 0.75rem;
            font-family: 'Montserrat', sans-serif;
        }
        
        .share-buttons-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1rem;
            margin-bottom: 1.5rem;
        }
        
        .share-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.75rem;
            padding: 1rem;
            border: none;
            border-radius: 12px;
            color: #fff;
            cursor: pointer;
            transition: all 0.3s;
            font-family: 'Montserrat', sans-serif;
            font-weight: 600;
        }
        
        .share-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 16px rgba(0,0,0,0.3);
        }
        
        .share-link-container {
            padding: 1rem;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 12px;
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        
        .share-link-input {
            flex: 1;
            background: transparent;
            border: none;
            color: rgba(255,255,255,0.7);
            font-family: 'Montserrat', sans-serif;
            outline: none;
        }
        
        @media (max-width: 768px) {
            .share-modal-content {
                padding: 2rem 1.25rem;
                width: 95%;
                max-width: none;
                margin: 1rem;
            }
            
            .share-buttons-grid {
                grid-template-columns: repeat(2, 1fr);
                gap: 0.75rem;
            }
            
            .share-btn {
                padding: 0.875rem 0.5rem;
                font-size: 0.875rem;
            }
        }
        
        @media (max-width: 480px) {
            .share-modal-content {
                padding: 1.5rem 1rem;
            }
            
            .share-modal-title {
                font-size: 1.25rem;
            }
            
            .share-btn {
                font-size: 0.8125rem;
                padding: 0.75rem 0.375rem;
            }
        }
    </style>
    
    <div class="share-modal-overlay" id="shareModalNew">
        <div class="share-modal-content">
            <button class="share-modal-close" id="closeShareModalNew">
                <i class="fas fa-times"></i>
            </button>
            
            <h3 class="share-modal-title">
                <i class="fas fa-share-alt"></i>
                Подели чланак
            </h3>
            
            <div class="share-buttons-grid">
                <button class="share-btn" style="background: #1877F2;" onclick="shareToFacebook()">
                    <i class="fab fa-facebook-f"></i>
                    Facebook
                </button>
                <button class="share-btn" style="background: #1DA1F2;" onclick="shareToTwitter()">
                    <i class="fab fa-twitter"></i>
                    Twitter
                </button>
                <button class="share-btn" style="background: #0A66C2;" onclick="shareToLinkedIn()">
                    <i class="fab fa-linkedin-in"></i>
                    LinkedIn
                </button>
                <button class="share-btn" style="background: #25D366;" onclick="shareToWhatsApp()">
                    <i class="fab fa-whatsapp"></i>
                    WhatsApp
                </button>
                <button class="share-btn" style="background: #7360F2;" onclick="shareToViber()">
                    <i class="fab fa-viber"></i>
                    Viber
                </button>
                <button class="share-btn" style="background: linear-gradient(45deg, #F58529 0%, #DD2A7B 50%, #8134AF 100%);" onclick="shareToInstagram()">
                    <i class="fab fa-instagram"></i>
                    Instagram
                </button>
            </div>
            
            <div class="share-link-container">
                <input type="text" class="share-link-input" id="shareLinkNew" readonly>
                <button class="share-btn" style="background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%); padding: 0.5rem 1rem;" onclick="copyLink()">
                    <i class="fas fa-copy"></i>
                </button>
            </div>
        </div>
    </div>

    <!-- Newsletter CTA Section -->'''

# New JavaScript for share modal
new_js = '''        // Share modal functionality
        const shareBtn = document.getElementById('shareBtn');
        const shareModalNew = document.getElementById('shareModalNew');
        const closeShareModalNew = document.getElementById('closeShareModalNew');
        const shareLinkNew = document.getElementById('shareLinkNew');
        
        if (shareLinkNew) {
            shareLinkNew.value = window.location.href;
        }
        
        if (shareBtn && shareModalNew) {
            shareBtn.addEventListener('click', (e) => {
                e.preventDefault();
                shareModalNew.classList.add('active');
            });
        }
        
        if (closeShareModalNew && shareModalNew) {
            closeShareModalNew.addEventListener('click', () => {
                shareModalNew.classList.remove('active');
            });
        }
        
        if (shareModalNew) {
            shareModalNew.addEventListener('click', (e) => {
                if (e.target === shareModalNew) {
                    shareModalNew.classList.remove('active');
                }
            });
        }'''

new_copy_function = '''
        function copyLink() {
            const input = document.getElementById('shareLinkNew');
            if (input) {
                input.select();
                document.execCommand('copy');
                
                const btn = event.target.closest('button');
                const originalHTML = btn.innerHTML;
                btn.innerHTML = '<i class="fas fa-check"></i>';
                
                setTimeout(() => {
                    btn.innerHTML = originalHTML;
                }, 2000);
            }
        }'''

# Update blog posts 2-12
for i in range(2, 13):
    filename = f'blog-post-{i}.html'
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace share modal HTML section
        pattern = r'<!-- Share Modal -->.*?<!-- Newsletter CTA Section -->'
        content = re.sub(pattern, new_share_modal, content, flags=re.DOTALL)
        
        # Replace share modal JavaScript
        js_pattern = r'// Share modal functionality.*?}\);'
        content = re.sub(js_pattern, new_js, content, flags=re.DOTALL)
        
        # Replace copyLink function
        copy_pattern = r'function copyLink\(\) \{[^}]*(?:\{[^}]*\}[^}]*)*\}'
        content = re.sub(copy_pattern, new_copy_function.strip(), content, flags=re.DOTALL)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f'✅ Updated {filename}')
    except Exception as e:
        print(f'❌ Error updating {filename}: {e}')

print('\n✨ Share modal update complete!')
