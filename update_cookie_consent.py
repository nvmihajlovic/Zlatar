import re
import os

# Stranice koje treba ažurirati (bez index.html koja već ima pravi consent)
pages = [
    'about.html',
    'menu.html', 
    'wine.html',
    'gallery.html',
    'contact.html',
    'sitemap.html'
]

# Napredni cookie consent HTML
advanced_cookie_consent_html = '''    <!-- Cookie Consent Banner -->
    <div class="cookie-consent" id="cookieConsent">
        <div class="cookie-header" style="display: flex; align-items: center; gap: 1.5rem; margin-bottom: 1.5rem;">
            <div class="cookie-icon" style="width: 60px; height: 60px; background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%); border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 1.75rem; color: #1a1410; box-shadow: 0 8px 24px rgba(212, 175, 55, 0.3); flex-shrink: 0;">
                <i class="fas fa-cookie-bite"></i>
            </div>
            <div>
                <h4 data-i18n="cookie.title" style="font-family: 'Montserrat', sans-serif; font-size: 1.35rem; font-weight: 700; color: #D4AF37; margin: 0 0 0.5rem 0;">Подешавање колачића</h4>
                <p style="font-family: 'Montserrat', sans-serif; font-size: 0.95rem; line-height: 1.6; color: rgba(255, 255, 255, 0.75); margin: 0;">
                    <span data-i18n="cookie.description">Изаберите које врсте колачића желите да прихватите.</span> <a href="privacy.html" style="color: #FFD700; text-decoration: none; font-weight: 600; border-bottom: 1px solid transparent; transition: all 0.3s;"><span data-i18n="cookie.learn_more">Сазнајте више</span></a>
                </p>
            </div>
        </div>
        
        <div class="cookie-categories" style="display: flex; flex-direction: column; gap: 1rem; margin-bottom: 1.5rem;">
            <!-- Neophodni kolacici -->
            <div class="cookie-category" style="display: flex; justify-content: space-between; align-items: center; padding: 1rem 1.25rem; background: rgba(255, 255, 255, 0.05); border-radius: 12px; border: 1px solid rgba(255, 255, 255, 0.08);">
                <div style="flex: 1;">
                    <h5 style="font-family: 'Montserrat', sans-serif; font-size: 1rem; font-weight: 600; color: rgba(255, 255, 255, 0.9); margin: 0 0 0.25rem 0;">
                        <i class="fas fa-shield-alt" style="color: #D4AF37; margin-right: 0.5rem; font-size: 0.9rem;"></i>
                        <span data-i18n="cookie.essential.title">Неопходни колачићи</span>
                    </h5>
                    <p data-i18n="cookie.essential.description" style="font-family: 'Montserrat', sans-serif; font-size: 0.85rem; color: rgba(255, 255, 255, 0.6); margin: 0; line-height: 1.5;">Омогућавају основне функције сајта (навигација, безбедност)</p>
                </div>
                <div style="margin-left: 1rem;">
                    <span data-i18n="cookie.essential.always" style="font-family: 'Montserrat', sans-serif; font-size: 0.75rem; font-weight: 600; color: rgba(255, 255, 255, 0.5); text-transform: uppercase; letter-spacing: 0.05em;">Увек укључени</span>
                </div>
            </div>
            
            <!-- Analiticki kolacici -->
            <div class="cookie-category" style="display: flex; justify-content: space-between; align-items: center; padding: 1rem 1.25rem; background: rgba(255, 255, 255, 0.05); border-radius: 12px; border: 1px solid rgba(255, 255, 255, 0.08);">
                <div style="flex: 1;">
                    <h5 style="font-family: 'Montserrat', sans-serif; font-size: 1rem; font-weight: 600; color: rgba(255, 255, 255, 0.9); margin: 0 0 0.25rem 0;">
                        <i class="fas fa-chart-line" style="color: #D4AF37; margin-right: 0.5rem; font-size: 0.9rem;"></i>
                        <span data-i18n="cookie.analytics.title">Аналитички колачићи</span>
                    </h5>
                    <p data-i18n="cookie.analytics.description" style="font-family: 'Montserrat', sans-serif; font-size: 0.85rem; color: rgba(255, 255, 255, 0.6); margin: 0; line-height: 1.5;">Помажу нам да разумемо како користите сајт (Google Analytics)</p>
                </div>
                <label class="cookie-switch" style="margin-left: 1rem;">
                    <input type="checkbox" id="analyticsConsent" checked>
                    <span class="cookie-slider"></span>
                </label>
            </div>
            
            <!-- Funkcionalni kolacici -->
            <div class="cookie-category" style="display: flex; justify-content: space-between; align-items: center; padding: 1rem 1.25rem; background: rgba(255, 255, 255, 0.05); border-radius: 12px; border: 1px solid rgba(255, 255, 255, 0.08);">
                <div style="flex: 1;">
                    <h5 style="font-family: 'Montserrat', sans-serif; font-size: 1rem; font-weight: 600; color: rgba(255, 255, 255, 0.9); margin: 0 0 0.25rem 0;">
                        <i class="fas fa-cog" style="color: #D4AF37; margin-right: 0.5rem; font-size: 0.9rem;"></i>
                        <span data-i18n="cookie.functional.title">Функционални колачићи</span>
                    </h5>
                    <p data-i18n="cookie.functional.description" style="font-family: 'Montserrat', sans-serif; font-size: 0.85rem; color: rgba(255, 255, 255, 0.6); margin: 0; line-height: 1.5;">Памте ваше преференције (језик, тема, локација)</p>
                </div>
                <label class="cookie-switch" style="margin-left: 1rem;">
                    <input type="checkbox" id="functionalConsent" checked>
                    <span class="cookie-slider"></span>
                </label>
            </div>
            
            <!-- Marketing kolacici -->
            <div class="cookie-category" style="display: flex; justify-content: space-between; align-items: center; padding: 1rem 1.25rem; background: rgba(255, 255, 255, 0.05); border-radius: 12px; border: 1px solid rgba(255, 255, 255, 0.08);">
                <div style="flex: 1;">
                    <h5 style="font-family: 'Montserrat', sans-serif; font-size: 1rem; font-weight: 600; color: rgba(255, 255, 255, 0.9); margin: 0 0 0.25rem 0;">
                        <i class="fas fa-bullhorn" style="color: #D4AF37; margin-right: 0.5rem; font-size: 0.9rem;"></i>
                        <span data-i18n="cookie.marketing.title">Маркетиншки колачићи</span>
                    </h5>
                    <p data-i18n="cookie.marketing.description" style="font-family: 'Montserrat', sans-serif; font-size: 0.85rem; color: rgba(255, 255, 255, 0.6); margin: 0; line-height: 1.5;">Прате вас преко сајтова за персонализоване огласе</p>
                </div>
                <label class="cookie-switch" style="margin-left: 1rem;">
                    <input type="checkbox" id="marketingConsent">
                    <span class="cookie-slider"></span>
                </label>
            </div>
        </div>
        
        <div class="cookie-actions" style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
            <button class="btn-cookie-accept-all" id="acceptAllCookies" style="font-family: 'Montserrat', sans-serif; font-size: 0.95rem; font-weight: 600; padding: 0.875rem 1.75rem; border: none; border-radius: 12px; cursor: pointer; transition: all 0.3s; display: flex; align-items: center; gap: 0.5rem; background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%); color: #1a1410; box-shadow: 0 4px 16px rgba(212, 175, 55, 0.3); flex: 1;">
                <i class="fas fa-check-double"></i>
                <span data-i18n="cookie.accept_all">Прихвати све</span>
            </button>
            <button class="btn-cookie-save" id="saveCookiePreferences" style="font-family: 'Montserrat', sans-serif; font-size: 0.95rem; font-weight: 600; padding: 0.875rem 1.75rem; border: 1px solid rgba(212, 175, 55, 0.4); border-radius: 12px; cursor: pointer; transition: all 0.3s; display: flex; align-items: center; gap: 0.5rem; background: rgba(212, 175, 55, 0.1); color: #D4AF37; flex: 1;">
                <i class="fas fa-save"></i>
                <span data-i18n="cookie.save_preferences">Сачувај избор</span>
            </button>
            <button class="btn-cookie-decline-all" id="declineAllCookies" style="font-family: 'Montserrat', sans-serif; font-size: 0.95rem; font-weight: 600; padding: 0.875rem 1.5rem; border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; cursor: pointer; transition: all 0.3s; background: rgba(255, 255, 255, 0.05); color: rgba(255, 255, 255, 0.7);">
                <span data-i18n="cookie.decline_all">Само неопходни</span>
            </button>
        </div>
    </div>'''

# Napredni cookie consent CSS
advanced_cookie_consent_css = '''        .cookie-consent {
            position: fixed;
            bottom: 2rem;
            left: 50%;
            transform: translateX(-50%) translateY(150%);
            max-width: 700px;
            width: calc(100% - 2rem);
            background: linear-gradient(145deg, rgba(26, 20, 16, 0.98) 0%, rgba(43, 33, 15, 0.98) 100%);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(212, 175, 55, 0.3);
            border-radius: 24px;
            padding: 2rem;
            box-shadow: 
                0 20px 60px rgba(0, 0, 0, 0.5),
                0 8px 20px rgba(212, 175, 55, 0.15),
                inset 0 1px 0 rgba(255, 255, 255, 0.1);
            z-index: 10000;
            transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        }

        .cookie-consent.show {
            transform: translateX(-50%) translateY(0);
        }
        
        /* Toggle Switch */
        .cookie-switch {
            position: relative;
            display: inline-block;
            width: 50px;
            height: 26px;
            flex-shrink: 0;
        }
        
        .cookie-switch input {
            opacity: 0;
            width: 0;
            height: 0;
        }
        
        .cookie-slider {
            position: absolute;
            cursor: pointer;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: rgba(255, 255, 255, 0.15);
            border: 1px solid rgba(255, 255, 255, 0.2);
            transition: 0.3s;
            border-radius: 26px;
        }
        
        .cookie-slider:before {
            position: absolute;
            content: "";
            height: 18px;
            width: 18px;
            left: 3px;
            bottom: 3px;
            background-color: rgba(255, 255, 255, 0.7);
            transition: 0.3s;
            border-radius: 50%;
        }
        
        .cookie-switch input:checked + .cookie-slider {
            background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%);
            border-color: #D4AF37;
        }
        
        .cookie-switch input:checked + .cookie-slider:before {
            transform: translateX(24px);
            background-color: #1a1410;
        }
        
        /* Button Hovers */
        .btn-cookie-accept-all:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 24px rgba(212, 175, 55, 0.4);
        }
        
        .btn-cookie-save:hover {
            background: rgba(212, 175, 55, 0.2);
            border-color: rgba(212, 175, 55, 0.6);
        }
        
        .btn-cookie-decline-all:hover {
            background: rgba(255, 255, 255, 0.08);
            color: rgba(255, 255, 255, 0.9);
            border-color: rgba(255, 255, 255, 0.2);
        }

        @media (max-width: 768px) {
            .cookie-consent {
                bottom: 1rem;
                width: calc(100% - 1rem);
                padding: 1.5rem;
            }

            .cookie-header {
                flex-direction: column !important;
                text-align: center;
                gap: 1rem !important;
            }

            .cookie-actions {
                flex-direction: column;
            }

            .btn-cookie-accept-all,
            .btn-cookie-save,
            .btn-cookie-decline-all {
                width: 100%;
                justify-content: center;
            }

            .cookie-icon {
                width: 50px !important;
                height: 50px !important;
                font-size: 1.5rem !important;
            }
        }'''

# Napredni cookie consent JavaScript
advanced_cookie_consent_js = '''        // Cookie Consent Logic
        document.addEventListener('DOMContentLoaded', function() {
            const cookieConsent = document.getElementById('cookieConsent');
            const acceptAllBtn = document.getElementById('acceptAllCookies');
            const saveBtn = document.getElementById('saveCookiePreferences');
            const declineAllBtn = document.getElementById('declineAllCookies');
            
            const analyticsCheckbox = document.getElementById('analyticsConsent');
            const functionalCheckbox = document.getElementById('functionalConsent');
            const marketingCheckbox = document.getElementById('marketingConsent');

            // Check if user has already made a choice
            const cookiePreferences = localStorage.getItem('cookiePreferences');
            
            if (!cookiePreferences) {
                // Show banner after 1 second
                setTimeout(() => {
                    cookieConsent.classList.add('show');
                }, 1000);
            } else {
                // Load saved preferences
                const prefs = JSON.parse(cookiePreferences);
                analyticsCheckbox.checked = prefs.analytics;
                functionalCheckbox.checked = prefs.functional;
                marketingCheckbox.checked = prefs.marketing;
            }

            // Accept all cookies
            acceptAllBtn.addEventListener('click', function() {
                const preferences = {
                    necessary: true,
                    analytics: true,
                    functional: true,
                    marketing: true
                };
                localStorage.setItem('cookiePreferences', JSON.stringify(preferences));
                cookieConsent.classList.remove('show');
                initializeScripts(preferences);
                console.log('All cookies accepted');
            });

            // Save custom preferences
            saveBtn.addEventListener('click', function() {
                const preferences = {
                    necessary: true,
                    analytics: analyticsCheckbox.checked,
                    functional: functionalCheckbox.checked,
                    marketing: marketingCheckbox.checked
                };
                localStorage.setItem('cookiePreferences', JSON.stringify(preferences));
                cookieConsent.classList.remove('show');
                initializeScripts(preferences);
                console.log('Cookie preferences saved:', preferences);
            });

            // Decline all (only necessary)
            declineAllBtn.addEventListener('click', function() {
                const preferences = {
                    necessary: true,
                    analytics: false,
                    functional: false,
                    marketing: false
                };
                localStorage.setItem('cookiePreferences', JSON.stringify(preferences));
                cookieConsent.classList.remove('show');
                console.log('Only necessary cookies accepted');
            });
            
            // Initialize scripts based on preferences
            function initializeScripts(prefs) {
                if (prefs.analytics) {
                    // Initialize Google Analytics or other analytics
                    console.log('Analytics initialized');
                }
                if (prefs.functional) {
                    console.log('Functional cookies initialized');
                }
                if (prefs.marketing) {
                    console.log('Marketing cookies initialized');
                }
            }
        });'''

for page in pages:
    if not os.path.exists(page):
        print(f"⚠️ File {page} not found, skipping...")
        continue
    
    print(f"\n📄 Processing {page}...")
    
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace old cookie consent HTML
    # Pattern: <!-- Cookie Consent Banner --> ... </div> (end of consent div)
    old_consent_pattern = r'<!-- Cookie Consent Banner -->.*?<div class="cookie-consent".*?</div>\s*</div>'
    
    if re.search(old_consent_pattern, content, re.DOTALL):
        content = re.sub(old_consent_pattern, advanced_cookie_consent_html, content, flags=re.DOTALL)
        print(f"   ✅ Replaced cookie consent HTML")
    else:
        print(f"   ⚠️ Could not find old cookie consent HTML pattern")
    
    # Find and replace old cookie consent CSS
    old_css_pattern = r'\.cookie-consent\s*\{[^}]+position:\s*fixed;.*?@media\s*\(max-width:\s*768px\)[^}]*\{[^}]*\.cookie-consent\s*\{[^}]*\}.*?\}'
    
    if re.search(old_css_pattern, content, re.DOTALL):
        content = re.sub(old_css_pattern, advanced_cookie_consent_css, content, flags=re.DOTALL)
        print(f"   ✅ Replaced cookie consent CSS")
    else:
        # Try simpler pattern
        old_css_simple = r'\.cookie-consent\s*\{.*?(?=\n\s*(?:@media|\.(?!cookie)|</style>))'
        if re.search(old_css_simple, content, re.DOTALL):
            content = re.sub(old_css_simple, advanced_cookie_consent_css, content, flags=re.DOTALL)
            print(f"   ✅ Replaced cookie consent CSS (simple pattern)")
        else:
            print(f"   ⚠️ Could not find old cookie consent CSS pattern")
    
    # Find and replace old cookie consent JavaScript
    old_js_pattern = r'//\s*Cookie\s*Consent\s*Logic.*?const\s+cookieConsent\s*=.*?(?=\n\s*(?:document\.|window\.|const\s+\w+\s*=\s*document\.getElementById\((?!.*cookie)|</script>))'
    
    if re.search(old_js_pattern, content, re.DOTALL):
        content = re.sub(old_js_pattern, advanced_cookie_consent_js, content, flags=re.DOTALL)
        print(f"   ✅ Replaced cookie consent JavaScript")
    else:
        print(f"   ⚠️ Could not find old cookie consent JavaScript pattern")
    
    # Write updated content
    with open(page, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"   ✅ {page} updated successfully!")

print("\n✨ All pages updated with advanced cookie consent!")
