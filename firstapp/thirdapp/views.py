from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Employee, User

# decorator
def authenticate(fun):
    def authenticate(request):
        try:
            realname = request.session['realname']
        except KeyError:
            return redirect('http://127.0.0.1:8000/secondapp/login/')
        return fun(request)
    return authenticate


def redirectAtAuth(request):
    return redirect('/secondapp/login/')

@authenticate
def home(request):
    return render(request, 'home.html')
@authenticate
def contact(request):
    return render(request, 'contact.html')

# crud
@authenticate
def viewEmployees(request):
    employees = Employee.objects.all()
    # employees = Employee.objects.filter(esal__lte=222000).values()
    return render(request, 'viewsEmployees.html', {'employees' : employees})

@authenticate
def newEmployee(request):
    return render(request, 'newEmployee.html')
@authenticate
def insertEmployee(request):
    emp = Employee()
    emp.eno = request.POST['eno']
    emp.ename = request.POST['ename']
    emp.esal = request.POST['esal']
    emp.save()
    return HttpResponseRedirect('http://127.0.0.1:8000/secondapp/employees/')

@authenticate
def updateEmployeeForm(request):
    eno = request.GET['eno']
    emp = Employee.objects.filter(eno__exact = eno).values()
    return render(request, 'updateEmployee.html', {'emp': emp[0]})

@authenticate
def updateEmployee(request):
    eno = request.POST['eno']
    emp = Employee.objects.filter(eno__exact = eno).values()
    e = Employee()
    # e.id = request.POST['id']
    e.eno = request.POST['eno']
    e.ename = request.POST['ename']
    e.esal = request.POST['esal']
    e.save()
    return HttpResponseRedirect('http://127.0.0.1:8000/secondapp/employees/')

@authenticate
def deleteEmployee(request):
    eno = request.GET['eno']
    emp = Employee.objects.filter(eno__exact = eno)
    emp.delete()
    return HttpResponseRedirect('http://127.0.0.1:8000/secondapp/employees/')


def signup(request):
    d = {}
    try:
        if request.GET['error']==str(1):
            d['errormsg']  = 'Username already exists'
    except:
        d['errormsg'] = ''
    return render(request, 'signup.html', d)

def saveUser(request):
    user = User()
    isUserExist = User.objects.filter(username = request.POST['username'])
    
    if not isUserExist:
        user.username = request.POST['username']
        user.password = request.POST['password']
        user.realname = request.POST['realname']
        user.save()
        url = 'http://127.0.0.1:8000/secondapp/login/'
    else:
        url = 'http://127.0.0.1:8000/secondapp/signup/?error=1'
    return HttpResponseRedirect(url)

def login(request):
    d = {}
    try:
        if request.GET['error']==str(1):
            d['errormsg']  = 'Incorrect Credentials'
    except:
        d['errormsg'] = ''
    return render(request, 'login.html', d)

def loginvalidate(request):
    try:
        user = User.objects.get(username = request.POST['username'], password = request.POST['password'])
        user.username
        request.session['username'] = user.username
        request.session['realname'] = user.realname
        
        url = 'http://127.0.0.1:8000/secondapp/home/'
    except:
        url = 'http://127.0.0.1:8000/secondapp/login?error=1'

    return HttpResponseRedirect(url)
        
@authenticate
def logout(request):
    request.session.clear()
    return redirect('http://127.0.0.1:8000/secondapp/login/')