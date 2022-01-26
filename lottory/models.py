from django.db import models


# Create your models here.
class Lottory(models.Model):
    period = models.DateTimeField(auto_now_add=True)
    number = models.TextField()
    bip39 = models.TextField()
    sha256 = models.TextField()

    class Meta:
        db_table = "lottery_period"
