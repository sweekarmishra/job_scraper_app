from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('job_scraper_app.urls')),  # Correct way to include app URLs
]