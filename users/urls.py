from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import login_view, logout_view, registry_view

urlpatterns = [                                                                                              
 path('login', login_view, name='login' ),
 path('logout', logout_view, name='logout' ),
 path('registry', registry_view, name='registry' ),
]
