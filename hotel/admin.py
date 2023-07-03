from django.contrib import admin
from .models import Hotel
from .models import Service
from .models import Room
from .models import Reservation
from .models import HotelAdditionRequest

admin.site.register(Hotel)
admin.site.register(Service)
admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(HotelAdditionRequest)