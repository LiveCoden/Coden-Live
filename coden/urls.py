from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('demo/', include("demoform.urls")),

    path('account/', include("accounts.urls")),
    path('accounts/', include('allauth.urls')),
    path('', include('landing.urls')),
    path('courses/', include('courses.urls')),
    path('admin/', admin.site.urls),   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
