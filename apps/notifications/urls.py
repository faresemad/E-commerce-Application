from django.urls import path

from apps.notifications.views import test

urlpatterns = [
    path("test/", test, name="test"),
]
