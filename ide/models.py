from django.db import models

class Questions(models.Model):
    title = models.CharField(max_length=100)
    contest = models.CharField(max_length=100)
    year = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title