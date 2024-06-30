from typing import Type
from django.db.models.signals import post_save
from django.dispatch import receiver

from location.models import EventModel, LatitudeModel, LongitudeModel
from location.utils.utils import get_nearest_instance


@receiver(post_save, sender=EventModel)
def add_lat_long_event_model(
    sender: Type[EventModel], instance: EventModel, created: bool, **kwargs
):
    """
    A pre_save signal to get the nearest latitude and longitude.[]
    """
    breakpoint()
    if created:
        latitude = get_nearest_instance(instance.occurrence_time, LatitudeModel)
        longitude = get_nearest_instance(instance.occurrence_time, LongitudeModel)
        instance.longitude = longitude
        instance.latitude = latitude
        instance.save(update_fields=['latitude', 'longitude'])
