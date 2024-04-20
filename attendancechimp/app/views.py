# these are Django imports
from venv import create
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
from django.core.exceptions import PermissionDenied

# these are import from my model
from .models import *

@csrf_exempt
def index(request):
    '''
    Presents the main landing page
    Error checks: 
        - this view only triggers on a GET request.
    '''
    
    if request.method == "GET":
        return render(request, 'app/index.html', {'my_var': 'its value'})
    
    raise PermissionDenied
    

@csrf_exempt
def handle_form(request):

    cname = request.POST['cname']
    cnum =  request.POST['cnum']

    print(cname, cnum)

    new_course = Course(cname, cnum)
    new_course.save()

    return render(request, 'app/index.html', {})

@csrf_exempt
def new(request):
    '''
    The page for creating a new user
    Error checks:
        - this view can only trigger on a GET request.
        - this view only triggers if the user isn't logged in
    '''
    
    if request.method == "GET" and not request.user.is_authenticated:
        return render(request, 'app/new.html', {})
    
    raise PermissionDenied

@csrf_exempt
def new_submit(request):
    
    return render(request)

@csrf_exempt
def createUser(request):

    '''
    Handles a submission from a new user creation form
    Error checks:
        - raises an error if logged in
    '''
    
    # is a user is logged in, if yes then fail
    #if request.user.is_authenticated:
    #    raise PermissionDenied
    
    # get the post data
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    instructor = (request.POST.get("choice") == "instructor")
    
    if User.objects.filter(email=email).exists():
        return render(request, 'app/new.html', {'error': 'Email already in use'})
    
    # return back if there is some kind of error
    if username is None or\
        email is None or\
        password is None or\
        request.POST.get("choice") is None:
        return render(request, 'app/new.html', {})
    
    # create and login
    user, uni_per = create_ac_user(username, email, password, instructor)
    login(request, user)
    
    user.save()
    uni_per.save()
    
    # return to index
    return render(request, 'app/index.html', {})
