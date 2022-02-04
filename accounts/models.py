from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserCustomManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, username, password=None):
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, first_name, last_name, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            username = username,
            password = password
        )
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, blank=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=150, unique=True)
    phone_number = models.IntegerField(blank=True, null=True)

    joined_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    objects = UserCustomManager()


    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        

    def __str__(self):
        return self.email

    def has_perm(self, perms, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def short_name(self):
        return self.first_name
    
