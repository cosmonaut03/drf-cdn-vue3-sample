import uuid
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import AbstractUser, UserManager as AbstractUserManager
from django_boost.models.mixins import LogicalDeletionMixin
from django.db import models


class UserManager(AbstractUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(LogicalDeletionMixin, AbstractUser):
    username_validator = UnicodeUsernameValidator()

    class Role(models.IntegerChoices):
        MANAGEMENT = 0
        GENERAL = 1
        PART_TIME = 2

    # 不要なフィールドはNoneにすることができる
    first_name = None
    last_name = None
    date_joined = None
    groups = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    password = models.CharField("パスワード", max_length=100)
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[username_validator],
    )
    email = models.EmailField(max_length=254, unique=True)
    role = models.PositiveIntegerField(choices=Role.choices, default=Role.PART_TIME)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # デフォルトはusernameだが今回は社員番号を指定
    USERNAME_FIELD = "email"
    PASSWORD_FIELD = "password"
    # uniqueのemailとusernameを指定
    REQUIRED_FIELDS = ["password"]

    objects = UserManager()

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.pk
