from django.shortcuts import render, redirect, reverse
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



