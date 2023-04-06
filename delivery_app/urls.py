from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('user_auth.urls')),  # auth app
    path('user/', include('system_user.urls')),  # system_user app
    path('deliveries/', include('deliveries.urls'))  # system_user app
]
