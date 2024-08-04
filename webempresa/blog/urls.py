from typing import List
from . import views
from django.urls import URLPattern, URLResolver, path

urlpatterns: List[URLResolver | URLPattern] = [
    path(route="", view=views.blog, name="blog"),
    path(route="category/<int:category_id>/", view=views.category, name="category"),
]
