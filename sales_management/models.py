from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import post_delete, pre_save
from phone_field import PhoneField


class SalesPost(models.Model):
    name            = models.CharField(max_length=50, null=False, blank=False)
    contact         = PhoneField(blank=True)
    date_purchase   = models.DateTimeField(auto_now_add=True, verbose_name='date purchase')
    author          = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug            = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Customer Record'
        verbose_name_plural = 'Sales'

# @receiver(post_delete, sender=SalesPost)
# def submission_delete(sender, instance, **kwargs):
#     instance.id.delete(False)

def pre_save_sales_post_receiver(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username + '-' + instance.name)

pre_save.connect(pre_save_sales_post_receiver, sender=SalesPost)