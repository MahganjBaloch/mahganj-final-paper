from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('' , views.index , name = "index"),
    path('blogPage/<str:pk>' , views.blogPage , name = "blogPage"),
    path('authorData/' , views.authorData , name = "authorData"),
    path('addBlogs/' , views.addBlogs , name = "addBlogs"),
    path('addBlogs_page/' , views.addBlogs_page , name = "addBlogs_page")


]
