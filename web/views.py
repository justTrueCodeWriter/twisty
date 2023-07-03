from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse


class IndexPage(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!")
