from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/project')
    description = models.TextField()
    customer = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=False)
    link = models.CharField(max_length=300, blank=True)


