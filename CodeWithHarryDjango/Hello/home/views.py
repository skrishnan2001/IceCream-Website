from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from .models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    context = {
        'variable1':"this is sent",
        'variable2':"test message"
    }
    messages.success(request, "Come and experience what actual ice cream tastes like.")
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def services2(request):
    return render(request, 'services2.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')

    return render(request, 'contact.html')

def signupUser(request):
    if request.method == 'POST':
        #Get the post parameters
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        # Check for erroneous inputs
        if len(username) > 15:
            messages.error(request, "Username must be less than 16 characters")
            return redirect("signup")

        if not username.isalnum():
            messages.success(request, "Username should only contain letters and numbers")
            return redirect("signup")

        if password != confirmpassword:
            messages.error(request, "Password and confirm password fields do not match")
            return redirect("signup")

        # Create the user
        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        messages.success(request, 'Your account has been created successfully!')
        return redirect("/")

    return render(request, 'signup.html')

def loginUser(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')

