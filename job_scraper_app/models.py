from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=100, blank=True, null=True)
    job_url = models.URLField(max_length=500, blank=True, unique=True)
    description = models.TextField(blank=True, null=True)  # Ensure this field exists
    date_posted = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.job_title