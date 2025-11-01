"""
AWJ Calculator Pro - Main URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # API Endpoints
    path('api/', include('backend.apps.calculations.urls')),
    # path('api/', include('backend.apps.analysis.urls')),  # Přidat později
    # path('api/', include('backend.apps.ai_optimization.urls')),  # Přidat později
    # path('api/', include('backend.apps.chatbot.urls')),  # Přidat později

    # Frontend - Main Page
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]

# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Admin site customization
admin.site.site_header = "AWJ Calculator Pro Administration"
admin.site.site_title = "AWJ Admin"
admin.site.index_title = "Welcome to AWJ Calculator Pro Admin"
