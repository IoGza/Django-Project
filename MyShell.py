import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","learning_log.settings")

import django
django.setup()

from MainApp.models import Topic, Entry

topics = Topic.objects.all()
entries = Entry.objects.all()

t = Topic.objects.get(id=1)

print(t)

entries = t.entry_set.all()

for entry in entries:
    print(entry)

'''
for t in topics:
    print(f"Topic ID: {t.id} Topic: {t}")

for e in entries:
    print(f"Topic: {e.topic} ")
    print(f"Text: {e}")
    print(f"Date Added: {e.date_added}")
'''