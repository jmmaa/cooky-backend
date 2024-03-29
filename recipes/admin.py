from django.contrib import admin

from .models import Recipe, UserRecipeCollection, UserRecipe

# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Recipe._meta.fields]


class UserRecipeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in UserRecipe._meta.fields]


class UserRecipeCollectionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in UserRecipeCollection._meta.fields]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(UserRecipe, UserRecipeAdmin)
admin.site.register(UserRecipeCollection, UserRecipeCollectionAdmin)
