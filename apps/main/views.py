from django.http import HttpResponse
from django.shortcuts import render

from apps.main.models import Test


def index(request):
    msg = Test.objects.all()
    return render(request, "index.html", context={"users": msg})
