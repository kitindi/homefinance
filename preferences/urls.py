from django.urls import reverse, path
from . import views


urlpatterns = [
    path("", views.preferences, name='preferences')
]
