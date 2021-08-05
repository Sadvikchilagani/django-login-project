from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from .models import Details

def home(request):
        return render(request,"pages/home.html")
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        birth = request.POST['birth']
        email = request.POST['email']
        p_number = request.POST['p_number']
        subject = request.POST['subject']
        location = request.POST['location']
        radio = request.POST['RADIO1']
        password = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST["username"]
        if password == password2:
            if User.objects.filter(username=username).exists():
                print("user taken")
                return render(request,"pages/register.html")
            elif User.objects.filter(email=email).exists():
                print("email taken")
                return render(request,"pages/register.html")
            else:
                user = User.objects.create_user(username=username, password=password, email=email,first_name=first_name, last_name=last_name)
                ins = Details(birth=birth, email=email, first_name=first_name, last_name=last_name,Radio=radio, p_number=p_number, location=location)
                user.save();
                ins.save()
                print("user created")
                return render(request,"pages/login.html")
    else:
        return render(request,"pages/register.html")
def login(request):
    if request.method=="POST":
        password = request.POST['password']
        username = request.POST["username"]
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return render(request,"pages/index.html")
        else:
            return render(request,"pages/login.html")

    else:
        return render(request,"pages/login.html")
def logout(request):
    auth.logout(request)
    return redirect("/")

# Create your views here.
