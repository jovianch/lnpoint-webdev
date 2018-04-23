from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError


from autoslug import AutoSlugField
# Create your models here.

from profiles.models import Profile
from accounts.models import User

from django.utils.timezone import now

import datetime
import os


def get_picture_filename(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return "activity/{base}--{date}{ext}".format(base=filename_base,
                                                date=now().strftime('%Y%m%d%H%M%S'),
                                                ext=filename_ext)

class Tag(models.Model):
    name = models.CharField(max_length=32)
    slug = AutoSlugField(populate_from='name')


    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name

class Activity(models.Model):
    
    PRE = 'PRE'
    COMPLETED = 'COMPLETED'
    HELD = 'HELD'
    POSTED = 'POSTED'
    CANCELED = 'CANCELED'

    STATUS_CHOICES = (
        (PRE,PRE),
        (COMPLETED, COMPLETED),
        (HELD, HELD),
        (POSTED, POSTED),
        (CANCELED, CANCELED)
    )

    partner = models.ForeignKey(Profile,
                                related_name='activities',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    photo = models.ImageField(upload_to=get_picture_filename)
    description = models.TextField()
    caption = models.TextField()
    #categories = models.ManyToManyField() // not used yet
    tags = models.ManyToManyField(Tag)
    location_latitude = models.FloatField()
    location_longitude = models.FloatField()
    location_name = models.CharField(max_length=64)
    #location_description = models.TextField(null=True, blank=True) // there will be new entity of place
    fee = models.IntegerField(default=0)
    maximum_guest = models.IntegerField()
    guest = models.ManyToManyField(User, related_name='activities_joined', symmetrical=False, through='UserJoinActivity')
    date_held = models.DateField()
    time = models.TimeField()
    duration = models.IntegerField()
    status = models.CharField(max_length=16, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activities"

    def __str__(self):
        return "{} activity by {}".format(self.name, self.partner)

    @property
    def user(self):
        return self.partner.use

    @user.setter
    def user(self,value):
        self.partner = value.profile
        return self.name

    def join_activity(self, user_that_join):
        user_join = UserJoinActivity(guest=user_that_join, activity=self)
        user_join.save()

    def unjoin_activity(self, user_that_unjoin):
        UserJoinActivity.objects.filter(guest=user_that_unjoin, activity=self).delete()

    def like_activity(self, user_that_like):
        user_like = Like(user=user_that_like, activity=self)
        user_like.save()

    def unlike_activity(self, user_that_unlike):
        Like.objects.filter(user=user_that_unlike, activity=self).delete()

    def get_absolute_url(self):
        return reverse('activity:activity_detail', kwargs={'pk': self.id})

    #is_seen = models.ManyToManyField(Profile) // can be build using reddis later on
    
    #def get_absolute_url(self):

class Like(models.Model):
    activity = models.ForeignKey(Activity, 
                                related_name='liked_by',
                                on_delete=models.CASCADE)
    user = models.ForeignKey(User, 
                            related_name='activities_liked',
                            on_delete=models.CASCADE)
    class Meta:
        unique_together = [('user','activity')]

    def __Unicode__(self):
        return self.user

class Comment(models.Model):
    activity = models.ForeignKey(Activity, 
                                related_name='commented_by',
                                on_delete=models.CASCADE)
    user = models.ForeignKey(User, 
                            related_name='activities_commented',
                            on_delete=None)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __Unicode__(self):
        return self.user

class UserJoinActivity(models.Model):
    guest = models.ForeignKey(User, related_name='guest')
    activity = models.ForeignKey(Activity, related_name='activity')

    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_joined']
        unique_together = [('guest','activity')]

       
     
