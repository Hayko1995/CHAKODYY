# A new class is imported. ##
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import User
import uuid as generateUUID
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from coin.models import CoinCount


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""


    USER = 1
    COLLABORATOR = 2
    MODERATOR = 3
    ADMIN = 4

    ROLE_CHOICES = (
        (USER, "USER"),
        (COLLABORATOR, "COLLABORATOR"),
        (ADMIN, "ADMIN"),
    )
    
    username = None
    USERNAME_FIELD = 'email'
    
    
    is_active = models.BooleanField(_("active"), default=True)
    is_verified = models.BooleanField(_("active"), default=True)
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(_("first name"), max_length=30, blank=True)
    last_name = models.CharField(_("last name"), max_length=30, blank=True)
    phone = models.CharField(_("phone"), max_length=30, blank=True)
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, blank=True, default=USER
    )
    coin = models.ManyToManyField(CoinCount, blank=True)

    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    unique_id = models.UUIDField(
        unique=True, default=generateUUID.uuid4, editable=False
    )
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    objects = UserManager()

    REQUIRED_FIELDS = ["first_name", "last_name", "phone"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
