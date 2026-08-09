from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class expenses(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    amount=models.IntegerField()
    category=models.CharField(max_length=200)
    date=models.DateField(auto_now_add=False)
    description=models.CharField(max_length=255)