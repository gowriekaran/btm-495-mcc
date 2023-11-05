from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("positions/", views.positions, name='positions'),
    path("add_position/", views.add_position, name='add_position'),
    path("logout/", views.logout_user, name='logout'),
]
