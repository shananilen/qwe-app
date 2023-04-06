import traceback

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from deliveries.models import *


# routes page
@login_required(login_url='login_path')
def routes_list(request):
    fleets = Fleet.objects.all()
    routes = Route.objects.all()

    if request.method == 'POST':
        data = request.POST
        try:
            save_route = Route(route_name=data['routename'],
                               starting_fleet_id=Fleet.objects.get(id=int(data['fleetid'])),
                               starting_location=data['startinglocation'], destination=data['destination'])
            save_route.save()
        except:
            traceback.print_exc()

    context = {
        'fleets': fleets,
        'routes': routes
    }
    return render(request, 'routes/routes_list.html', context=context)


# fleets page
@staff_member_required
@login_required(login_url='login_path')
def fleets_list(request):
    cities = City.objects.all()
    fleets = Fleet.objects.all()
    vehicles = Vehicle.objects.all()

    if request.method == 'POST':
        data = request.POST
        try:
            save_fleet = Fleet(fleet_name=data['fleetname'],
                               fleet_city_id=City.objects.get(id=int(data['cityid'])),
                               fleet_description=data['description'])
            save_fleet.save()
        except:
            traceback.print_exc()

        try:
            save_vehicle = FleetVehicle(fleet_id=Fleet.objects.get(id=int(data['fleet_id'])),
                                        vehicle_id=Vehicle.objects.get(id=int(data['vehicle_id'])))
            save_vehicle.save()
        except:
            traceback.print_exc()

    context = {
        'cities': cities,
        'fleets': fleets,
        'vehicles': vehicles,
    }
    return render(request, 'routes/fleet_list.html', context=context)


# vehicle page
@staff_member_required
@login_required(login_url='login_path')
def vehicle_list(request):
    vehicles = Vehicle.objects.all()

    if request.method == 'POST':
        data = request.POST
        try:
            save_route = Vehicle(vehicle_number=data['vehicleno'],
                                 make=data['make'],
                                 model=data['manufactureyear'], make_year=data['manufactureyear'])
            save_route.save()
        except:
            traceback.print_exc()

    context = {
        'vehicles': vehicles
    }
    return render(request, 'routes/vehicle_list.html', context=context)


# Delivery page
@login_required(login_url='login_path')
def delivery_list(request):
    auth_user = request.user
    if auth_user.groups.get().name == "ADMIN":
        deliveries = VehicleRoute.objects.all()
        security_teams = SecurityTeam.objects.all()
        routes = Route.objects.all()
        vehicles = Vehicle.objects.all()
        vehicle_routes = VehicleRouteStatus.objects.all()
        route_status = RouteStatus.objects.all()
        if request.method == 'POST':
            data = request.POST
            try:
                save_route = VehicleRoute(route_id=Route.objects.get(id=int(data['routeid'])),
                                          vehicle_id=Vehicle.objects.get(id=int(data['vehicleid'])),
                                          )
                save_route.save()

                save_vehicle_route_status = VehicleRouteStatus(
                    vehicle_route_id=VehicleRoute.objects.get(id=save_route.id),
                    route_status_id=RouteStatus.objects.get(id=1),
                    securityteam_id=SecurityTeam.objects.get(
                        id=int(data['securityid'])))
                save_vehicle_route_status.save()
            except:
                traceback.print_exc()

            try:
                update_vehicle_route = VehicleRouteStatus.objects.get(id=int(data['vehicleroute_id']))
                update_vehicle_route.route_status_id = RouteStatus.objects.get(id=int(data['route_status']))
                update_vehicle_route.securityteam_id = SecurityTeam.objects.get(id=int(data['security_team']))
                update_vehicle_route.save()
            except:
                traceback.print_exc()

        context = {
            'deliveries': deliveries,
            'security_teams': security_teams,
            'routes': routes,
            'vehicles': vehicles,
            'vehicle_routes': vehicle_routes,
            'route_status': route_status,
        }
        return render(request, 'routes/delivery_list.html', context=context)

    elif auth_user.groups.get().name == "NORMAL_USER":
        deliveryuser_securityteam_id = request.user.id
        user_team = DeliveryUserSecurityTeam.objects.get(
            user_id=DeliveryUser.objects.get(id=int(deliveryuser_securityteam_id)))
        vehicle_routes = VehicleRouteStatus.objects.filter(securityteam_id=user_team.securityteam_id.id)
        # deliveries = VehicleRoute.objects.all()
        security_teams = SecurityTeam.objects.all()
        routes = Route.objects.all()
        vehicles = Vehicle.objects.all()

        route_status = RouteStatus.objects.all()
        if request.method == 'POST':
            data = request.POST
            try:
                save_route = VehicleRoute(route_id=Route.objects.get(id=int(data['routeid'])),
                                          vehicle_id=Vehicle.objects.get(id=int(data['vehicleid'])),
                                          )
                save_route.save()

                save_vehicle_route_status = VehicleRouteStatus(
                    vehicle_route_id=VehicleRoute.objects.get(id=save_route.id),
                    route_status_id=RouteStatus.objects.get(id=1),
                    securityteam_id=SecurityTeam.objects.get(
                        id=int(data['securityid'])))
                save_vehicle_route_status.save()
            except:
                traceback.print_exc()

            try:
                update_vehicle_route = VehicleRouteStatus.objects.get(id=int(data['vehicleroute_id']))
                update_vehicle_route.route_status_id = RouteStatus.objects.get(id=int(data['route_status']))
                # update_vehicle_route.securityteam_id = SecurityTeam.objects.get(id=int(data['security_team']))
                update_vehicle_route.save()
            except:
                traceback.print_exc()

        context = {
            # 'deliveries': deliveries,
            'security_teams': security_teams,
            'routes': routes,
            'vehicles': vehicles,
            'vehicle_routes': vehicle_routes,
            'route_status': route_status,
        }
        return render(request, 'routes/delivery_list_normal_user.html', context=context)


# Delete route
@login_required(login_url='login_path')
def delete_route(request, pk):
    Route.objects.filter(id=pk).delete()

    return redirect('routes_path')
