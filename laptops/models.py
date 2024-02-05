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


class Sale(models.Model):
    class Meta:
        ordering = ('date__year', 'date__month', 'city', 'date__day')
        verbose_name = 'sale'
        verbose_name_plural = 'sales'

    date = models.DateField()
    city = models.CharField(max_length=255)
    sales = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.date}, {self.city}, {self.sales}'
