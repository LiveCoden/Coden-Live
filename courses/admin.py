from django.contrib import admin
from .models import Course
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon', 'url_name','priority',)
    list_display_links = ('id', )
    list_editable = ('name' ,'url_name','priority',)
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Course, CourseAdmin)
