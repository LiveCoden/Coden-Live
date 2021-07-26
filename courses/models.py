from django.db import models
from django.db.models.lookups import IContains

class Course(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='photos/%Y/%m/%d')
    description = models.TextField()
    content = models.JSONField(blank=True)
    amount = models.IntegerField(default=0)
    priority = models.IntegerField(default=1)
    teacher = models.CharField(max_length=200, default="Arshdeep Singh")
    url_name = models.CharField(max_length=200, default="Course - Coden Live")
    alt_text = models.CharField(max_length=200, default="Course - Coden Live")
    who_should_apply = models.TextField(blank=True)
    job_opportunity = models.TextField(blank=True)
    major_topic_covered = models.TextField(blank=True)
    skills = models.JSONField(default=[])

    def __str__(self):
        return self.name