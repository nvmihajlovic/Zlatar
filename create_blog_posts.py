# -*- coding: utf-8 -*-
import codecs

posts = [
    {'id': 2, 'category': 'Рецепти', 'title': 'Тајна савршеног ћевапа: Рецепт из златарског краја', 'date': '18. Децембар 2025', 'time': '7 мин', 'image': 'images/galerija/1-1-scaled.jpg', 'views': '2,156', 'likes': '187', 'breadcrumb': 'Тајна савршеног ћевапа'},
    {'id': 3, 'category': 'Догађаји', 'title': 'Новогодишња прослава 2026: Резервишите своје место', 'date': '15. Децембар 2025', 'time': '4 мин', 'image': 'images/galerija/2-scaled.jpg', 'views': '3,842', 'likes': '312', 'breadcrumb': 'Новогодишња прослава'},
    {'id': 4, 'category': 'Кухиња', 'title': 'Печење испод сача: Древна уметност припреме', 'date': '12. Децембар 2025', 'time': '6 мин', 'image': 'images/galerija/3-scaled.jpg', 'views': '987', 'likes': '76', 'breadcrumb': 'Печење испод сача'},
    {'id': 5, 'category': 'Вино', 'title': 'Водич кроз нашу винску карту: Одаберите савршено вино', 'date': '10. Децембар 2025', 'time': '8 мин', 'image': 'images/galerija/217-scaled.jpg', 'views': '1,532', 'likes': '124', 'breadcrumb': 'Водич кроз винску карту'},
    {'id': 6, 'category': 'Прича', 'title': 'Упознајте нашу екипу: Људи иза успеха', 'date': '8. Децембар 2025', 'time': '5 мин', 'image': 'images/galerija/224-scaled.jpg', 'views': '1,876', 'likes': '142', 'breadcrumb': 'Упознајте нашу екипу'},
    {'id': 7, 'category': 'Састојци', 'title': 'Од фарме до трпезе: Наш приступ квалитету', 'date': '5. Децембар 2025', 'time': '6 мин', 'image': 'images/galerija/img-098b22a2367eae445a03494a392e46e7-v.jpg', 'views': '765', 'likes': '58', 'breadcrumb': 'Од фарме до трпезе'},
    {'id': 8, 'category': 'Музика', 'title': 'Жива музика сваке вечери: Традиција која живи', 'date': '3. Децембар 2025', 'time': '4 мин', 'image': 'images/galerija/img-48cfa936b74b8d1ff2188661bc4dd709-v.jpg', 'views': '2,341', 'likes': '198', 'breadcrumb': 'Жива музика'},
    {'id': 9, 'category': 'Сезонски', 'title': 'Зимски специјалитети: Топлина у сваком залогају', 'date': '1. Децембар 2025', 'time': '5 мин', 'image': 'images/galerija/img-5d4f7c20062472de7ac4f6fdf6d1887f-v.jpg', 'views': '1,432', 'likes': '116', 'breadcrumb': 'Зимски специјалитети'},
    {'id': 10, 'category': 'Десерт', 'title': 'Слатка страна традиције: Домаћи десерти', 'date': '28. Новембар 2025', 'time': '4 мин', 'image': 'images/galerija/img-71edaeea36f3b089187271a6f021c1c1-v.jpg', 'views': '1,654', 'likes': '134', 'breadcrumb': 'Слатка страна традиције'},
    {'id': 11, 'category': 'Породица', 'title': 'Породичне прославе у Златару: Простор за успомене', 'date': '25. Новембар 2025', 'time': '6 мин', 'image': 'images/galerija/img-b2dd35aa556646c608ff962e5104da5c-v.jpg', 'views': '892', 'likes': '67', 'breadcrumb': 'Породичне прославе'},
    {'id': 12, 'category': 'Историја', 'title': 'Београдска гастрономија кроз деценије', 'date': '22. Новембар 2025', 'time': '9 мин', 'image': 'images/galerija/img-da99f9fabb0f918b15accba619a1d555-v.jpg', 'views': '1,123', 'likes': '89', 'breadcrumb': 'Београдска гастрономија'}
]

# Read template
with codecs.open('blog-post-1.html', 'r', 'utf-8') as f:
    template = f.read()

# Create blog posts
for post in posts:
    content = template
    content = content.replace('blog-post-1.html', f"blog-post-{post['id']}.html")
    content = content.replace('Четрдесет година традиције и гостољубивости - Ресторан Златар', f"{post['title']} - Ресторан Златар")
    content = content.replace('images/galerija/019-scaled.jpg', post['image'])
    content = content.replace('<span class="blog-hero__category">Традиција</span>', f'<span class="blog-hero__category">{post["category"]}</span>')
    content = content.replace('<h1 class="blog-hero__title">Четрдесет година традиције и гостољубивости</h1>', f'<h1 class="blog-hero__title">{post["title"]}</h1>')
    content = content.replace('<span>Четрдесет година традиције</span>', f'<span>{post["breadcrumb"]}</span>')
    content = content.replace('<span>20. Децембар 2025</span>', f'<span>{post["date"]}</span>')
    content = content.replace('<span>5 мин читања</span>', f'<span>{post["time"]} читања</span>')
    content = content.replace('<span>1,247 прегледа</span>', f'<span>{post["views"]} прегледа</span>')
    content = content.replace('<span>89 лајкова</span>', f'<span>{post["likes"]} лајкова</span>')
    
    # Write file
    with codecs.open(f'blog-post-{post["id"]}.html', 'w', 'utf-8') as f:
        f.write(content)
    
    print(f"Креирано: blog-post-{post['id']}.html")

print("\nСви blog post фајлови су успешно креирани!")
