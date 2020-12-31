from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=300)
    email = models.CharField(max_length=80, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    birthday = models.DateField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    blocked_status = models.BooleanField(default=False, verbose_name="Blocked")
    blocked_at = models.DateTimeField(auto_now=False, blank=True, null=True)
    delete_status = models.BooleanField(default=False, verbose_name="Deleted")
    deleted_at = models.DateTimeField(auto_now=False, blank=True, null=True)

    def __str__(self):
        return self.username


class Critic(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=300)
    email = models.CharField(max_length=80, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    birthday = models.DateField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    blocked_status = models.BooleanField(default=False, verbose_name="Blocked")
    blocked_at = models.DateTimeField(auto_now=False, blank=True, null=True)
    delete_status = models.BooleanField(default=False, verbose_name="Deleted")
    deleted_at = models.DateTimeField(auto_now=False, blank=True, null=True)

    def __str__(self):
        return self.username
