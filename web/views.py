from django.shortcuts import render, reverse
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect

from web.models import Post, Profile


class CreatePost(View):
    def get(self, request, *args, **kwargs):
        return render(request, "web/create.html")

    def post(self, request, *args, **kwargs):
        user_profile = Profile.objects.get(owner=request.user)
        if user_profile:
            new_post = Post(text=request.POST["text"], author=user_profile)
            new_post.save()
        return HttpResponseRedirect(reverse("index"))


class IndexPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, "web/index.html")
