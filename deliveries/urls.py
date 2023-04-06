from django.urls import path
from deliveries import views

# Url routes of the delivery app
urlpatterns = [
    path('routes', views.routes_list, name='routes_path'),
    path('fleets', views.fleets_list, name='fleets_path'),
    path('vehicles', views.vehicle_list, name='vehicles_path'),
    path('delivery', views.delivery_list, name='delivery_path'),
    path('delete_route/<str:pk>/', views.delete_route, name='delete_route'),
]
