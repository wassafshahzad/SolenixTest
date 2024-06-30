from django.db import migrations
from django.apps.registry import Apps
from django.conf import settings

from location.utils.utils import populate_position_models


def load_latitude_data(apps:Apps, _):
    Latitude = apps.get_model("location", "LatitudeModel")

    json_file_path = f"{settings.BASE_DIR}/latitudes.json"
    populate_position_models(json_file_path, Latitude)

class Migration(migrations.Migration):

    dependencies = [
        ("location", "0003_eventmodel"),
    ]

    operations = [
        migrations.RunPython(load_latitude_data),
    ]
