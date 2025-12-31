import re

# Read menu.html
with open('menu.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the simple cookie consent HTML - very specific pattern
old_cookie_html = r'<!-- Cookie Consent Banner -->\s*<div class="cookie-consent"[^>]*>\s*<p[^>]*>.*?privacy\.html.*?</p>\s*<div class="cookie-buttons"[^>]*>.*?</div>\s*</div>'

# New advanced cookie consent HTML (from update_cookie_consent.py)
new_cookie_html = '''    <!-- Cookie Consent Banner -->
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
                    <p data-i18n="cookie.marketing.description" style="font-family: 'Montserrat', sans-serif; font-size: 0.85rem; color: rgba(255, 255, 255, 0.6); margin: 0; line-height: 1.5;">Прилагођавају садржај и рекламе (социјалне мреже, маркетинг)</p>
                </div>
                <label class="cookie-switch" style="margin-left: 1rem;">
                    <input type="checkbox" id="marketingConsent" checked>
                    <span class="cookie-slider"></span>
                </label>
            </div>
        </div>
        
        <div class="cookie-actions" style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
            <button class="btn-cookie-accept-all" id="acceptAllBtn" style="flex: 1; min-width: 140px; background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%); color: #1a1410; font-weight: 700; padding: 0.875rem 1.75rem; border: none; border-radius: 50px; cursor: pointer; font-size: 0.95rem; transition: all 0.3s; box-shadow: 0 4px 16px rgba(212, 175, 55, 0.3); letter-spacing: 0.03em;">
                <i class="fas fa-check-circle" style="margin-right: 0.5rem;"></i>
                <span data-i18n="cookie.accept_all">Прихвати све</span>
            </button>
            <button class="btn-cookie-save" id="savePreferencesBtn" style="flex: 1; min-width: 140px; background: transparent; color: rgba(255, 255, 255, 0.85); font-weight: 600; padding: 0.875rem 1.75rem; border: 1.5px solid rgba(212, 175, 55, 0.4); border-radius: 50px; cursor: pointer; font-size: 0.95rem; transition: all 0.3s; letter-spacing: 0.03em;">
                <i class="fas fa-save" style="margin-right: 0.5rem;"></i>
                <span data-i18n="cookie.save_preferences">Сачувај избор</span>
            </button>
            <button class="btn-cookie-decline-all" id="declineAllBtn" style="flex: 0 0 auto; background: transparent; color: rgba(255, 255, 255, 0.5); font-weight: 500; padding: 0.875rem 1.5rem; border: 1.5px solid rgba(255, 255, 255, 0.15); border-radius: 50px; cursor: pointer; font-size: 0.9rem; transition: all 0.3s; letter-spacing: 0.03em;">
                <span data-i18n="cookie.decline_all">Одбиј све</span>
            </button>
        </div>
    </div>'''

# Replace HTML only if found
if re.search(old_cookie_html, content, re.DOTALL):
    content = re.sub(old_cookie_html, new_cookie_html, content, flags=re.DOTALL)
    print("✅ Replaced cookie consent HTML")
else:
    print("⚠️ Could not find old cookie consent HTML - may already be updated")

# Write back
with open('menu.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ menu.html cookie consent updated (HTML only - JS not touched)")
