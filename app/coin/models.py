from django.db import models
from chakodyy import settings
from accounts.models import User


User = settings.AUTH_USER_MODEL


class Name(models.Model):
    name = models.CharField(max_length=20, blank=False)

    def __str__(self) -> str:
        return self.name


# Create your models here.
class Coin(models.Model):
    name = models.ForeignKey(Name, blank=False, on_delete=models.CASCADE)
    count = models.FloatField(max_length=20, blank=False)

    
