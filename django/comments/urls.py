from django.urls import path

from . import api

app_name='comments'
urlpatterns = [
    path('', api.CommentView.as_view(), name='index'),
]
