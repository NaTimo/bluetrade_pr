from django.db import models
import uuid
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from datetime import datetime
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.

class City(models.Model):
    name = models.CharField(verbose_name="City_name", max_length=200, help_text="Name of the city (for example Klaipėda)")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

class Ad(models.Model):
    title = models.CharField(verbose_name="Ad title", max_length=200)
    # description = models.TextField(verbose_name="Ad_description", max_length=1000)
    city = models.ManyToManyField(to="City", blank=True)
    uuid = models.UUIDField(verbose_name="UUID", default=uuid.uuid4, help_text="Unique ad id")
    due_ad_end = models.DateField(verbose_name="Expires at")
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads')
    photo = models.ImageField(verbose_name="Photo", upload_to="photos", null=True, blank=True)
    description = HTMLField(verbose_name="Ad_description", blank=True, null=True)
    def display_city(self):
        return ', '.join(city.name for city in self.city.all()[:3])

    display_city.short_description = "City"

    CATEGORY = (
        ('t', 'Transportation'),
        ('r', 'Real estate'),
        ('w', 'Work, services'),
        ('f', 'Furniture, appliances'),
        ('c', 'Computers'),
        ('o', 'Communication'),
        ('m', 'Media'),
        ('e', 'Entertainment'),
        ('l', 'Clothing'),
        ('h', 'Children'),
    )


    category = models.CharField(
        max_length=1,
        choices=CATEGORY,
        blank=True,
        default='a',
        help_text='Category (for example Computers)',
    )

    def display_category(self):
        return dict(self.CATEGORY)[self.category]

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Ad"
        verbose_name_plural = "Ads"

@receiver(pre_delete, sender=Ad)
def delete_ad(sender, instance, **kwargs):
    if instance.due_ad_end <= datetime.now().date():
        instance.delete()