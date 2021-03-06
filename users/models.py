from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=40, blank=True)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    #organization = models.ForeignKey()
    location = models.CharField(max_length=30, blank=True)
    is_lawyer = models.BooleanField(default=False)
    saw_dashboard = models.BooleanField(default=False)
    saw_tree_view = models.BooleanField(default=False)
    saw_node_create = models.BooleanField(default=False)
    saw_published_trees = models.BooleanField(default=False)
    saw_visualbuilder = models.BooleanField(default=False)


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, **kwargs):
    new_profile = kwargs.pop('created')
    user = kwargs.pop('instance')
    if new_profile:
        Profile.objects.create(user=user)
