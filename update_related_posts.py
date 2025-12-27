import re

# The new related posts section from blog-post-1
new_related_posts = '''
            </div>

            <!-- Related Posts -->
            <div style="margin-top: 5rem;">
                <h2 style="font-family: 'Montserrat', sans-serif; font-size: clamp(2rem, 4vw, 2.5rem); font-weight: 700; color: #D4AF37; margin-bottom: 3rem; text-align: center;">Слични Чланци</h2>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
                    
                    <!-- Related Post 1 -->
                    <a href="blog-post-2.html" style="text-decoration: none; color: inherit; display: block; background: linear-gradient(135deg, rgba(30,22,15,0.5) 0%, rgba(40,30,20,0.5) 100%); border: 1px solid rgba(212,175,55,0.15); border-radius: 20px; overflow: hidden; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); position: relative;" onmouseover="this.style.transform='translateY(-8px)'; this.style.boxShadow='0 12px 40px rgba(212,175,55,0.25)'; this.style.borderColor='rgba(212,175,55,0.4)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none'; this.style.borderColor='rgba(212,175,55,0.15)'">
                        <div style="position: relative; overflow: hidden;">
                            <img src="images/kako-je-pocela-nasa-prica.jpg" alt="Restoran" style="width: 100%; height: 220px; object-fit: cover; transition: transform 0.4s;" onerror="this.src='images/restoran zlatar.jpg'" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                            <div style="position: absolute; top: 1rem; left: 1rem;">
                                <span style="display: inline-block; padding: 0.5rem 1rem; background: rgba(20,15,10,0.9); backdrop-filter: blur(10px); border: 1px solid rgba(212,175,55,0.3); border-radius: 50px; color: #D4AF37; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; font-family: 'Montserrat', sans-serif;">Приче</span>
                            </div>
                        </div>
                        <div style="padding: 1.75rem;">
                            <h3 style="font-family: 'Montserrat', sans-serif; font-size: 1.375rem; color: #fff; margin-bottom: 0.875rem; font-weight: 700; line-height: 1.3;">Како је почела наша прича</h3>
                            <p style="color: rgba(255,255,255,0.7); font-size: 0.9375rem; line-height: 1.6; margin-bottom: 1.25rem;">Пре четири деценије, у малом локалу у центру Београда...</p>
                            <div style="display: flex; align-items: center; gap: 1.25rem; color: rgba(255,255,255,0.5); font-size: 0.875rem; font-family: 'Montserrat', sans-serif;">
                                <span style="display: flex; align-items: center; gap: 0.375rem;"><i class="fas fa-eye"></i> 1.9K</span>
                                <span style="display: flex; align-items: center; gap: 0.375rem;"><i class="fas fa-heart"></i> 287</span>
                            </div>
                        </div>
                    </a>

                    <!-- Related Post 2 -->
                    <a href="blog-post-3.html" style="text-decoration: none; color: inherit; display: block; background: linear-gradient(135deg, rgba(30,22,15,0.5) 0%, rgba(40,30,20,0.5) 100%); border: 1px solid rgba(212,175,55,0.15); border-radius: 20px; overflow: hidden; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); position: relative;" onmouseover="this.style.transform='translateY(-8px)'; this.style.boxShadow='0 12px 40px rgba(212,175,55,0.25)'; this.style.borderColor='rgba(212,175,55,0.4)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none'; this.style.borderColor='rgba(212,175,55,0.15)'">
                        <div style="position: relative; overflow: hidden;">
                            <img src="images/ajvar-domaci.jpg" alt="Ajvar" style="width: 100%; height: 220px; object-fit: cover; transition: transform 0.4s;" onerror="this.src='images/restoran zlatar.jpg'" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                            <div style="position: absolute; top: 1rem; left: 1rem;">
                                <span style="display: inline-block; padding: 0.5rem 1rem; background: rgba(20,15,10,0.9); backdrop-filter: blur(10px); border: 1px solid rgba(212,175,55,0.3); border-radius: 50px; color: #D4AF37; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; font-family: 'Montserrat', sans-serif;">Рецепти</span>
                            </div>
                        </div>
                        <div style="padding: 1.75rem;">
                            <h3 style="font-family: 'Montserrat', sans-serif; font-size: 1.375rem; color: #fff; margin-bottom: 0.875rem; font-weight: 700; line-height: 1.3;">Ајвар - злато српске кухиње</h3>
                            <p style="color: rgba(255,255,255,0.7); font-size: 0.9375rem; line-height: 1.6; margin-bottom: 1.25rem;">Домаћи ајвар по старом рецепту који се преноси генерацијама...</p>
                            <div style="display: flex; align-items: center; gap: 1.25rem; color: rgba(255,255,255,0.5); font-size: 0.875rem; font-family: 'Montserrat', sans-serif;">
                                <span style="display: flex; align-items: center; gap: 0.375rem;"><i class="fas fa-eye"></i> 1.8K</span>
                                <span style="display: flex; align-items: center; gap: 0.375rem;"><i class="fas fa-heart"></i> 312</span>
                            </div>
                        </div>
                    </a>

                    <!-- Related Post 3 -->
                    <a href="blog-post-4.html" style="text-decoration: none; color: inherit; display: block; background: linear-gradient(135deg, rgba(30,22,15,0.5) 0%, rgba(40,30,20,0.5) 100%); border: 1px solid rgba(212,175,55,0.15); border-radius: 20px; overflow: hidden; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); position: relative;" onmouseover="this.style.transform='translateY(-8px)'; this.style.boxShadow='0 12px 40px rgba(212,175,55,0.25)'; this.style.borderColor='rgba(212,175,55,0.4)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none'; this.style.borderColor='rgba(212,175,55,0.15)'">
                        <div style="position: relative; overflow: hidden;">
                            <img src="images/sarma-domaca.jpg" alt="Sarma" style="width: 100%; height: 220px; object-fit: cover; transition: transform 0.4s;" onerror="this.src='images/restoran zlatar.jpg'" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                            <div style="position: absolute; top: 1rem; left: 1rem;">
                                <span style="display: inline-block; padding: 0.5rem 1rem; background: rgba(20,15,10,0.9); backdrop-filter: blur(10px); border: 1px solid rgba(212,175,55,0.3); border-radius: 50px; color: #D4AF37; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; font-family: 'Montserrat', sans-serif;">Рецепти</span>
                            </div>
                        </div>
                        <div style="padding: 1.75rem;">
                            <h3 style="font-family: 'Montserrat', sans-serif; font-size: 1.375rem; color: #fff; margin-bottom: 0.875rem; font-weight: 700; line-height: 1.3;">Сарма која се топи у устима</h3>
                            <p style="color: rgba(255,255,255,0.7); font-size: 0.9375rem; line-height: 1.6; margin-bottom: 1.25rem;">Рецепт наше бакице који је освојио срца хиљада гостију...</p>
                            <div style="display: flex; align-items: center; gap: 1.25rem; color: rgba(255,255,255,0.5); font-size: 0.875rem; font-family: 'Montserrat', sans-serif;">
                                <span style="display: flex; align-items: center; gap: 0.375rem;"><i class="fas fa-eye"></i> 2.1K</span>
                                <span style="display: flex; align-items: center; gap: 0.375rem;"><i class="fas fa-heart"></i> 345</span>
                            </div>
                        </div>
                    </a>

                </div>
            </div>

        </div>
    </section>
'''

# Process blog posts 2-12
for i in range(2, 13):
    filename = f'blog-post-{i}.html'
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace Related Posts section
        # Pattern from </div> before Related Posts comment to end of </section>
        pattern = r'</div>\s+<!-- Related Posts -->.*?</div>\s+</section>'
        content = re.sub(pattern, new_related_posts, content, flags=re.DOTALL)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f'✅ Updated related posts in {filename}')
    except Exception as e:
        print(f'❌ Error: {e}')

print('\n✨ All blog posts now have matching related posts style!')
