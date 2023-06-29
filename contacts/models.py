from django.db import models

# Create your models here.


class Contact(models.Model):
    phoneNumber = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    linkedId = models.ForeignKey('self', on_delete=models.CASCADE, default=None)
    linkPrecedence = models.CharField(max_length=20,default="secondary")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
