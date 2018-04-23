from django.db import models
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse
from django.conf import settings
import os

from django.utils.timezone import now
from accounts.models import User

def get_avatar_filename(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)

    return "profiles/{base}-{date}{ext}".format(base=filename_base,
                                                date=now().strftime('%Y%m%d%H%M%S'),
                                                ext=filename_ext)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    avatar = models.ImageField(default="first_avatar.png", upload_to=get_avatar_filename)
    bio = models.CharField(max_length=200, default="", blank=True)
    # custom_skill

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profiles:profiles', kwargs={'username': self.user.username})

    # automatically run create_profile if save() method is called by user
