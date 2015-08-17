import string
import random
import threading
from datetime import datetime
from datetime import timedelta
from django.contrib import auth
from bilityab.views import home
from ticket.models import PurchasedTicket
from smtplib import SMTPException
from django.shortcuts import render
from django.core.mail import send_mail
from django.template import loader, Context
from .check_registration import CheckRegistration
from account.models import CustomUser, RecoveryRequests
from django.http import HttpResponseForbidden, HttpResponse, HttpResponseRedirect


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
        if not errors.strip():
            birth_date = birth_date.split('/')
            CustomUser.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                           password=password, birth_date=datetime(int(birth_date[0]),
                                                                                  int(birth_date[1]),
                                                                                  int(birth_date[2])))
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return HttpResponse('success')
        else:
            return HttpResponse(errors)
    else:
        return HttpResponseForbidden('post required')


def profile_edit(request, user_id):
    if request.user.is_authenticated():
        if request.method == 'POST':
            if(request.POST.get('type', None)) == "edit-details-form":
                user = CustomUser.objects.get(id=user_id)
                user.first_name = request.POST.get('edit-first-name', None)
                user.last_name = request.POST.get('edit-last-name', None)
                user.birth_date = request.POST.get('edit-birthday', None)
                if (request.POST.get('edit-gender', None)) == "مرد":
                    user.gender = True
                else:
                    user.gender = False
                user.phone = request.POST.get('edit-phone', None)
                user.save()
            elif(request.POST.get('type', None)) == "edit-account-form":
                user = CustomUser.objects.get(id=user_id)
                user.username = request.POST.get('edit-username', None)
                user.email = request.POST.get('edit-email', None)
                if (request.user.check_password(request.POST.get('edit-password', None))):
                    if (request.POST.get('edit-new-password', None) == request.POST.get('edit-new-password-repeat', None)):
                        user.set_password(request.POST.get('edit-new-password', None))
                user.save()
            elif(request.POST.get('type', None)) == "delete-account-form":
                CustomUser.objects.filter(id=user_id).delete()
            return HttpResponseRedirect('/profile/'+str(request.user.id))
        else:
            return render(request, 'profile.html', {
                'ticketCount': len(PurchasedTicket.objects.filter(user_id=user_id)),
                'pageTitle': " - پروفایل کاربر",
            })
    else:
        return HttpResponseRedirect('/')


def charge(request, user_id):
    if request.user.is_authenticated():
        return render(request, 'charge.html', {
            'pageTitle': " - شارژ حساب کاربری",
        })
    else:
        return HttpResponseRedirect('/')


def favorites(request, user_id):
    if request.user.is_authenticated():
        return render(request, 'favorites.html', {
            'pageTitle': " - شارژ حساب کاربری",
        })
    else:
        return HttpResponseRedirect('/')


def favorites(request, user_id):
    if request.user.is_authenticated():
        return render(request, 'favorites.html', {
            'pageTitle': " - شارژ حساب کاربری",
        })
    else:
        return HttpResponseRedirect('/')

def charge_user_bank(request):
    if request.method == 'POST':
        price = request.POST.get('price')
        return render(request, 'charge-user-balance.html', {
            'pageTitle': " - خرید بلیط",
            'price': price,
        })
    else:
        return HttpResponseForbidden()


def charge_user_balance(request, user_id):
    if request.method == 'POST':
        user = CustomUser.objects.get(id=request.user.id)
        user.balance = user.balance + int(request.POST.get('price'))
        user.save()
        return HttpResponseRedirect('/profile/'+str(request.user.id))
    else:
        return HttpResponseForbidden()


def random_generator(size=6, chars=string.ascii_letters + string.digits + '!@$%^&*()'):
    return ''.join(random.SystemRandom().choice(chars) for _ in range(size))


def recover(request):
    if request.method == 'POST':
        email = request.POST.get('reset-email', None)
        if email:
            try:
                user = CustomUser.objects.get(email=email)
                RecoveryRequests.objects.filter(user=user).delete()
                random_num = random_generator(size=27)
                t = loader.get_template('reset-password.html')
                c = Context({
                    'user': user,
                    'random_num': random_num
                })
                try:
                    send_mail(subject='درخواست تغییر رمز عبور', message='', recipient_list=[email],
                              from_email='bilityab@sadrnezhaad.ir', fail_silently=False, html_message=t.render(c))
                    RecoveryRequests.objects.create(user=user, random_num=random_num)
                    set_disable_schedule(user)
                except SMTPException:
                    pass
            except CustomUser.DoesNotExist:
                pass
            return HttpResponse(1)
    else:
        return HttpResponseForbidden('post required')


def set_disable_schedule(user):
    now = datetime.now()
    run_at = now + timedelta(hours=24)
    delay = (run_at - now).total_seconds()
    threading.Timer(delay, disable_reset_password, [user]).start()


def reset_password(request, random_num):
    try:
        recovery_request = RecoveryRequests.objects.get(random_num=random_num)
        user = recovery_request.user
        new_password = random_generator(16)
        user.set_password(new_password)
        user.save()
        t = loader.get_template('new-password.html')
        c = Context({
            'user': user,
            'new_password': new_password
        })
        try:
            send_mail(subject='رمز عبور جدید', message='', recipient_list=[user.email],
                      from_email='bilityab@sadrnezhaad.ir', fail_silently=False, html_message=t.render(c))
        except SMTPException:
            pass
        recovery_request.delete()
        return home(request, 1)
    except RecoveryRequests.DoesNotExist:
        return HttpResponseRedirect('/')


def disable_reset_password(user):
    RecoveryRequests.objects.filter(user=user).delete()


def users(request):
    if request.user.is_superuser:
        if request.method == "POST":
            normal_users = request.POST.get('users[]', '')
            super_users = request.POST.get('superusers[]', '')
            for normal_user in normal_users:
                print(normal_user)
                user = CustomUser.objects.get(id=normal_user)
                user.is_organizer = 0
                user.save()
            for super_user in super_users:
                print(super_user)
                super_user = CustomUser.objects.get(id=super_user)
                super_user.is_organizer = 1
                super_user.save()
            return HttpResponseRedirect("/users/")
        else:
            return render(request, 'all_users.html', {
                'pageTitle': "- کاربران",
                'users': CustomUser.objects.all()
            })
    else:
        return HttpResponse("شما اجازه دسترسی به این صفحه را ندارید")
