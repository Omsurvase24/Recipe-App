from django.contrib import admin
from .models import *
# Register your models here.


class RecipeWho(admin.ModelAdmin):
    list_display = ['recipe_name', 'user']


admin.site.register(Recipe, RecipeWho)
admin.site.register(Comment)
