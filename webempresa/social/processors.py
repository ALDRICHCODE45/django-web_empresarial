from .models import Link


def extend_context_social(request):
    ctx_extended = {}
    social_links = Link.objects.all()

    for link in social_links:
        ctx_extended[link.key] = link.url

    return ctx_extended
