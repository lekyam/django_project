from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from rest_framework import viewsets
from .models import Service, Hotel, Room, Reservation
from .serializers import ServiceSerializer, HotelSerializer, RoomSerializer, ReservationSerializer
from datetime import date

def index(request):
    return HttpResponse("Hello World Hotels")

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

def room_count(request):
    try:
        count = Room.objects.count()
        return JsonResponse(
            {
                "count": count
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)
    
def rooms_unreserved(request):
    try:
        today = date.today()

        reservations_today = Reservation.objects.filter(
            Q(start_date__lte=today) & Q(end_date__gte=today)
        )

        reserved_room_ids = [reservation.room.id for reservation in reservations_today]
        unreserved_rooms = Room.objects.exclude(id__in=reserved_room_ids)
        unreserved_room_ids = list(unreserved_rooms.values_list('id', flat=True))
        return JsonResponse(
            {
                "unreserved_rooms": unreserved_room_ids
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)