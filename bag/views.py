from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ This view will render the bag page where
        the user can view what's in the bag. """

    return render(request, 'bag.html')


def add_to_bag(request, item_id):
    bag = request.session.get('bag', {})
    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')

    if item_id in list(bag.keys()):
        messages.warning(request, f'You have already \
                         added {product.name} to your bag.')
    else:
        bag[item_id] = 1
        messages.success(request, f'{product.name} has
                         been added to your bag.')

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_product(request, item_id):
    """ This view will remove the selected product from the bag """

    bag = request.session.get('bag', {})
    product = get_object_or_404(Product, pk=item_id)

    bag.pop(item_id)

    messages.success(request, f'{product.name} has successfully been removed
                     from your bag.')

    request.session['bag'] = bag

    return redirect(reverse('view_bag'))
