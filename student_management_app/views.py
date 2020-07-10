from django.contrib.auth import login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate

# Create your views here.
from student_management_app.EmailBackEnd import EmailBackEnd


def showDemoPage(request):
    return render(request, "demo.html")


def ShowLoginPage(request):
    return render(request, "login.html")


def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:

        user = EmailBackEnd.authenticate(request, username=request.POST.get("email"),password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            return HttpResponse("Email : " + request.POST.get("email") + " Password : " + request.POST.get("password"))
        else:
            return HttpResponse("Invalid id login")


def GetUserDetails(request):
    if request.user is not None:
        return HttpResponse("User : " + request.user.email + " Usertype :" + request.user.user_type)
    else:
        return HttpResponse("Please login First!!")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")
