from django.db import models

class Post(models.Model):
    title_text = models.CharField(max_length=50)
    content_text = models.CharField(max_length=140)
