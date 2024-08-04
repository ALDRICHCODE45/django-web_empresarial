from django.http import HttpResponse
from django.shortcuts import render
from .models import Service


def services(request) -> HttpResponse:
    services = Service.objects.all()
    return render(request, "services/services.html", {"services": services})


# Create your views here.
