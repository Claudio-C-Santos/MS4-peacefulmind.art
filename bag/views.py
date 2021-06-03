from django.shortcuts import render, redirect


def view_bag(request):
    """ This view will render the bag page where the user can view what's in the bag. """

    return render(request, 'bag.html')


def add_to_bag(request, item_id):

    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        """ Create a message 'This item is already in your shopping bag' """
    else:
        bag[item_id] = 1

    request.session['bag'] = bag
    return redirect(redirect_url)
