from typing import Type
from django.db.models.signals import post_save
from django.dispatch import receiver

from location.models import EventModel, LatitudeModel, LongitudeModel
from location.utils.utils import get_nearest_instance


@receiver(post_save, sender=EventModel)
def create_user_profile(
    created: bool, sender: Type[EventModel], instance: EventModel, *args, **kwargs
):
    """
    A pre_save signal to get the nearest latitude and longitude.[]
    """
    if created:
        latitude = get_nearest_instance(instance.occurrence_time, LatitudeModel)
        longitude = get_nearest_instance(instance.occurrence_time, LongitudeModel)
        instance.longitude = longitude
        instance.latitude = latitude
