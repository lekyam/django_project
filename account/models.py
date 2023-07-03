from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from .validators import validate_adult

class Role(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class CustomUser(AbstractUser):
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField(validators=[validate_adult])
    roles = models.ManyToManyField(Role, related_name='users')
    groups = models.ManyToManyField(Group, related_query_name='custom_users', related_name='+')
    user_permissions = models.ManyToManyField(Permission, related_query_name='custom_users', related_name='+')

    def __str__(self):
        return self.username