from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    thumbnail = models.URLField(null=True)
    notes = models.TextField(null=True, default='')

    def __str__(self):
        return f'<User {self.email}>'