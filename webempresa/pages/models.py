from django.db import models
from django.forms import CharField
from ckeditor.fields import RichTextField


# Create your models here.


class Page(models.Model):
    title: models.CharField = models.CharField(max_length=200)
    content: RichTextField = RichTextField()
    created_at: models.DateTimeField = models.DateTimeField(auto_now=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering: list[str] = ["-created_at"]

    def __str__(self) -> CharField:
        return self.title
