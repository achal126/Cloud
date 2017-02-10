from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from Cloud.settings import BASE_DIR
from django.shortcuts import render_to_response
#from myapp.forms import LoginForm
from django.contrib.auth import authenticate, login
from myapp.models import Login
import os
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response, redirect

#from django.contrib.auth import login as django_login, authenticate
from myapp.forms import AuthenticationForm
from myapp.models import Login
from .models import Login


def achal1(request):
    return render(request,"Azure_CP.html",{})


# def login(request):
#     username = "not logged in"
#     if request.method == "POST":
#         # Get the posted form
#         MyLoginForm = LoginForm(request.POST)
#
#         if MyLoginForm.is_valid():
#             username = MyLoginForm.cleaned_data['username']
#     else:
#         MyLoginForm = LoginForm()
#
#     return render(request,"User Registration.html",{})

# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = authenticate(email=request.POST['email'], password=request.POST['password'])
#             if user is not None:
#                 if user.is_active:
#                     django_login(request, user)
#                     return redirect('/cloud/bootstrap/docs/examples/signin/Azure_Cp.html/')
#     else:
#         form = AuthenticationForm()
#     return render(request,"User Registration.html")

# def login(request):
#     if request.method == 'POST':
#
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = authenticate(email=request.POST['Username'], password=request.POST['Password'])
#             if user is not None:
#                 a=1
#             else:
#                 HttpResponseBadRequest("Bad request")
#     return render(request, "User Registration.html")




# def login(request):
#     username = "not logged in"
#     print username
#     form = AuthenticationForm(request.POST)
#     print form.as_p()
#     # data= form['Password']
#     # print data
#     # print form.clean()
#     # print form.errors
#     # form.save()
#     # print form['Username'].data
#     # print form['Username'].value()
#     # print form.is_valid()
#     if form.is_valid():
#         username = request.POST.get('Username')
#         print username
#         print form['Username']
#         username = form.cleaned_data['Username']
#         username= form.clean_message()
#         print username
#         #password = form.cleaned_data['inputPassword']
#         print username
#         #print password
#     username_db= Login.objects.filter(email=username).exists()
#     print username_db
#     #password_db=Login.objects.filter(password=password)
#     if Login.objects.filter(email=username).exists():
#         return render(request, "User Registration.html")
#     else:
#         return HttpResponseBadRequest(username)



def login(request):
    username = "not logged in"
    print username

    if request.method == "POST":
        # Get the posted form
        MyLoginForm = AuthenticationForm(request.POST)

        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
            print username
    else:
        MyLoginForm = AuthenticationForm()
    if Login.objects.filter(email=username).exists():
        return render(request, 'User Registration.html', {"username": username})
    else:
        return HttpResponseBadRequest(username)
