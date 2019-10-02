from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('register/', include('plaython.urls')),
    path('admin/', admin.site.urls),
]
