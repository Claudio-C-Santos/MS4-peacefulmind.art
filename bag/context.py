from decimal import Decimal
from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    product_counter = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_counter': product_counter,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_thresholdd': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total
    }

    return context
