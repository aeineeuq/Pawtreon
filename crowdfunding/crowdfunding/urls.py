from django.urls import path, include

urlpatterns = [
    path('', include('projects.urls')),
    path('', include('users.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
