from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth


# Create your views here.
def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pas = request.POST['password']
        user=auth.authenticate(username=uname,password=pas)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"inavalid user")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method== 'POST':
        uname=request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        mail = request.POST['email']
        pas = request.POST['password']
        cpas = request.POST['confirm_password']
        if pas==cpas:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"username has already taken")
                return redirect('register')
            elif User.objects.filter(email=mail).exists():
                messages.info(request,"email has already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=uname, first_name=fname, last_name=lname, email=mail,
                                                password=pas)
                user.save();
                print("user created")
                return redirect('login')
        else:
            messages.info(request,'passwords not matching')
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
