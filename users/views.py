from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from .models import Student
# Create your views here.
from users.forms import LoginForm


def redirect_to_profile(request):
    pass


def home(request):
    return render_to_response('loginform.html', {}, context_instance=RequestContext(request))


def login_handler(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print form.is_valid()
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print username
            print password
            stu_user = authenticate(username=username, password=password)
            login(request, stu_user)
            return render_to_response('login.html', {'message': "Welcome"}, context_instance=RequestContext(request))
        else:
            print 'fuckla'
            return render_to_response('logout.html', {'message': "form invalid"},
                                      context_instance=RequestContext(request))
    else:
        print 'fuckla'
        return render_to_response('logout.html', {'message': "method gandli"}, context_instance=RequestContext(request))


def logoutrequest(request):
    logout(request)
    return HttpResponseRedirect('/')
