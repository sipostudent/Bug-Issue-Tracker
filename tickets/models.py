from django.db import models
from account.models import User

# Create your models here.
class Ticket(models.Model):
    title = models.CharField(max_length=200)
    time = models.DateField()
    category = models.CharField(max_length=30)
    details = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)