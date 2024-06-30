"""Utility file for helper functions."""

import json
from datetime import datetime
from typing import Type
from django.db import transaction
from django.db.models import F, ExpressionWrapper, DurationField

from location.models import PositionModel, EventModel, LatitudeModel, LongitudeModel


def populate_position_models(json_file_path: str, model: Type[PositionModel]):
    """Populate PositionModel using json files

    Args:
        json_file_path: Path to json file.
        model: class of PositionModel or its children.
    """

    with open(json_file_path, "r") as file:
        data = json.load(file)
        instances = []
        for entry in data:
            timestamp_str = entry["timestamp"]
            timestamp = datetime.fromisoformat(timestamp_str)
            position = entry["position"]
            instances.append(model(timestamp=timestamp, position=position))

        with transaction.atomic():
            model.objects.bulk_create(instances)


def populate_event_models(json_file_path: str, model: Type[EventModel]):
    """Populate EventModel using json files

    Args:
        json_file_path: Path to json file.
        model: class of EventModel.
    """

    with open(json_file_path, "r") as file:
        data = json.load(file)
        instances = []
        for entry in data:
            instance = model(**entry)
            instances.append(instance)
        with transaction.atomic():
            model.objects.bulk_create(instances)


def get_nearest_instance(
    target_datetime: datetime, model: Type[PositionModel]
) -> PositionModel:
    """Get nearest instance of a PositionModel.
    Args:
        model: class of PositionModel or its children.
        target_datetime: datetime object to match object.
    Returns:
        PositionModel: Instance of nearest PositionModel.
    """

    nearest_entry = (
        model.objects.annotate(
            time_diff=ExpressionWrapper(
                F("timestamp") - target_datetime, output_field=DurationField()
            )
        )
        .order_by("time_diff")
        .first()
    )

    return nearest_entry


def add_lang_lot(model: Type[EventModel]):
    """Add latitude and longitude instances based on the nearest position
    Args:
        model: A class object of EventMode.
    """

    instances = []
    for instance in model.objects.all():
        instance.latitude = get_nearest_instance(
            instance.occurrence_time, LatitudeModel
        )
        instance.longitude = get_nearest_instance(
            instance.occurrence_time, LongitudeModel
        )
        instances.append(instance)
    with transaction.atomic():
        model.objects.bulk_update(instances, fields=["latitude", "longitude"])
