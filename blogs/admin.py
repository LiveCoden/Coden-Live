from django.contrib import admin
from django.db import models

from blogs.forms import BlogAdminForm
from coden.settings import TINYMCE_DEFAULT_CONFIG
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title',)
    list_per_page = 20
    formfield_overrides = {
   models.TextField: {'widget': TINYMCE_DEFAULT_CONFIG()}
   }




admin.site.register(Post, PostAdmin)



