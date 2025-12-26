import codecs
import re

# HTML за резервациони модал
modal_html = '''    <!-- Reservation Modal -->
    <div class="modal" id="reservationModal">
        <div class="modal-overlay" id="modalOverlay"></div>
        <div class="modal-content">
            <button class="modal-close" id="modalClose">
                <i class="fas fa-times"></i>
            </button>
            
            <div class="modal-header">
                <i class="fas fa-calendar-check"></i>
                <h2>Резервација стола</h2>
                <p>Попуните формулар и потврдићемо вашу резервацију</p>
            </div>
            
            <form class="reservation-form" id="reservationForm">
                <div class="form-row">
                    <div class="form-group">
                        <input type="text" id="resName" class="form-input" placeholder=" " required>
                        <label for="resName" class="form-label">Име и презиме</label>
                    </div>
                    
                    <div class="form-group">
                        <input type="tel" id="resPhone" class="form-input" placeholder=" " required>
                        <label for="resPhone" class="form-label">Телефон</label>
                    </div>
                </div>
                
                <div class="form-row">
                    <div class="form-group">
                        <input type="date" id="resDate" class="form-input" placeholder=" " required>
                        <label for="resDate" class="form-label">Датум</label>
                    </div>
                    
                    <div class="form-group">
                        <input type="time" id="resTime" class="form-input" placeholder=" " required>
                        <label for="resTime" class="form-label">Време</label>
                    </div>
                </div>
                
                <div class="form-group">
                    <select id="resGuests" class="form-input" required>
                        <option value="">Број особа</option>
                        <option value="1">1 особа</option>
                        <option value="2">2 особе</option>
                        <option value="3">3 особе</option>
                        <option value="4">4 особе</option>
                        <option value="5">5 особа</option>
                        <option value="6">6 особа</option>
                        <option value="7">7 особа</option>
                        <option value="8">8 особа</option>
                        <option value="more">Више од 8</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <textarea id="resNote" class="form-input" rows="3" placeholder=" "></textarea>
                    <label for="resNote" class="form-label">Напомена (опционално)</label>
                </div>
                
                <button type="submit" class="btn btn-primary btn-full">
                    <span>Пошаљите резервацију</span>
                    <i class="fas fa-check"></i>
                </button>
            </form>
        </div>
    </div>

'''

# CSS за модал
modal_css = '''
        /* Modal Styles */
        .modal {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 10000;
            display: none;
            align-items: center;
            justify-content: center;
            padding: 1rem;
        }
        
        .modal.active {
            display: flex;
        }
        
        .modal-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.85);
            backdrop-filter: blur(8px);
            animation: fadeInModal 0.3s ease-out;
        }
        
        @keyframes fadeInModal {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        @keyframes modalSlideIn {
            from {
                opacity: 0;
                transform: scale(0.9) translateY(-20px);
            }
            to {
                opacity: 1;
                transform: scale(1) translateY(0);
            }
        }
        
        .modal-content {
            position: relative;
            background: linear-gradient(180deg, rgba(40, 30, 20, 0.98) 0%, rgba(30, 22, 15, 0.98) 100%);
            border-radius: 24px;
            padding: 3rem;
            max-width: 600px;
            width: 90%;
            max-height: 90vh;
            overflow-y: auto;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5), 0 0 100px rgba(212, 175, 55, 0.15);
            border: 1px solid rgba(212, 175, 55, 0.2);
            animation: modalSlideIn 0.4s cubic-bezier(0.16, 1, 0.3, 1);
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
        
        .form-input[type="date"] ~ .form-label,
        .form-input[type="time"] ~ .form-label {
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
'''

# JavaScript за модал
modal_js = '''
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
                
                console.log('Reservation data:', formData);
                alert('Хвала! Ваша резервација је послата. Контактираћемо вас ускоро за потврду.');
                
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
'''

# Листа фајлова
files = ['blog.html'] + [f'blog-post-{i}.html' for i in range(1, 13)]

for filename in files:
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        modified = False
        
        # 1. Додај модал HTML пре затварајућег </body>
        if 'id="reservationModal"' not in content:
            content = content.replace('</body>', modal_html + '\n</body>')
            print(f"✓ Додат reservation modal HTML у {filename}")
            modified = True
        
        # 2. Додај CSS пре последњег </style>
        if '.modal-content {' not in content:
            # Пронађи последњи </style> тег
            last_style_pos = content.rfind('</style>')
            if last_style_pos != -1:
                content = content[:last_style_pos] + modal_css + '\n    </style>' + content[last_style_pos+8:]
                print(f"✓ Додат reservation modal CSS у {filename}")
                modified = True
        
        # 3. Додај JavaScript пре последњег </script> пре </body>
        if 'btnReserve.addEventListener' not in content or 'reservationModal.classList.add' not in content:
            # Пронађи последњи </script> пре </body>
            body_pos = content.rfind('</body>')
            script_search = content[:body_pos].rfind('</script>')
            if script_search != -1:
                content = content[:script_search] + modal_js + '\n    </script>' + content[script_search+9:]
                print(f"✓ Додат reservation modal JavaScript у {filename}")
                modified = True
        
        if modified:
            with codecs.open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
        else:
            print(f"⏭ {filename} већ има reservation modal")
            
    except FileNotFoundError:
        print(f"✗ Није пронађено: {filename}")
    except Exception as e:
        print(f"✗ Грешка у {filename}: {str(e)}")

print("\nЗавршено! Reservation modal додат на blog.html и све blog-post странице.")
