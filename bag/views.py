from django.shortcuts import render, redirect


def view_bag(request):
    """ This view will render the bag page where the user can view what's in the bag. """

    return render(request, 'bag.html')


def add_to_bag(request, item_id):

    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    bag[item_id] = 1

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
