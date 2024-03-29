from django.urls import path

from . import views

urlpatterns = [
    path("recipes/", views.get_all_user_recipes),
    path("recipes/user/", views.get_all_user_recipes_by_user),
    path("recipes/create/", views.create_recipe),
    path("recipes/edit/", views.edit_recipe),
    path("recipes/delete/", views.delete_recipe),
    path("recipes/collections/", views.get_all_user_recipe_collections_by_user),
    path("recipes/collections/add/", views.add_user_recipe_to_collection_by_user),
    path("recipes/collections/delete/", views.delete_user_recipe_to_collection_by_user),
]
