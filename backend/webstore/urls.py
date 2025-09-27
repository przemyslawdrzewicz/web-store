from django.contrib import admin
from django.urls import path, include

api = [
    path('users/', include('users.urls')),
    path('products/', include('products.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api)),
    path('api-auth/', include('rest_framework.urls')),
]
