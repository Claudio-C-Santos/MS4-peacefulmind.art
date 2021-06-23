from django.db import models
from django_countries.fields import CountryField


class customOrder(models.Model):
    name = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    country = CountryField(blank_label='Country', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    JEWEL_OPTIONS = [
        ('Pendant', 'Pendant'),
        ('Ring', 'Ring'),
        ('Other', 'Other')
    ]

    material = models.CharField(max_length=254)
    color = models.CharField(max_length=254)
    jewel_type = models.CharField(max_length=10, choices=JEWEL_OPTIONS, default='Other')
    notes = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']

