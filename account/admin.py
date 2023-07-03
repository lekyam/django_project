from django.contrib import admin
from .models import CustomUser
from .models import Role


admin.site.register(CustomUser)
admin.site.register(Role)