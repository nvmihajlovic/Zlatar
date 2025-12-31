#!/usr/bin/env python3
"""Generate proper PWA icons with background for Restoran Zlatar"""

from PIL import Image, ImageDraw
import os

def create_pwa_icons():
    """Create PWA icons with proper background and padding"""
    
    # Load the original logo
    logo_path = "images/znak-restoran-zlatar-vektorski_clipped_rev_1.png"
    
    if not os.path.exists(logo_path):
        print(f"❌ Logo file not found: {logo_path}")
        return
    
    logo = Image.open(logo_path).convert("RGBA")
    
    # Background colors
    bg_color = (20, 15, 8, 255)  # #140f08 - dark background
    gold_color = (212, 175, 55, 255)  # #D4AF37 - gold accent
    
    sizes = [192, 512]
    
    for size in sizes:
        # Create icon with background (for 'any' purpose)
        bg_img = Image.new('RGBA', (size, size), bg_color)
        
        # Resize logo to 80% of icon size (leave some padding)
        logo_size = int(size * 0.8)
        logo_resized = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        
        # Center the logo
        offset = ((size - logo_size) // 2, (size - logo_size) // 2)
        bg_img.paste(logo_resized, offset, logo_resized)
        
        # Save standard icon
        bg_img.save(f"images/icon-{size}x{size}.png", "PNG", optimize=True)
        print(f"✅ Created icon-{size}x{size}.png")
        
        # Create maskable icon with more padding (70% of size)
        maskable_bg = Image.new('RGBA', (size, size), bg_color)
        logo_maskable = int(size * 0.7)
        logo_mask_resized = logo.resize((logo_maskable, logo_maskable), Image.Resampling.LANCZOS)
        
        offset_mask = ((size - logo_maskable) // 2, (size - logo_maskable) // 2)
        maskable_bg.paste(logo_mask_resized, offset_mask, logo_mask_resized)
        
        # Save maskable icon
        maskable_bg.save(f"images/icon-{size}x{size}-maskable.png", "PNG", optimize=True)
        print(f"✅ Created icon-{size}x{size}-maskable.png")
    
    # Create favicon (32x32) with gold border for visibility
    favicon = Image.new('RGBA', (32, 32), bg_color)
    
    # Add subtle gold border
    draw = ImageDraw.Draw(favicon)
    draw.rectangle([0, 0, 31, 31], outline=gold_color, width=1)
    
    logo_favicon = logo.resize((28, 28), Image.Resampling.LANCZOS)
    favicon.paste(logo_favicon, (2, 2), logo_favicon)
    favicon.save("favicon.ico", format="ICO", sizes=[(32, 32)])
    print(f"✅ Created favicon.ico")
    
    # Create apple-touch-icon (180x180)
    apple_icon = Image.new('RGBA', (180, 180), bg_color)
    logo_apple = logo.resize((144, 144), Image.Resampling.LANCZOS)
    apple_icon.paste(logo_apple, (18, 18), logo_apple)
    apple_icon.save("images/apple-touch-icon.png", "PNG", optimize=True)
    print(f"✅ Created apple-touch-icon.png")
    
    print("\n🎉 All PWA icons generated successfully!")

if __name__ == "__main__":
    create_pwa_icons()
