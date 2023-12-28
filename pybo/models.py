from django.db import models

# Create your models here.

class User(models.Model):
    id = models.TextField(primary_key=True)
    passwd = models.TextField()
    nickname = models.TextField()
    email = models.TextField()
    mobile = models.TextField()
    def __str__(self):
        return self.id
