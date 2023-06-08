from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Property._meta.fields]


@admin.register(PricingRule)
class PricingRuleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PricingRule._meta.fields]


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Booking._meta.fields]