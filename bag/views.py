from django.shortcuts import render, redirect, reverse, HttpResponse


def view_bag(request):
    """ This view will render the bag page where the user can view what's in the bag. """

    return render(request, 'bag.html')


def add_to_bag(request, item_id):
    bag = request.session.get('bag', {})

    redirect_url = request.POST.get('redirect_url')

    if item_id in list(bag.keys()):
        """ Create a message 'This item is already in your shopping bag' """
    else:
        bag[item_id] = 1

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_product(request, item_id):
    """ This view will remove the selected product from the bag """

    bag = request.session.get('bag', {})

    bag.pop(item_id)

    request.session['bag'] = bag
    
    return redirect(reverse('view_bag'))
