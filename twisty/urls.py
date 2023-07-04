from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from web.views import IndexPage, CreatePost

urlpatterns = [
    path('', IndexPage.as_view(), name="index"),
    path('create/', CreatePost.as_view(), name="create_post"),
    path('admin/', admin.site.urls, name="admin"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout")
]



