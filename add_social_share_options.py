import re
import os

# List of all blog post files
blog_files = [
    'blog-post-1.html',
    'blog-post-2.html',
    'blog-post-3.html',
    'blog-post-4.html',
    'blog-post-5.html',
    'blog-post-6.html',
    'blog-post-7.html',
    'blog-post-8.html',
    'blog-post-9.html',
    'blog-post-10.html',
    'blog-post-11.html',
    'blog-post-12.html'
]

# New share buttons HTML (Viber, Instagram, TikTok)
new_buttons = '''                <button onclick="shareToViber()" style="display: flex; align-items: center; justify-content: center; gap: 0.75rem; padding: 1rem; background: #7360F2; border: none; border-radius: 12px; color: #fff; cursor: pointer; transition: all 0.3s; font-family: 'Montserrat', sans-serif; font-weight: 600;">
                    <i class="fab fa-viber"></i>
                    Viber
                </button>
                <button onclick="shareToInstagram()" style="display: flex; align-items: center; justify-content: center; gap: 0.75rem; padding: 1rem; background: linear-gradient(45deg, #F58529 0%, #DD2A7B 50%, #8134AF 100%); border: none; border-radius: 12px; color: #fff; cursor: pointer; transition: all 0.3s; font-family: 'Montserrat', sans-serif; font-weight: 600;">
                    <i class="fab fa-instagram"></i>
                    Instagram
                </button>
                <button onclick="shareToTikTok()" style="display: flex; align-items: center; justify-content: center; gap: 0.75rem; padding: 1rem; background: #000000; border: none; border-radius: 12px; color: #fff; cursor: pointer; transition: all 0.3s; font-family: 'Montserrat', sans-serif; font-weight: 600;">
                    <i class="fab fa-tiktok"></i>
                    TikTok
                </button>'''

# New share functions JavaScript
new_functions = '''
        function shareToViber() {
            window.open(`viber://forward?text=${encodeURIComponent(document.title + ' ' + window.location.href)}`, '_blank');
        }

        function shareToInstagram() {
            // Instagram ne podržava direktno deljenje linkova, pa otvaramo profil ili kopiramo link
            copyLink();
            alert('Link je kopiran! Možete ga podeliti na Instagram-u.');
        }

        function shareToTikTok() {
            // TikTok ne podržava direktno deljenje linkova, pa otvaramo profil ili kopiramo link
            copyLink();
            alert('Link je kopiran! Možete ga podeliti na TikTok-u.');
        }
'''

for blog_file in blog_files:
    if not os.path.exists(blog_file):
        print(f"⚠️  File {blog_file} not found, skipping...")
        continue
    
    with open(blog_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the WhatsApp button and add new buttons after it
    whatsapp_pattern = r'(<button onclick="shareToWhatsApp\(\)"[^>]*>[\s\S]*?WhatsApp[\s\S]*?</button>)'
    
    if re.search(whatsapp_pattern, content):
        content = re.sub(
            whatsapp_pattern,
            r'\1' + '\n' + new_buttons,
            content
        )
    else:
        print(f"⚠️  WhatsApp button not found in {blog_file}")
        continue
    
    # Add new share functions after copyLink function
    copy_link_pattern = r'(function copyLink\(\) \{[\s\S]*?\n        \})'
    
    if re.search(copy_link_pattern, content):
        content = re.sub(
            copy_link_pattern,
            r'\1' + new_functions,
            content
        )
    else:
        print(f"⚠️  copyLink function not found in {blog_file}")
        continue
    
    # Write updated content
    with open(blog_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Updated {blog_file}")

print("\n🎉 All blog posts updated with Viber, Instagram, and TikTok share options!")
