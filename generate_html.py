import os
import django
from django.template.loader import render_to_string

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CulturalCompass.settings')
django.setup()

html_content = render_to_string('index.html')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML")