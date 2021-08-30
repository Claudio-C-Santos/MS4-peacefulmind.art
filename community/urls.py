from django.urls import path

from . import views

urlpatterns = [
    path('', views.community, name='community'),
    path('new_card/', views.newCard, name='new_card'),
    path('delete_confirmation/<int:card_id>/', views.delete_confirmation,
         name='delete_confirmation'),
    path('delete_card/<int:card_id>/', views.delete_card, name='delete_card'),
]
