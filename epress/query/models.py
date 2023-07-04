from django.db import models

# Create your models here.

class Query(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    subject = models.CharField(max_length=500, blank=False, null=False)
    message = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.name