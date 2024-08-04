from typing import Literal, LiteralString
from django.contrib import admin
from .models import Category, Post

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")


class PostAdmin(admin.ModelAdmin):
    readonly_fields: tuple[Literal["created_at", "updated_at"]] = (
        "created_at",
        "updated_at",
    )
    list_display: tuple[Literal["title"], Literal["author"], Literal["published"]] = (
        "title",
        "author",
        "published",
        "post_categories",
    )
    search_fields: tuple[Literal["content"], Literal["author__username"]] = (
        "content",
        "author__username",
    )
    list_filter: tuple[Literal["author__username"]] = ("author__username",)

    def post_categories(self, obj) -> LiteralString:
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])

    post_categories.short_description = "Categorias"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
