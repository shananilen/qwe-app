from django_extensions.db.models import TimeStampedModel
from django.db import models
from user_auth.models import DeliveryUser


# Create your models here.
class Province(TimeStampedModel):
    province_name = models.CharField(max_length=500)

    def __str__(self):
        return self.province_name


class City(TimeStampedModel):
    city_name = models.CharField(max_length=500)
    city_province_id = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name


class Fleet(TimeStampedModel):
    fleet_name = models.CharField(max_length=200)
    fleet_description = models.TextField(null=True)
    fleet_city_id = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.fleet_name


class Vehicle(TimeStampedModel):
    vehicle_number = models.CharField(max_length=200)
    make = models.CharField(max_length=100, null=True)
    model = models.CharField(max_length=100, null=True)
    make_year = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.vehicle_number)


class SecurityTeam(TimeStampedModel):
    team_name = models.CharField(max_length=500)

    def __str__(self):
        return self.team_name


class DeliveryUserSecurityTeam(TimeStampedModel):
    user_id = models.ForeignKey(DeliveryUser, on_delete=models.CASCADE)
    securityteam_id = models.ForeignKey(SecurityTeam, on_delete=models.CASCADE)


class FleetVehicle(TimeStampedModel):
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    fleet_id = models.ForeignKey(Fleet, on_delete=models.CASCADE)

    def __str__(self):
        return self.fleet_id.fleet_name + "-" + self.vehicle_id.vehicle_number


class Route(TimeStampedModel):
    route_name = models.CharField(max_length=400)
    starting_fleet_id = models.ForeignKey(Fleet, on_delete=models.CASCADE)
    starting_location = models.CharField(max_length=500)
    destination = models.CharField(max_length=500)

    def __str__(self):
        return self.route_name


class RouteStatus(TimeStampedModel):
    status_name = models.CharField(max_length=100)

    def __str__(self):
        return self.status_name


class VehicleRoute(TimeStampedModel):
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.route_id)


class VehicleRouteStatus(TimeStampedModel):
    vehicle_route_id = models.ForeignKey(VehicleRoute, on_delete=models.CASCADE)
    route_status_id = models.ForeignKey(RouteStatus, on_delete=models.CASCADE)
    securityteam_id = models.ForeignKey(SecurityTeam, on_delete=models.CASCADE)
