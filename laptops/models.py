from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Laptop(models.Model):

    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
