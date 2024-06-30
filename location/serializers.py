from rest_framework.serializers import ModelSerializer

from location.models import EventModel, LatitudeModel, LongitudeModel


class LatitudeModelSerializer(ModelSerializer):
    class Meta:
        model = LatitudeModel
        fields = "__all__"


class LongitudeModelSerializer(ModelSerializer):
    class Meta:
        model = LongitudeModel
        fields = "__all__"


class EventModelSerializer(ModelSerializer):
    latitude = LatitudeModelSerializer(many=False, read_only=True)
    longitude = LongitudeModelSerializer(many=False, read_only=True)

    class Meta:
        model = EventModel
        fields = "__all__"
