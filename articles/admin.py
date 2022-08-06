from django.contrib import admin
from .models import Author, Article
# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Author)
# admin.site.register(Author, AuthorAdmin)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass