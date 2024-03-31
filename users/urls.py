from django.urls import path

from . import views

urlpatterns = [
    path("user/", views.get_user),
    # path("users/", views.get_users),
    # path("users/create/", views.create_user),
    # path("users/update/", views.update_user),
    # path("users/delete/", views.delete_user),
    # auth
    path("users/signup/", views.signup),
    path("users/login/", views.login),
]
