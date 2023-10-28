from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class contact(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    question = models.TextField()
    answer = models.TextField(default="Thanks for contacting us.We will get back to you soon")
    subscribe = models.BooleanField()

    class Meta:
        ordering = ["-question"]

    def __str__(self):
        return self.name
