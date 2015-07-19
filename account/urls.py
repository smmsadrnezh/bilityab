from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'bilityab.views.home', name='home'),
    url(r'^profile/(?P<user_id>\d+)/$', 'account.views.profile', name='home'),
    url(r'^profile/(?P<user_id>\d+)/charge/$', 'account.views.charge', name='home'),
]

