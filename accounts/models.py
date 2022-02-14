from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser


<<<<<<< HEAD
class UserCustomManager(BaseUserManager):
=======
class UserManager(BaseUserManager):
>>>>>>> 4710397c97df0ed639ec731e8792e78cf5f126f4
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email = email,
            first_name = first_name,
            last_name = last_name,
            password = password
        )
<<<<<<< HEAD
        user.staff = True
        user.admin = True
        user.is_active = True
=======
        user.active = True
        user.staff = True
        user.admin = True
>>>>>>> 4710397c97df0ed639ec731e8792e78cf5f126f4
        user.superadmin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=150, unique=True)
    phone_number = models.IntegerField(blank=True, null=True)

    joined_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
<<<<<<< HEAD
    is_active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    superadmin = models.BooleanField(default=False)
=======
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
>>>>>>> 4710397c97df0ed639ec731e8792e78cf5f126f4

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

        
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def short_name(self):
        return self.first_name
    
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
<<<<<<< HEAD
        return self.admin
=======
        return self.admin
>>>>>>> 4710397c97df0ed639ec731e8792e78cf5f126f4
