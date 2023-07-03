from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"services",views.ServiceViewSet)
router.register(r"rooms",views.RoomViewSet)
router.register(r"hotels",views.HotelViewSet)
router.register(r"reservations",views.ReservationViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("rooms_count/", views.room_count, name="room_count"),
    path("rooms_unreserved/", views.rooms_unreserved, name="rooms_unreserved"),
    path('', include(router.urls)),
    
]