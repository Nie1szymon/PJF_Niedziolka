from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    # You can remove these fields as they become redundant
    groups = models.ManyToManyField(Group, related_name="accounts_user_set")
    user_permissions = models.ManyToManyField(Permission, related_name="accounts_user_set")
