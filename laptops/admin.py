from django.contrib import admin
from django.shortcuts import render
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from laptops.models import Laptop, Vendor


class LaptopAdmin(admin.ModelAdmin):

    actions = ["make_published"]

    @admin.action(description="Mark selected stories as published")
    def make_published(self, request, queryset):
       print("Hello")


admin.site.register(Laptop, LaptopAdmin)


class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'overview_link']

    def has_add_permission(self, request):
        return False

    def overview_link(self, obj):
        return mark_safe(f'<a href="/admin/laptops/overview/?vendor_id={obj.id}">See overview</a>')


admin.site.register(Vendor, VendorAdmin)


class Overview(Laptop):
    class Meta:
        proxy = True

class LaptopCustomListAdmin(admin.ModelAdmin):
    change_list_template = 'admin/laptop/payment_overview.html'
    model = Overview

    list_display = ['name', "brand"]

admin.site.register(Overview, LaptopCustomListAdmin)