from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Employee, Position, Project
from django.db.models import *

def employee(request):
    all_employee = Employee.objects.order_by("id")
    num_employee = all_employee.count()
    context = {"emp": all_employee,
               "num": num_employee,
    }
    return render(request, "employee.html", context)

def position(request):
    all_position = Position.objects.annotate(count=Count("employee")).order_by("id")
    context = {"pos": all_position}
    return render(request, "position.html", context)

def project(request):
    all_project = Project.objects.order_by("id")
    context = {"pj": all_project}
    return render(request, "project.html", context)

def project_detail(request, id):
    proj = Project.objects.get(id=id)
    context = {"proj": proj,
               "staff": proj.staff.all,
               "start_date": proj.start_date.strftime("%Y-%m-%d"),
               "due_date": proj.due_date.strftime("%Y-%m-%d")}
    return render(request, "project_detail.html", context)

def project_delete(request, project_id):
    if request.method == "GET":
        return HttpResponse("result")
    elif request.method == "POST":
        return HttpResponse(status=201)
    elif request.method == "DELETE":
        del_project = Project.objects.get(id=project_id)
        del_project.delete()
        return JsonResponse({'foo':'bar'}, status=200)
    
def add_staff(request, project_id, employee_id):
    if request.method == "PUT":
        project = Project.objects.get(id=project_id)
        employee = Employee.objects.get(id=employee_id)
        project.staff.add(employee)
        return JsonResponse({'foo':'bar'}, status=200)
    
def remove_staff(request, project_id, employee_id):
    if request.method == "DELETE":
        project = Project.objects.get(id=project_id)
        employee = Employee.objects.get(id=employee_id)
        project.staff.remove(employee)
        return JsonResponse({'foo':'bar'}, status=200)
    

