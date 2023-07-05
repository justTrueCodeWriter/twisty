from django.shortcuts import render, reverse
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User

from web.models import Post, Profile


class CreatePost(View):
    def get(self, request, *args, **kwargs):
        return render(request, "web/create.html")

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user_profile = Profile.objects.get(owner=request.user)
            if user_profile:
                new_post = Post(text=request.POST["text"], author=user_profile)
                new_post.save()
        return HttpResponseRedirect(reverse("index"))


class Registration(View):
    def get(self, request, *args, **kwargs):
        return render(request, "registration/reg.html")

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        new_user = User.objects.create_user(request.POST["username"])
        new_user.set_password(request.POST["password"])
        new_user.save()
        new_profile = Profile(owner=new_user, name=request.POST["nickname"])
        new_profile.save()
        return HttpResponseRedirect(reverse("login"))


class IndexPage(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        context = {"posts": posts}
        return render(request, "web/index.html", context)

class ProfilePage(View):
    def get(self, request, *args, **kwargs):
        username = Profile.objects.get(owner=request.user)
        posts = Post.objects.all().filter(author = username)
        context = {"username": username,
                   "posts": posts}
        return render(request, "profile/profile_view.html", context)

class EditProfile(View):
    def get(self, request, *args, **kwargs):
        return render(request, "profile/edit_profile.html")
    
    def post(self, request, *args, **kwargs):
        username = Profile.objects.get(owner=request.user)
        username.name = request.POST["username"]
        username.save(update_fields=["name"])
        return HttpResponseRedirect(reverse("profile"))
