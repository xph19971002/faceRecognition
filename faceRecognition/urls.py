from django.conf.urls import url
from django.contrib import admin
import xadmin
# from django.urls import path
from apps.main import views as v1
from apps.result import views as v2

urlpatterns = [
    # path('admin/', admin.site.urls),
    url('admin/', xadmin.site.urls),
    url('^$', v1.index, name="index"),
    url('result/', v2.result, name='result'),
    url('add/', v2.add, name="add")
]
