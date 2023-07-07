from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from web import views

# TODO: Надо бы пренести в будущем эти ссылки в `web/urls.py`, когда будем внедрять API
urlpatterns = [
    path('', views.IndexPage.as_view(), name="index"),
    path('profile/', views.ProfilePage.as_view(), name="profile"),
    path('profile/<int:id>/', views.ProfilePageById.as_view(), name="profile_id"),
    path('editprofile/', views.EditProfile.as_view(), name="edit_profile"),
    path('create/', views.CreatePost.as_view(), name="create_post"),
    path('deletepost/<int:id>/', views.DeletePost.as_view(), name="delete_post"),
    path('editpost/<int:id>/', views.EditPost.as_view(), name="edit_post"),
    path('viewpost/<int:id>/', views.ViewPost.as_view(), name="view_post"),
    path('admin/', admin.site.urls, name="admin"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("reg/", views.Registration.as_view(), name="registration")
]
