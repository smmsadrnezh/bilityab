from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    ### bilityab urls
    url(r'^$', 'bilityab.views.home'),
    url(r'^contact/$', 'bilityab.views.contact'),
    url(r'^about/$', 'bilityab.views.about'),
    url(r'^terms/$', 'bilityab.views.terms'),

    ### account urls
    url(r'^profile/(?P<user_id>\d+)/$', 'account.views.profile_edit'),
    url(r'^profile/(?P<user_id>\d+)/charge/$', 'account.views.charge'),

    ### event urls
    url(r'^events/$', 'event.views.events'),
    url(r'^events/add/$', 'event.views.add_event'),
    url(r'^events/sport/$', 'event.views.all_sport'),
    url(r'^events/tourism/$', 'event.views.all_tourism'),
    url(r'^events/art/$', 'event.views.all_art'),
    url(r'^events/sport/(?P<event_id>\d+)/$', 'event.views.sport'),
    url(r'^events/tourism/(?P<event_id>\d+)/$', 'event.views.tourism'),
    url(r'^events/art/(?P<event_id>\d+)/$', 'event.views.art'),
    url(r'^organizer/$', 'event.views.all_organizer'),
    url(r'^organizer/(?P<organizer_id>\d+)/$', 'event.views.organizer'),
    url(r'^organizer/(?P<organizer_id>\d+)/events/$', 'event.views.organizer_events'),
    url(r'^events/(?P<event_id>\d+)/edit/$', 'event.views.edit_event'),
    url(r'^report/$', 'event.views.report'),

    ### ticket urls
    url(r'^buy/(?P<event_id>\d+)/$', 'ticket.views.buy'),
    url(r'^ticket/(?P<user_id>\d+)/(?P<purchased_id>\d+)/$', 'ticket.views.ticket'),
    url(r'^ticket/(?P<user_id>\d+)/$', 'account.views.all_ticket'),

    ### promotion urls
    url(r'^promotion/(?P<promotion_id>\d+)/$', 'promotion.views.edit'),
    url(r'^promotion/add/$', 'promotion.views.add'),
    url(r'^promotion/(?P<promotion_id>\d+)/remove/$', 'promotion.views.remove'),

    url(r'^admin/', include(admin.site.urls)),
]