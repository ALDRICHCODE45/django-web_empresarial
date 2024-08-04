from . import views
from django.urls import URLPattern, URLResolver, path

urlpatterns: list[URLResolver | URLPattern] = [
    path(route="", view=views.contact, name="contact"),
]
