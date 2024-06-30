from django.db import migrations
from django.apps.registry import Apps
from django.conf import settings

from location.utils.utils import populate_position_models


def load_longitude_data(apps:Apps, _):
    Longitude = apps.get_model("location", "LongitudeModel")

    json_file_path = f"{settings.BASE_DIR}\\longitudes.json"
    populate_position_models(json_file_path, Longitude)

class Migration(migrations.Migration):

    dependencies = [
        ('location', '0004_populate_latitude'),
    ]

    operations = [
        migrations.RunPython(load_longitude_data),
    ]

