from django.db import models
from django.forms import forms, widgets


class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=30)
    uname = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    date_created = models.DateTimeField(editable=False, auto_now_add=True)
    date_modified = models.DateTimeField(editable=False, auto_now=True)



