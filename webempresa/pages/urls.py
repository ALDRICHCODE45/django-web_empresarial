from . import views
from django.urls import path

urlpatterns = [
    path(route="<int:page_id>/<slug:page_slug>/", view=views.page, name="page"),
]
