from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("admin-hub/", views.admin_hub, name='admin-hub'),
    path("student-hub/", views.student_hub, name='student-hub'),
    path("positions/", views.positions, name='positions'),
    path("add_position/", views.add_position, name='add_position'),
    path("edit_position/", views.edit_position, name='edit_position'),
    path("update_position/", views.update_position, name='update_position'),
    path("delete_position/", views.delete_position, name='delete_position'),
    path("logout/", views.logout_user, name='logout'),
]
