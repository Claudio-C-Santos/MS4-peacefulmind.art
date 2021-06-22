from django.db import models


class communityCard(models.Model):
    name = models.CharField(max_length=254)
    website = models.URLField(max_length=254)
    description = models.TextField()
    email = models.CharField(max_length=254)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']

    
