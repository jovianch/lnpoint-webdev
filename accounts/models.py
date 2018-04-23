from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.utils import timezone
from django.contrib.auth import authenticate
from datetime import datetime
from accounts import constants
import phonenumbers

class UserManager(BaseUserManager):
    def create_user(self, email, username, fullname, password):
        if not email:
            raise ValueError("Kamu harus memiliki email")
        if not username:
            raise ValueError("Kamu harus memiliki username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            fullname=fullname
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, fullname, password):
        user = self.create_user(
            email,
            username,
            fullname,
            password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):

    PARTNER = 'PARTNER'

    #Yang harus dimiliki pengguna
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=40, primary_key=True)
    fullname = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    #untuk verified partner
    card_id = models.CharField(max_length=20, help_text=" NIM", blank=True)
    phone_number = models.CharField(max_length=15, help_text="Nomor HP", blank=True, null=True)
    contact = models.CharField(max_length=255, help_text="ID line", blank=True)
    institution = models.CharField(max_length=100, blank=True)

    follows = models.ManyToManyField('self', related_name='followers', symmetrical=False, through='UserFollow')

    last_notified_message = models.DateTimeField(default=datetime(2000, 1, 1, 0, 0, 0))

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["fullname", "email"]

    def __str__(self):
        return "@{}".format(self.username)

    def get_short_name(self):
        return self.fullname

    def get_long_name(self):
        return "{} (@{})".format(self.fullname, self.username)

    def get_phone_number(self):
        phone_number = phonenumbers.parse(self.phone_number, "ID")

        if phonenumbers.is_valid_number(phone_number):
            return phonenumbers.format_number(
                phone_number, phonenumbers.PhoneNumberFormat.E164
            )
        else:
            raise Exception('Phone number is not valid.')

    def should_notify_new_message(self):
        try:
            phone_number = self.get_phone_number()

            if timezone.now() - self.last_notified_message > constants.TIMEDELTA_NOTIFY_NEW_MESSAGE:
                return True
            else:
                return False
        except Exception as e:
            return False

    def follow(self, user_to_follow):
        user_follow = UserFollow(who=self, whom=user_to_follow)
        user_follow.save()

    def unfollow(self, user_to_unfollow):
        UserFollow.objects.filter(who=self, whom=user_to_unfollow).delete()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

class UserFollow(models.Model):
    who = models.ForeignKey(User, related_name='who')
    whom = models.ForeignKey(User, related_name='whom')

    date_followed = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_followed']
        unique_together = [('who', 'whom')]


