from django.contrib import admin
from .models import Course
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon', 'description')
    list_display_links = ('name',)
    list_editable = ('description','id')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Course, CourseAdmin)
