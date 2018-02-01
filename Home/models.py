from django.db import models
from django.contrib.auth.models import User


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.CharField(max_length=100)
    phone = models.CharField("Phone Nunber", max_length=100)


class Book(models.Model):
    name = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='docs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
