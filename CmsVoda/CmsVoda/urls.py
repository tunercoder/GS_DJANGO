from django.contrib import admin
from django.urls import path,include
from core import urls as coreurls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(coreurls)),
]