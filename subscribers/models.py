from django.db import models

# Create your models here.


class Subscribers(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
