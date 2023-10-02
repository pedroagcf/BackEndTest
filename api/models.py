from django.db import models

# Create your models here.
class Dividend(models.Model):
    id = models.AutoField(primary_key=True)
    symbol = models.CharField(max_length=100, null=False)
    date = models.CharField(max_length=255 ,null=False)
    amount = models.FloatField(null=False) 