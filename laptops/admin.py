from django.contrib import admin
from django.shortcuts import render
from django.urls import reverse
from django.utils.html import format_html

from laptops.models import Laptop


class LaptopAdmin(admin.ModelAdmin):

    actions = ["make_published"]

    @admin.action(description="Mark selected stories as published")
    def make_published(self, request, queryset):
       print("Hello")


admin.site.register(Laptop, LaptopAdmin)
