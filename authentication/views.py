from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User


# LOGIN VIEW ENDPOINT

def Login(request):
    if request.method == 'POST':
        etxt = request.POST['email']
        ptxt = request.POST['password']
        print('email:', etxt, 'password: ', ptxt)

        if etxt != "" and ptxt != "":
            user = authenticate(email=etxt, password=ptxt)

            if user != None:
                login(request, user)
                return redirect('posts')

    return render(request, 'login.html')


def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        print(username, first_name, last_name, email, password, password2)
        if password != password2:
            error = "Password not matched"
            return render(request, 'error.html', {'error': error})

        count1 = 0
        count2 = 0
        count3 = 0
        for i in password:
            if "0" < i < "9":
                count1 = 1
            if "A" < i < "Z":
                count2 = 1
            if "a" < i < "z":
                count3 = 1

        if count1 == 0 or count2 == 0 or count3 == 0:
            error = "Your Password Didn't Strong Enough"
            return render(request, 'error.html', {'error': error})

        if len(password) < 8:
            error = "Your Password Must be Greater Than 8 Characters"
            return render(request, 'error.html', {'error': error})

        if len(User.objects.filter(username=username)) == 0 and len(User.objects.filter(email=email)) == 0:
            user = User.objects.create_user(
                username=username, first_name=first_name, last_name=last_name, email=email, password=password)
        else:
            error = "User already exists"
            return render(request, 'error.html', {'error': error})

        return redirect('login_user')
    return render(request, 'register.html')



def Logout(request):
    logout(request)
    return redirect('posts')


def register(request):
    return render(request, 'register.html')
