from django.db import models
from django.contrib.auth.models  import (PermissionsMixin, BaseUserManager, AbstractBaseUser)  
from django.conf import settings

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, SSN, username, phone_number,user_type, password=None):
        if not SSN:
            raise ValueError('Users must have a SSN')
        if not username:
            raise ValueError('Users must have a username')
        if not phone_number:
            raise ValueError('Users must have a phone number')
        if not user_type:
            raise ValueError('Users must have a user type')

        user = self.model(
            SSN=SSN,
            username=username,
            phone_number=phone_number,
            user_type=user_type
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, username='admin'):
        user = self.create_user(
            email=email.lower(),
            password=password,
            username=username
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_pro = True
        
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(verbose_name='name', max_length=80,blank=True)
    SSN= models.IntegerField(unique=True,blank=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    phone_number = models.IntegerField(unique=True,blank=False)
    
    OWNER = 1
    DEALER = 2
    CUSTOMER = 3

    USER_TYPE_CHOICES = (
      (OWNER, 'owner'),
      (DEALER, 'dealer'),
      (CUSTOMER, 'customer'),

     )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,default=2)
    
    USERNAME_FIELD = 'SSN'
    REQUIRED_FIELDS=['username','phone_number','user_type']
    objects = MyUserManager()
    
    class Meta:
        permissions = []

    def __str__(self):
        return self.username