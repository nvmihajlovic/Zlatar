import os
import shutil
from datetime import datetime

# Get current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Create backup folder name with timestamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
backup_folder = os.path.join(current_dir, f"backup_{timestamp}")

# Create backup directory
os.makedirs(backup_folder, exist_ok=True)

# Files and folders to backup
items_to_backup = [
    'index.html',
    'about.html',
    'menu.html',
    'wine.html',
    'gallery.html',
    'contact.html',
    'terms.html',
    'privacy.html',
    'sitemap.html',
    'i18n.js',
    'script.js',
    'style.css',
    'style-mobile-first.css',
    'new-script.js',
    'new-style.css',
    'README.md',
    'images',
    'jelovnik',
    'pansoft'
]

print(f"Creating backup in: {backup_folder}")

# Copy each item
for item in items_to_backup:
    source = os.path.join(current_dir, item)
    destination = os.path.join(backup_folder, item)
    
    if os.path.exists(source):
        try:
            if os.path.isdir(source):
                shutil.copytree(source, destination)
                print(f"✓ Copied folder: {item}")
            else:
                shutil.copy2(source, destination)
                print(f"✓ Copied file: {item}")
        except Exception as e:
            print(f"✗ Error copying {item}: {str(e)}")
    else:
        print(f"⚠ Skipped (not found): {item}")

print(f"\n✓ Backup completed successfully!")
print(f"Backup location: {backup_folder}")
