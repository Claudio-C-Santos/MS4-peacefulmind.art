from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .forms import newCustomOrderForm
from .models import customOrder


def custom_orders(request):
    if request.method == 'POST':
        customOrder = newCustomOrderForm(request.POST)

        if customOrder.is_valid():
            customOrder.save()
            messages.success(request, 'Your order has been successfully received. You will be contacted as soon as possible. Thank you!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Something went wrong with your order. Please ensure you filled the form correctly.')
    else:
        customOrder = newCustomOrderForm()

    template = 'custom_order.html'

    context = {
        'customOrder': customOrder
    }

    return render(request, template, context)


def pending_orders(request):
    pending_order = customOrder.objects.all()

    template = 'pending_orders.html'

    context = {
        'pending_order': pending_order
    }

    return render(request, template, context)


def custom_order_details(request, custom_order_number):
    custom_order = get_object_or_404(customOrder, order_number=custom_order_number)

    template = 'custom_order_details.html'
    context = {
        'custom_order': custom_order,
    }

    return render(request, template, context)

