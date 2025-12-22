import re

# Read index.html to extract modal and JavaScript
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract modal HTML (from line 946 to before Back to Top button)
modal_match = re.search(r'(<!-- Reservation Modal -->.*?</div>\s*</div>\s*\n\s*<!-- Back to Top)', index_content, re.DOTALL)
if modal_match:
    modal_html = modal_match.group(1).replace('<!-- Back to Top', '').strip()
    print("✓ Modal HTML extracted")
else:
    print("✗ Failed to extract modal")
    exit(1)

# Create JavaScript for modal
modal_js = '''
    <!-- Modal JavaScript -->
    <script>
        // Reservation Modal Functionality
        const btnReserve = document.getElementById('btnReserve');
        const reservationModal = document.getElementById('reservationModal');
        const modalOverlay = document.getElementById('modalOverlay');
        const modalClose = document.getElementById('modalClose');
        const reservationForm = document.getElementById('reservationForm');
        
        // Open modal
        if (btnReserve) {
            btnReserve.addEventListener('click', () => {
                reservationModal.classList.add('active');
                document.body.style.overflow = 'hidden';
            });
        }
        
        // Close modal functions
        function closeModal() {
            reservationModal.classList.remove('active');
            document.body.style.overflow = '';
        }
        
        if (modalClose) {
            modalClose.addEventListener('click', closeModal);
        }
        
        if (modalOverlay) {
            modalOverlay.addEventListener('click', closeModal);
        }
        
        // Close on ESC key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && reservationModal.classList.contains('active')) {
                closeModal();
            }
        });
        
        // Handle form submission
        if (reservationForm) {
            reservationForm.addEventListener('submit', (e) => {
                e.preventDefault();
                
                const formData = {
                    name: document.getElementById('resName').value,
                    phone: document.getElementById('resPhone').value,
                    date: document.getElementById('resDate').value,
                    time: document.getElementById('resTime').value,
                    guests: document.getElementById('resGuests').value,
                    note: document.getElementById('resNote').value
                };
                
                // Here you would typically send data to server
                console.log('Reservation data:', formData);
                
                // Show success message
                alert('Хвала! Ваша резервација је послата. Контактираћемо вас ускоро за потврду.');
                
                // Close modal and reset form
                closeModal();
                reservationForm.reset();
            });
        }
        
        // Set minimum date to today
        const resDate = document.getElementById('resDate');
        if (resDate) {
            const today = new Date().toISOString().split('T')[0];
            resDate.setAttribute('min', today);
        }
    </script>
'''

# CSS for modal (if not already present)
modal_css = '''
    <style>
        /* Modal Styles */
        .modal {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 10000;
            opacity: 0;
            visibility: hidden;
            transition: opacity 0.3s, visibility 0.3s;
        }
        
        .modal.active {
            opacity: 1;
            visibility: visible;
        }
        
        .modal-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.85);
            backdrop-filter: blur(8px);
        }
        
        .modal-content {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: linear-gradient(180deg, rgba(40, 30, 20, 0.98) 0%, rgba(30, 22, 15, 0.98) 100%);
            border-radius: 24px;
            padding: 3rem;
            max-width: 600px;
            width: 90%;
            max-height: 90vh;
            overflow-y: auto;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5), 0 0 100px rgba(212, 175, 55, 0.15);
            border: 1px solid rgba(212, 175, 55, 0.2);
        }
        
        .modal-close {
            position: absolute;
            top: 1.5rem;
            right: 1.5rem;
            width: 40px;
            height: 40px;
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #fff;
            font-size: 1.25rem;
            cursor: pointer;
            transition: all 0.3s;
            z-index: 10;
        }
        
        .modal-close:hover {
            background: rgba(212, 175, 55, 0.2);
            border-color: rgba(212, 175, 55, 0.4);
            color: #D4AF37;
            transform: rotate(90deg);
        }
        
        .modal-header {
            text-align: center;
            margin-bottom: 2rem;
        }
        
        .modal-header i {
            font-size: 3rem;
            color: #D4AF37;
            margin-bottom: 1rem;
        }
        
        .modal-header h2 {
            font-size: 2rem;
            color: #fff;
            margin-bottom: 0.5rem;
            font-weight: 700;
        }
        
        .modal-header p {
            color: rgba(255, 255, 255, 0.7);
            font-size: 1rem;
        }
        
        .reservation-form {
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }
        
        .form-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.5rem;
        }
        
        .form-group {
            position: relative;
        }
        
        .form-input {
            width: 100%;
            padding: 1rem;
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 12px;
            color: #fff;
            font-size: 1rem;
            font-family: 'Montserrat', sans-serif;
            transition: all 0.3s;
        }
        
        .form-input:focus {
            outline: none;
            background: rgba(255, 255, 255, 0.12);
            border-color: rgba(212, 175, 55, 0.5);
            box-shadow: 0 0 0 3px rgba(212, 175, 55, 0.1);
        }
        
        .form-input:not(:placeholder-shown) ~ .form-label,
        .form-input:focus ~ .form-label {
            top: -0.5rem;
            left: 0.75rem;
            font-size: 0.75rem;
            color: #D4AF37;
            background: rgba(30, 22, 15, 0.95);
            padding: 0 0.5rem;
        }
        
        .form-label {
            position: absolute;
            top: 1rem;
            left: 1rem;
            color: rgba(255, 255, 255, 0.6);
            font-size: 1rem;
            pointer-events: none;
            transition: all 0.3s;
        }
        
        .form-input[type="date"],
        .form-input[type="time"] {
            color-scheme: dark;
        }
        
        .form-input[type="date"]::-webkit-calendar-picker-indicator,
        .form-input[type="time"]::-webkit-calendar-picker-indicator {
            filter: invert(0.7) sepia(1) saturate(5) hue-rotate(10deg);
            cursor: pointer;
        }
        
        select.form-input {
            cursor: pointer;
        }
        
        select.form-input option {
            background: #1a1410;
            color: #fff;
        }
        
        textarea.form-input {
            resize: vertical;
            min-height: 100px;
        }
        
        .btn-full {
            width: 100%;
            padding: 1rem 2rem;
            background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%);
            color: #fff;
            border: none;
            border-radius: 50px;
            font-size: 1.125rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.75rem;
            box-shadow: 0 8px 24px rgba(212, 175, 55, 0.4);
        }
        
        .btn-full:hover {
            transform: translateY(-2px);
            box-shadow: 0 12px 32px rgba(212, 175, 55, 0.5);
        }
        
        @media (max-width: 768px) {
            .modal-content {
                padding: 2rem 1.5rem;
                width: 95%;
            }
            
            .form-row {
                grid-template-columns: 1fr;
                gap: 1rem;
            }
            
            .modal-header h2 {
                font-size: 1.5rem;
            }
        }
    </style>
'''

# Pages to update
pages = ['about.html', 'menu.html', 'wine.html', 'gallery.html', 'contact.html', 
         'terms.html', 'privacy.html', 'sitemap.html']

for page in pages:
    try:
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if modal already exists
        if 'reservationModal' in content:
            print(f"⚠ {page} - Modal already exists, skipping")
            continue
        
        # Find the closing </body> tag
        body_close_pos = content.rfind('</body>')
        if body_close_pos == -1:
            print(f"✗ {page} - </body> tag not found")
            continue
        
        # Insert modal, CSS and JS before </body>
        new_content = (
            content[:body_close_pos] + 
            '\n    ' + modal_html + 
            '\n\n' + modal_css +
            '\n' + modal_js + 
            '\n</body>' + 
            content[body_close_pos + 7:]
        )
        
        # Write updated content
        with open(page, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✓ {page} - Modal and JavaScript added")
        
    except Exception as e:
        print(f"✗ {page} - Error: {str(e)}")

print("\n✓✓✓ All pages updated with reservation modal!")
