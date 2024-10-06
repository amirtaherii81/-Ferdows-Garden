from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','family','is_active')

@admin.register(ArticleGroup)
class ArticleGroupAdmin(admin.ModelAdmin):
    list_display = ('group_title',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(ArticleGalery)
class ArticleGaleryAdmin(admin.ModelAdmin):
    list_display = ('article', 'image_name')


