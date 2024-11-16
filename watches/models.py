from django.db import models
from django.utils import timezone
# Create your models here.

class Watches(models.Model):
    gender = models.CharField(max_length=30)
    type = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.gender}<--->{self.type}'
    
    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Watches"


