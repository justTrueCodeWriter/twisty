from django.contrib import admin
from django.urls import path

from web.views import IndexPage

urlpatterns = [
    path('', IndexPage.as_view(), name="index"),
    path('admin/', admin.site.urls, name="admin"),
]



