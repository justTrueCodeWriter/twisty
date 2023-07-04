from django.contrib import admin
from web.views import Profile, Post


class ProfileAdmin(admin.ModelAdmin):
    ...


class PostAdmin(admin.ModelAdmin):
    ...


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)

