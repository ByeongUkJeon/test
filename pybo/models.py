from django.db import models

# Create your models here.

class User(models.Model):
    account = models.CharField(max_length=50, primary_key=True)
    passwd = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
