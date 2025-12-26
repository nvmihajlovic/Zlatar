import codecs
import re

# Листа фајлова
files = [f'blog-post-{i}.html' for i in range(1, 13)]

for filename in files:
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        modified = False
        
        # Уклони некомплетан <script тег пре </style>
        # Тражи pattern: </style>\n\n    <script\n<body>
        pattern = r'(</style>)\s*<script\s*\n(<body>)'
        if re.search(pattern, content):
            content = re.sub(pattern, r'\1\n</head>\n\n\2', content)
            print(f"✓ Уклоњен некомплетан <script> тег у {filename}")
            modified = True
        
        # Провери да ли постоји </head> тег, ако не, додај га после </style>
        if '</head>' not in content and '</style>' in content:
            content = content.replace('</style>', '</style>\n</head>', 1)
            print(f"✓ Додат </head> тег у {filename}")
            modified = True
        
        if modified:
            # Запиши ажуриран садржај
            with codecs.open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ {filename} поправљен\n")
        else:
            print(f"⏭ {filename} је у реду\n")
            
    except FileNotFoundError:
        print(f"✗ Није пронађено: {filename}")
    except Exception as e:
        print(f"✗ Грешка у {filename}: {str(e)}")

print("\n🎉 ЗАВРШЕНО! Поправљени некомплетни <script> тагови!")
