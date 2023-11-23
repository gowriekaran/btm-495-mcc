from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("admin-hub/", views.admin_hub, name='admin-hub'),
    path("student-hub/", views.student_hub, name='student-hub'),
    path("new_applicant/", views.new_applicant, name='new_applicant'),
    path("thank-you/", views.thank_you, name='thank-you'),
    path("view-my-applications/", views.view_student_applications, name='view-my-applications'),
    path("student-hub/applications/", views.applications, name='applications'),
    path("positions/", views.positions, name='positions'),
    path("add_position/", views.add_position, name='add_position'),
    path("edit_position/", views.edit_position, name='edit_position'),
    path("update_position/", views.update_position, name='update_position'),
    path("delete_position/", views.delete_position, name='delete_position'),
    path("applicants/", views.applicants, name='applicants'),
    path("candidates/", views.candidates, name='candidates'),
    path("add_candidate/", views.add_candidate, name='add_candidate'),
    path("interviews/", views.interviews, name='interviews'),
    path("logout/", views.logout_user, name='logout'),
]
