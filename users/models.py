from django.contrib.auth.models import AbstractUser
from .validators import UnicodeUsernameValidator, email_validator
from django.db import models


class CustomUser(AbstractUser):

    username = models.CharField(
        max_length=15,
        unique=True,
        validators=[UnicodeUsernameValidator()],
        error_messages={
            "unique": "Логин занят.",
        })
    group = models.ForeignKey('Group',
                              on_delete=models.CASCADE,
                              # unique=True,
                              # error_messages={
                              #     "unique": "Test group"
                              # }
                              )

    email = models.EmailField(models.EmailField.description,
                              unique=True,
                              validators=[email_validator],
                              error_messages={
                                  "unique": "Такая почта уже используется.",
                              })

    def __str__(self):
        return self.username


class Faculty(models.Model):

    name = models.CharField(max_length=50,
                            unique=True)

    def __str__(self):
        return self.name


class Group(models.Model):

    name = models.CharField(max_length=20,
                            unique=True)
    faculty = models.ForeignKey(Faculty,
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.name
