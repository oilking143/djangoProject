from django.db import models
import hashlib


# Create your models here.
class Period(models.Model):
    period = models.DateTimeField(auto_now_add=True)
    number = models.TextField(default="0,0,0,0,0")
    bip39 = models.TextField(default="")
    sha256 = models.TextField(default="")



    class Meta:
        db_table = "period+history"
