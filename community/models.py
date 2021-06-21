from django.db import models


class communityCard(models.Model):
    name = models.CharField(max_length=254)
    website = models.CharField(max_length=254)
    description = models.TextField()
    email = models.CharField(max_length=254)

    def __str__(self):
        return self.name
    
