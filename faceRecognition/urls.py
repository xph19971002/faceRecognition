from django.conf.urls import url
from django.contrib import admin

# from django.urls import path
from apps.main import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    url('admin/', admin.site.urls),
    url('index/', views.index),
]
