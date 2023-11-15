from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("post/form/", views.PostForm, name="PostForm")
]