from datetime import datetime

from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseForbidden, HttpResponse, HttpResponseRedirect

from .check_registration import CheckRegistration
from account.models import CustomUser

# Create your views here.


def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST.get('signin-username', ''),
                                 password=request.POST.get('signin-password', ''))
        if user is not None:
            auth.login(request, user)
            return HttpResponse(1)
        else:
            return HttpResponse(0)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(request.REQUEST.get('next', ''))


def register(request):
    if request.method == 'POST':
        errors = ''
        first_name = request.POST.get('signup-first-name', None)
        last_name = request.POST.get('signup-last-name', None)
        birth_date = request.POST.get('signup-birth-date', None)
        username = request.POST.get('signup-username', None)
        password = request.POST.get('signup-password', None)
        email = request.POST.get('signup-email', None)
        email = email.lower()
        errors += CheckRegistration.check_first_name(first_name) + ' '
        errors += CheckRegistration.check_last_name(last_name) + ' '
        errors += CheckRegistration.check_date(birth_date) + ' '
        errors += CheckRegistration.check_username(username) + ' '
        errors += CheckRegistration.check_pass(password) + ' '
        errors += CheckRegistration.check_email(email)
        print(errors)
        if not errors.strip():
            birth_date = birth_date.split('/')
            CustomUser.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                           password=password, birth_date=datetime(int(birth_date[0]),
                                                                                  int(birth_date[1]),
                                                                                  int(birth_date[2])))
            user = auth.authenticate(email=email, password=password)
            auth.login(request, user)
            return HttpResponse('success')
        else:
            return HttpResponse(errors)
    else:
        return HttpResponseForbidden('post required')


def profile_edit(request, user_id):
    if request.user.is_authenticated():
        return render(request, 'profile.html', {
            'logged_in': request.user.is_authenticated()
        })
    else:
        return HttpResponseRedirect('/')


def charge(request, user_id):
    if request.user.is_authenticated():
        return render(request, 'charge.html', {
            'logged_in': request.user.is_authenticated()

        })
    else:
        return HttpResponseRedirect('/')