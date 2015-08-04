from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    ### bilityab urls
    url(r'^$', 'bilityab.views.home'),
    url(r'^contact/$', 'bilityab.views.contact'),
    url(r'^about/$', 'bilityab.views.about'),
    url(r'^terms/$', 'bilityab.views.terms'),

    ### account urls
    url(r'^profile/(?P<user_id>\d+)/$', 'account.views.profile_edit'),
    url(r'^profile/(?P<user_id>\d+)/charge/$', 'account.views.charge'),

    url(r'^login/$', 'account.views.login'),
    url(r'^logout/$', 'account.views.logout'),
    url(r'^register/$', 'account.views.register'),

    ### event urls
    url(r'^events/$', 'event.views.events'),
    url(r'^events/add/$', 'event.views.add_event'),
    url(r'^events/delete/(?P<event_id>\d+)$', 'event.views.delete_event'),
    url(r'^events/rate/$', 'event.views.rate_event'),
    url(r'^events/sold_seats/$', 'event.views.get_sold_seats'),
    url(r'^events/buy_seats/$', 'event.views.buy_seats'),
    url(r'^events/(?P<event_id>\d+)/edit/$', 'event.views.edit_event'),
    url(r'^events/sport/$', 'event.views.all_sport'),
    url(r'^events/tourism/$', 'event.views.all_tourism'),
    url(r'^events/cinema/$', 'event.views.all_cinema'),
    url(r'^events/music/$', 'event.views.all_music'),
    url(r'^events/sport/(?P<event_id>\d+)/$', 'event.views.sport'),
    url(r'^events/tourism/(?P<event_id>\d+)/$', 'event.views.tourism'),
    url(r'^events/cinema/(?P<event_id>\d+)/$', 'event.views.cinema'),
    url(r'^events/music/(?P<event_id>\d+)/$', 'event.views.music'),
    url(r'^organizer/$', 'event.views.all_organizer'),
    url(r'^organizer/(?P<organizer_id>\d+)/$', 'event.views.organizer'),
    url(r'^report/$', 'event.views.report'),
    url(r'^categories/$', 'event.views.categories'),
    url(r'^categories/add/$', 'event.views.add_category'),
    url(r'^categories/delete/(?P<category_id>\d+)/$', 'event.views.delete_category'),


    ### ticket urls
    url(r'^buy/(?P<event_id>\d+)/$', 'ticket.views.buy'),
    url(r'^ticket/(?P<user_id>\d+)/(?P<purchased_id>\d+)/$', 'ticket.views.ticket'),
    url(r'^ticket/(?P<user_id>\d+)/$', 'ticket.views.all_ticket'),

    ### promotion urls
    url(r'^promotion/$', 'promotion.views.promotion'),

    url(r'^admin/', include(admin.site.urls)),

    ### serve media
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT
    })
]