from django.db import models
from django.forms import CharField


# Create your models here.


class Link(models.Model):
    key: models.SlugField = models.SlugField(max_length=100, unique=True)
    name: models.CharField = models.CharField(max_length=200)
    url: models.URLField = models.URLField(max_length=200, null=True, blank=True)
    created_at: models.DateTimeField = models.DateTimeField(auto_now=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering: list[str] = ["-created_at"]

    def __str__(self) -> CharField:
        return self.name
