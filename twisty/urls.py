from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from web.views import IndexPage

urlpatterns = [
    path('', IndexPage.as_view(), name="index"),
    path('admin/', admin.site.urls, name="admin"),
    path("change-password/", auth_views.PasswordChangeView.as_view()),
    path("login/", auth_views.LoginView.as_view(), name="login")
]



