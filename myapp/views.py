from django.shortcuts import render,HttpResponse
from .models import Employee,Department, Role
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    
    return render(request,"index.html")

def allEmp(request):
    emps=Employee.objects.all()
    return render(request, "allemp.html", {'allemp':emps})

def addEmpPage(request):
    depart=Department.objects.all()
    role=Role.objects.all()
    return render(request, "addemp.html", {'depart':depart, 'role':role})


def addEmp(request):
    if request.method=='POST':
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        salary=(request.POST['salary'])
        bonus=(request.POST['bonus'])
        phone=(request.POST['phone'])
        department=(request.POST['department'])
        role=(request.POST['role'])
        newemployee=Employee.objects.create(
            Firstname=fname, 
            Lastname=lname, 
            Salary=salary, 
            Bonus=bonus,
            Phone=phone,
            department_id=department,
            role_id=role,
            HireDate=datetime.now()
            )
        return render(request,"successfull.html",{'msg':"Employee Added"})
        
    else:
        return render(request,"addemp.html")


def removeEmp(request,pk=0):
    if pk:
        try:
            empToBeRemove=Employee.objects.get(id=pk)
            empToBeRemove.delete()
            return render(request,"successfull.html",{'msg':"Employee Removed"})
        except Employee.DoesNotExist:
            return render(request, "removeemp.html", {'msg':"please choose a correct employee"})
    else:
        allemp= Employee.objects.all()
        return render(request, "removeemp.html", {'allemp':allemp})

def filterEmp(request):
    if request.method=="POST":
        name=request.POST['name']
        depart=request.POST['depart']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(Firstname__icontains = name) | Q(Lastname__icontains=name))
        if depart:
            emps=emps.filter(department__Name__icontains=depart)
        if role:
            emps=emps.filter(role__Name__icontains=role)
        emps=emps
        return render(request,"allemp.html",{'allemp':emps})
    else:
        depart=Department.objects.all()
        role=Role.objects.all()
        return render(request, "filteremp.html", {'depart':depart, 'role':role})
        