from django.db import models
class short_url(models.Model):
    new = models.CharField(max_length=200)
    old = models.TextField()
    slug = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
