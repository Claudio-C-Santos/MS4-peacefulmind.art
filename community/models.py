from django.db import models


class communityCard(models.Model):
    card_number = models.AutoField(primary_key=True,
                                   null=False,
                                   editable=False)
    name = models.CharField(max_length=254)
    website = models.URLField(max_length=254)
    description = models.TextField(max_length=110)
    email = models.CharField(max_length=254)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']
