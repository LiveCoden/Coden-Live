from django.contrib import admin
from .models import ServicesForm
# Register your models here.

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'course', 'phone')
    list_display_links = ('name',)
    list_per_page = 20

admin.site.register(ServicesForm, ServicesAdmin)
