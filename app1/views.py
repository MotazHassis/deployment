from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
import bcrypt

def start(request):
    return render(request,'index.html')
def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0 :
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
            
    else:
        hash1= bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        registered_user = User.objects.create(first=request.POST['fname'],last=request.POST['lname'],email=request.POST['email'],password=hash1)
        messages.success(request, "Registered successfully")
        request.session['user_id']=registered_user.id
        request.session['user_name']=registered_user.first
        return redirect('/success')
def login(request):
    user = User.objects.filter(email=request.POST['lemail'])
    if user:
        logged_user = user[0]
    if bcrypt.checkpw(request.POST['lpassword'].encode(), logged_user.password.encode()):
        request.session['user_id']=logged_user.id
        request.session['user_name']=logged_user.first
        messages.success(request, "Login successfully")
        return redirect('/success')
    else:
        messages.error(request,'Invalid authentication')
        return redirect ('/')
    
def success(request):
    if 'user_id' in request.session:
        context={
            'username':request.session['user_name']
        }
        return render(request,'welcome.html',context)
    else:
        return redirect ('/')
def logout(request):
    request.session.flush()
    return redirect('/')