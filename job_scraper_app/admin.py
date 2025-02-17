from django.contrib import admin
from .models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'salary', 'job_url', 'date_posted')
    search_fields = ('title', 'company', 'location')
    list_filter = ('company', 'location', 'salary')

admin.site.register(Job, JobAdmin)