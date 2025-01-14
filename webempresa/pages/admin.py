from django.contrib import admin
from .models import Page

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")


admin.site.register(Page, PageAdmin)
