from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver


class Products(models.Model):
    name            =models.CharField(max_length=100, null=False, blank=False)
    company         =models.CharField(max_length=400, null=False, blank=False)
    type            =models.CharField(max_length=400, null=False, blank=False)
    cost            =models.FloatField()
    stock           =models.IntegerField()
    # author          =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # slug            =models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Products"
        verbose_name_plural = 'Product'

# def pre_save_products_receiver(sender, instance):



