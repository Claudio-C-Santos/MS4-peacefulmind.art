from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import communityCard
from .forms import newCardForm


def community(request):
    cards = communityCard.objects.all()

    template = 'community.html'

    context = {
        'cards': cards,
    }

    return render(request, template, context)


def newCard(request):  
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry but you are not authorized to do this. Please create an account.')

    if request.method == 'POST':
        card = newCardForm(request.POST)

        if card.is_valid():
            card.save()
            messages.success(request, 'The card for this business has successfully been created.')
            return redirect(reverse('community'))
        else:
            messages.error(request, 'Something went wrong! Please ensure all details are correctly inserted.')
    else:
        card = newCardForm()

    template = 'new_card.html'

    context = {
        'card': card
    }

    return render(request, template, context)


def delete_confirmation(request, card_id):
    """ Checks if the user really want to delete the product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry but you are not authorized to do this. Contact the store manager.')

    card = get_object_or_404(communityCard, pk=card_id)

    template = 'delete_card.html'

    context = {
        'card': card,
    }

    return render(request, template, context)


def delete_card(request, card_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry but you are not authorized to do this. Contact the store manager.')
        
    card = get_object_or_404(communityCard, pk=card_id)

    card.delete()
    messages.success(request, f'{card.name} has been successfully deleted!')

    return redirect(reverse('community'))

