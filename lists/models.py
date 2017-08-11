from django.db import models


# Create your models here.
class List(models.Model):
    pass


class Item(models.Model):
    text = models.TextField(blank=False, null=False)
    list = models.ForeignKey(List, default=None, blank=True, null=True)

