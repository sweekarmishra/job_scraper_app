from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=50)
    job_url = models.URLField()

    class Meta:
        app_label = 'job_scraper_app'  # Change this to your actual app name
        managed = True
        default_manager_name = 'mongodb'