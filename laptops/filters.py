import django_filters

from laptops.models import Laptop


class LaptopFilter(django_filters.FilterSet):

    brand_choices = [
        ["asus", "Asus"],
        ["hp", "HP"]
    ]

    brand = django_filters.ChoiceFilter(choices=brand_choices)

    class Meta:
        model = Laptop
        fields = ['name', 'brand']
