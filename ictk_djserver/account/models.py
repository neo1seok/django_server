from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    user_name = models.CharField(max_length=64,verbose_name='사용자이름', null=True)
    phone_number = models.CharField(max_length=32,verbose_name='전화번호', null=True)
    mobile_number = models.CharField(max_length=32,verbose_name='휴대폰번호', null=True)
    position = models.CharField(max_length=32,verbose_name='직급', null=True)
    depart = models.CharField(max_length=64,verbose_name='부서', null=True)
    address = models.CharField(max_length=255,verbose_name='주소', null=True)



    date_of_birth = models.DateField(verbose_name='생년월일',blank=True, null=True,default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin