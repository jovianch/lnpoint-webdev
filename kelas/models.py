from django.db import models
from accounts.models import User
from profiles.models import Profile
from autoslug import AutoSlugField
from django.utils import timezone
from django.core.validators import MinValueValidator

import datetime


class Category(models.Model):
    name = models.CharField(max_length=32)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Tag(models.Model):
    name = models.CharField(max_length=32)
    slug = AutoSlugField(populate_from='name')


    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name

class OpenClass(models.Model):
    partner = models.ForeignKey(Profile,
                                related_name='open_classes',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField()
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    location_latitude = models.FloatField()
    location_longitude = models.FloatField()
    location_name = models.CharField(max_length=64)
    location_description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    fee = models.IntegerField(null=True, blank=True)
    maximum_guest = models.IntegerField(null=True, blank=True)

    @property
    def user(self):
        return self.partner.user

    @user.setter
    def user(self, value):
        self.partner = value.profile

    @property
    def category(self):
        # Ternyata cuman satu category
        return self.categories.first()

    @category.setter
    def category(self, value):
        cat = Category.objects.get(slug=value)
        self.categories.add(cat)

    class Meta:
        ordering = ['-id']
        verbose_name = "Open Class"
        verbose_name_plural = "Open Classes"

    def __str__(self):
        return "{}'s open class".format(self.partner)


class BookedClass(models.Model):
    ACTIVE = 'ACTIVE'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'

    STATUS_CHOICES = (
        (ACTIVE, ACTIVE),
        (COMPLETED, COMPLETED),
        (CANCELLED, CANCELLED)
    )

    open_class = models.ForeignKey(OpenClass,
                                   related_name='bookings',
                                   null=True,
                                   on_delete=models.SET_NULL)
    users = models.ManyToManyField(User, related_name='classes_joined')
    date = models.DateTimeField()
    additional_description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES)

    @property
    def exceed_time(self):
        return timezone.now() > self.date

    @property
    def should_show(self):
        # Haruskah muncul di daftar kelas tersedia?
        return self.status == BookedClass.ACTIVE and not self.exceed_time

    @property
    def should_ask_status(self):
        # Haruskah minta status ke partner?
        return self.status == BookedClass.ACTIVE and self.exceed_time
