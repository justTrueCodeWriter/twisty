from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from web.views import IndexPage, CreatePost, ProfilePage, EditProfile, Registration, Logout

urlpatterns = [
    path('', IndexPage.as_view(), name="index"),
    path('profile/', ProfilePage.as_view(), name="profile"),
    path('editprofile/', EditProfile.as_view(), name="edit_profile"), 
    path('create/', CreatePost.as_view(), name="create_post"),
    path('admin/', admin.site.urls, name="admin"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("reg/", Registration.as_view(), name="registration")
]



