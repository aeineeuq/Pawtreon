from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', include('projects.urls')),
    path('', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')), #login to the browsable API
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
