from django.contrib import admin
from deliveries.models import *
# Register your models here.
admin.site.register(Province)
admin.site.register(City)
admin.site.register(Fleet)
admin.site.register(Vehicle)
admin.site.register(SecurityTeam)
admin.site.register(FleetVehicle)
admin.site.register(Route)
admin.site.register(RouteStatus)
admin.site.register(VehicleRoute)
admin.site.register(VehicleRouteStatus)
admin.site.register(DeliveryUserSecurityTeam)
