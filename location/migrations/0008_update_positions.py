# Generated by Django 5.0.6 on 2024-06-30 01:26

from django.db import migrations
from django.apps.registry import Apps

from location.utils.utils import add_lang_lot
from location.models import EventModel

"""
We use a real model instead of a historical model we are assigning to a related field.
"""

class Migration(migrations.Migration):

    def update(apps:Apps, _):
        add_lang_lot(EventModel)

    dependencies = [
        ('location', '0007_populate_events'),
    ]

    operations = [
        migrations.RunPython(update)
    ]
