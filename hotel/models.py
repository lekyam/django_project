from django.db import models
from .validators import validate_positive, validate_date, validate_max_days_reservation, validate_start_end_date,validate_future_date
class Hotel(models.Model):
    owner = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    amenities = models.JSONField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    def __str__(self):
        return f"Hotel: {self.name}"

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[validate_positive])
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    def __str__(self):
        return f"Service: {self.name}"

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[validate_positive])
    is_available = models.BooleanField(default=True)
    services = models.ManyToManyField(Service)
    features = models.JSONField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    def __str__(self):
        return f"{self.room_type} - {self.hotel.name}"

class Reservation(models.Model):
    user = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField(validators=[validate_date,validate_future_date])
    end_date = models.DateField(validators=[validate_date, validate_future_date])
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
   

    def clean(self):
        if self.start_date and self.end_date:
            validate_start_end_date(self.start_date, self.end_date)
            validate_max_days_reservation(self.start_date, self.end_date)
    def __str__(self):
        return f"{self.user.username} - {self.room.room_type}"

class HotelAdditionRequest(models.Model):
    user = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    def __str__(self):
        return f"Hotel Addition Request: {self.name}"