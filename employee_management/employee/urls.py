from django.urls import path

from . import views

urlpatterns = [
    path("employee/", views.employee, name="employee"),
    path("position/", views.position, name="position"),
    path("project/", views.project, name="project"),
    path("project/<int:id>/", views.project_detail, name="project_detail"),
    path("project/delete/<int:project_id>/", views.project_delete, name="project_delete"),
    path("project/<int:project_id>/<int:employee_id>/addstaff/", views.add_staff, name="add_staff"),
    path("project/<int:project_id>/<int:employee_id>/removestaff/", views.remove_staff, name="remove_staff"),
]