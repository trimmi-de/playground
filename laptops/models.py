from django.db import models


class Laptop(models.Model):

    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)

