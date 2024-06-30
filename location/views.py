from rest_framework.generics import ListAPIView, RetrieveAPIView

from location.models import EventModel
from location.serializers import EventModelSerializer


class EventModelListAPIView(ListAPIView):
    """Generic View to list all event model objects."""

    queryset = EventModel.objects.all()
    serializer_class = EventModelSerializer


class EventModelRetrieveAPIView(RetrieveAPIView):
    """Generic View to get Event Model object by id."""

    queryset = EventModel.objects.all()
    serializer_class = EventModelSerializer
