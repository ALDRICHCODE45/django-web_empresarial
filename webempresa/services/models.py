from django.db import models


class Service(models.Model):
    title: models.CharField = models.CharField(max_length=200)
    subtitle: models.CharField = models.CharField(max_length=200)
    content: models.TextField = models.TextField()
    image: models.ImageField = models.ImageField(upload_to="services")
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title


# Create your models here.
