from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse


class CreatePost(View):
    def get(self, request, *args, **kwargs):
        ...

    def post(self, request, *args, **kwargs):
        ...


class IndexPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, "web/index.html")
