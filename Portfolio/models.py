from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.TextField()
    image = models.FileField(upload_to='img/')
    def __str__(self):
        return self.title
