import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.test import Client
import re

c = Client(SERVER_NAME='127.0.0.1')

# Test User Login
print('--- USER LOGIN POST ---')
r = c.post('/login/', {'username': 'wronguser', 'password': 'wrongpassword'})
html = r.content.decode('utf-8')
match = re.search(r'<div class="mb-4">.*?</div>\s*</div>', html, re.DOTALL)
if match:
    print(match.group(0))
else:
    print('No message block found.')

# Test Admin Login
print('\n--- ADMIN LOGIN POST ---')
r_admin = c.post('/admin-login/', {'admin_id': 'wrongadmin', 'admin_password': 'wrongpassword'})
html_admin = r_admin.content.decode('utf-8')
match_admin = re.search(r'<div class="mb-4">.*?</div>\s*</div>', html_admin, re.DOTALL)
if match_admin:
    print(match_admin.group(0))
else:
    print('No message block found.')
