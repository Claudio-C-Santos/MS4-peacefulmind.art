from django.shortcuts import render

from .forms import newCustomOrderForm


def custom_orders(request):
    customOrder = newCustomOrderForm()

    template = 'custom_order.html'

    context = {
        'customOrder': customOrder
    }

    return render(request, template, context)

