from django.db import models

class DemoForm(models.Model):
    name = models.CharField(max_length=100) 
    email = models.EmailField(max_length=100)
    course = models.TextField(max_length=100)
    phone = models.TextField(max_length=100)


    def __str__(self):
        return self.name