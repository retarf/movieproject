from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    path('comments/', include('comments.urls')),
    path('top/', include('top.urls')),
]
