from django.contrib import admin

from .models import customOrder


class OrderAdmin(admin.ModelAdmin):

    list_display = ('name', 'date', 'jewel_type')

    """ Will show the order with most recent date first """ 

    ordering = ('-date',)

admin.site.register(customOrder, OrderAdmin)
