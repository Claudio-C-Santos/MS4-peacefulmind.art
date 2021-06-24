from django.db import models
from django_countries.fields import CountryField


class customOrder(models.Model):
    name = models.CharField(max_length=254)
    email = models.CharField(max_length=20)
    street_address1 = models.CharField(max_length=80)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40)
    postcode = models.CharField(max_length=20)
    county = models.CharField(max_length=80, null=True, blank=True)
    country = CountryField(blank_label='Country')
    date = models.DateTimeField(auto_now_add=True)

    JEWEL_OPTIONS = [
        ('Pendant', 'Pendant'),
        ('Ring', 'Ring'),
        ('Other', 'Other')
    ]

    material = models.CharField(max_length=254, null=True, blank=True)
    color = models.CharField(max_length=254, null=True, blank=True)
    jewel_type = models.CharField(max_length=10, choices=JEWEL_OPTIONS, default='Other')
    notes = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']

