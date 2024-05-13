from django.shortcuts import render
from empapp.models import Employee
from empapp.forms import Employeeform


# Create your views here.

def home(request):
    return render(request,'home.html')

def add(request):
    if(request.method=="POST"):
        f=request.POST['f']
        l=request.POST['l']
        e=request.POST['e']
        p=request.POST['p']
        b=request.POST['b']
        a=request.POST['a']
        d=request.POST['d']
        em=Employee.objects.create(first_name=f,last_name=l,email=e,phone=p,date_of_birth=b,address=a,department=d)
        em.save()
        return view(request)
    return render(request,'add.html')


def view(request):
    e=Employee.objects.all()
    return render(request,'view.html',{'emp':e})

def detail(request,n):
    e=Employee.objects.get(id=n)
    return render(request,'detail.html',context={'e':e})

def edit(request,n):
    e = Employee.objects.get(id=n)
    if (request.method == "POST"):
        form = Employeeform(request.POST, request.FILES, instance=e)  # create form object with values entered by user
        if form.is_valid():
            form.save()
            return view(request)
    form = Employeeform(instance=e)
    return render(request,'add1.html',context={'form':form})

def delete(request,n):
    e=Employee.objects.get(id=n)
    e.delete()
    return view(request)
