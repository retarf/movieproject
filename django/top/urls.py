from django.urls import path

from . import api

app_name = 'top'
urlpatterns = [
    path('', api.TopView.as_view(), name='index'),
]
