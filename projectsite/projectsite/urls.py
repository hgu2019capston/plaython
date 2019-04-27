from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('plaython/', include('plaython.urls')),
    path('admin/', admin.site.urls),
]
