from django.db import models


class PositionModel(models.Model):
    timestamp = models.DateTimeField()
    position = models.FloatField()

    class Meta:
        abstract = True


class LatitudeModel(PositionModel):

    def __str__(self) -> str:
        return f"Latitude at {self.timestamp}: {self.position}"


class LongitudeModel(PositionModel):

    def __str__(self) -> str:
        return f"Longitude at {self.timestamp}: {self.position}"


class EventModel(models.Model):

    class SeverityLevels(models.TextChoices):
        ERROR = "Error"
        INFO = "Info"
        WARNING = "Warning"

    id = models.CharField(max_length=255, primary_key=True)
    occurrence_time = models.DateTimeField()
    event_name = models.CharField(max_length=255)
    severity = models.CharField(
        choices=SeverityLevels.choices, max_length=10, default=SeverityLevels.INFO
    )
    longitude = models.ForeignKey(
        LongitudeModel,
        related_name="events_lt",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    latitude = models.ForeignKey(
        LatitudeModel,
        related_name="events_ln",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
