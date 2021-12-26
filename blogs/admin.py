from django import forms
from django.contrib import admin
from django.db import models

from django.db import models
from blogs.forms import BlogAdminForm

from blogs.models import Post
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', )
    list_display_links = ('title',)
    list_per_page = 20
    form = BlogAdminForm
    summernote_fields = ('content',)


    




admin.site.register(Post, PostAdmin)



