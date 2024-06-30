from django.urls import path

from location.views import EventModelListAPIView, EventModelRetrieveAPIView

urlpatterns = [
    path('', EventModelListAPIView.as_view()),
    path('<str:pk>', EventModelRetrieveAPIView.as_view()),
]
