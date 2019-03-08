from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('playton/', include('playton.urls')),
    path('admin/', admin.site.urls),
]
