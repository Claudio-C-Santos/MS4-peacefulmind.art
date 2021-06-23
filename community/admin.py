from django.contrib import admin

from .models import communityCard


class OrderAdmin(admin.ModelAdmin):

    list_display = ('name', 'card_number', 'description',
                    'date')

    """ Will show the order with most recent date first """ 

    ordering = ('-date',)


admin.site.register(communityCard, OrderAdmin)
