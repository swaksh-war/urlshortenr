from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class URL(models.Model):
    longurl = models.CharField(max_length=100000)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    uuid = models.CharField(max_length=7)
    shortenurl = models.CharField(default='aaaaa', max_length=10000)

    def __str__(self):
        return str(URL.uuid)