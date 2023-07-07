from django.contrib import admin
import web.models as models


class ProfileAdmin(admin.ModelAdmin):
    ...


class PostAdmin(admin.ModelAdmin):
    ...


class CommentaryAdmin(admin.ModelAdmin):
    ...


admin.site.register(models.Profile, ProfileAdmin)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Commentary, CommentaryAdmin)
