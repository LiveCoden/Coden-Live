from django.db import models

class ServicesForm(models.Model):
    name = models.CharField(max_length=100) 
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=100)
    phone = models.TextField(max_length=100)


    def __str__(self):
        return self.email