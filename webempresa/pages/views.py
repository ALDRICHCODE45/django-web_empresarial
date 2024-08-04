from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Page


# Create your views here.


def page(request, page_id, page_slug) -> HttpResponse:
    page = get_object_or_404(Page, id=page_id)
    return render(
        request=request, template_name="pages/sample.html", context={"page": page}
    )
