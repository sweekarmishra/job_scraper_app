from django.urls import path
from .views import home, job_list

urlpatterns = [
    path('', home, name='home'),         # Home page with search bar
    path('jobs/', job_list, name='job_list'),  # Job search results page
]