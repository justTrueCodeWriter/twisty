from django.db import IntegrityError
from django.contrib import messages
from django.shortcuts import render, reverse
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
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


class DeletePost(View):
    def post(self, request, *args, **kwargs):
        index = int(request.POST["index_del"])
        post = Post.objects.all()[index]
        post.delete()
        return HttpResponseRedirect(reverse("index")) 


class EditPost(View):
    def get(self, request, *args, **kwargs):
        return render(request, "web/edit_post.html")

    '''def post(self, request, *args, **kwargs):
        index = int(request.POST["index_del"])
        user_profile = Profile.objects.get(owner=request.user)
        post = Post.objects.get(author=user_profile)[index]
        post.text = request.POST["text"]
        post.save()
        return HttpResponseRedirect(reverse("index"))
    '''


class Registration(View):
    def get(self, request, *args, **kwargs):
        return render(request, "registration/reg.html")

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)

        try:
            new_user = User.objects.create_user(request.POST["username"])
        except IntegrityError:  #SQLite
            messages.error(request, "You are already registered")
            return HttpResponseRedirect(reverse("registration"))

        new_user.set_password(request.POST["password"])
        new_user.save()
        new_profile = Profile(owner=new_user, name=request.POST["nickname"])
        new_profile.save()
        return HttpResponseRedirect(reverse("login"))


class Logout(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return HttpResponseRedirect(reverse("index"))


class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, "registration/login.html")

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        user = authenticate(username=request.POST["username"],
                            password=request.POST["password"])
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return HttpResponseRedirect(request.POST["next"])


class IndexPage(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.order_by('-created')
        context = {"posts": posts}
        return render(request, "web/index.html", context)


class ProfilePage(View):
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(owner=request.user)
        posts = Post.objects.all().filter(author=profile)
        context = {"profile": profile,
                   "posts": posts}
        return render(request, "profile/profile_view.html", context)


class ProfilePageById(View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['id'])
        profile = Profile.objects.get(owner=user)
        posts = Post.objects.all().filter(author=profile)
        context = {"profile": profile,
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
