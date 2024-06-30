from django.db import migrations
from django.apps.registry import Apps
from django.conf import settings

from location.utils.utils import populate_event_models


def load_event_data(apps:Apps, _):
    Event = apps.get_model("location", "EventModel")

    json_file_path = f"{settings.BASE_DIR}\\events.json"
    populate_event_models(json_file_path, Event)
    

class Migration(migrations.Migration):

    dependencies = [
        ('location', '0006_eventmodel_latitude_eventmodel_longitude'),
    ]

    operations = [
        migrations.RunPython(load_event_data)
    ]
