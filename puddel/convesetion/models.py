from django.db import models

from item.models import Item

from django.contrib.auth.models import User

# Create your models here.

class Convesetion(models.Model):
    item=models.ForeignKey(Item,related_name='convesetion', on_delete=models.CASCADE)
    members=models.ManyToManyField(User, related_name='convesetion')
    created_at=models.DateTimeField(auto_now_add=True)
    modefied_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('-modefied_at',)

class ConvesetionMessage(models.Model):
    convesetion=models.ForeignKey(Convesetion, related_name='messages', on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User , related_name='created_messages', on_delete=models.CASCADE)

