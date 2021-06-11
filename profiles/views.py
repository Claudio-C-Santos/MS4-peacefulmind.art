from django.shortcuts import render


def profile(request):
    """ View to display user's profile """

    template = 'profile.html'
    context = {}

    return render(request, template, context)

