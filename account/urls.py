from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'bilityab.views.home', name='home'),
    url(r'^profile/(?P<user_id>\d+)/$', 'account.views.profile', name='home'),
    url(r'^profile/(?P<user_id>\d+)/charge/$', 'account.views.charge', name='home'),
]

