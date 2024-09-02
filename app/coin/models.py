from django.db import models
from chakodyy import settings
from accounts.models import User
from django.contrib.postgres.fields import ArrayField


User = settings.AUTH_USER_MODEL


class CoinName(models.Model):
    name = models.CharField(max_length=20, blank=False, unique=True)

    def __str__(self) -> str:
        return self.name


# Create your models here.
class CoinCount(models.Model):
    name = models.ForeignKey(CoinName, blank=False, on_delete=models.CASCADE)
    count = models.FloatField(max_length=20, blank=False)
    times = ArrayField(models.DateTimeField(), default=list)

    def __str__(self) -> str:
        return str(self.name) + " " + str(self.count)
