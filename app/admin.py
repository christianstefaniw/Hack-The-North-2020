from django.contrib import admin

from .models import Post, User


class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ['likes']


admin.site.register(Post, PostAdmin)
admin.site.register(User)
