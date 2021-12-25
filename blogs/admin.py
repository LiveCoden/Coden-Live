from django.contrib import admin
from django.db import models

from django.db import models
from tinymce.widgets import TinyMCE

from blogs.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title',)
    list_per_page = 20
    list_display = ["title"]
    formfield_overrides = {
    models.TextField: {'widget': TinyMCE()}
    }




admin.site.register(Post, PostAdmin)



