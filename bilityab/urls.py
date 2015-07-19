from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    ### bilityab urls
    url(r'^$', 'bilityab.views.home', name='home'),
    url(r'^events/$', 'bilityab.views.events', name='home'),
    url(r'^organizer/$', 'bilityab.views.organizer', name='home'),
    url(r'^contact/$', 'bilityab.views.contact', name='home'),
    url(r'^about/$', 'bilityab.views.about', name='home'),
    url(r'^terms/$', 'bilityab.views.terms', name='home'),
    # url(r'^blog/', include('blog.urls')),

    ### account urls
    url(r'^profile/(?P<user_id>\d+)/$', 'account.views.profile', name='home'),
    url(r'^profile/(?P<user_id>\d+)/charge/$', 'account.views.charge', name='home'),

    ### event urls
    url(r'^events/movie/(?P<event_id>\d+)/$', 'event.views.movie', name='home'),
    url(r'^events/sport/(?P<event_id>\d+)/$', 'event.views.sport', name='home'),
    url(r'^events/concert/(?P<event_id>\d+)/$', 'event.views.concert', name='home'),
    url(r'^events/entertainment/(?P<event_id>\d+)/$', 'event.views.entertainment', name='home'),
    url(r'^events/art/(?P<event_id>\d+)/$', 'event.views.art', name='home'),
    url(r'^organizer/(?P<organizer_id>\d+)/$', 'event.views.organizer', name='home'),
    url(r'^organizer/(?P<organizer_id>\d+)/add-event/$', 'event.views.add_event', name='home'),
    url(r'^organizer/(?P<organizer_id>\d+)/events/$', 'event.views.events', name='home'),
    url(r'^organizer/(?P<organizer_id>\d+)/events/(?P<event_id>\d+)/edit/$', 'event.views.edit_event', name='home'),
    url(r'^organizer/(?P<organizer_id>\d+)/events/(?P<event_id>\d+)/delete/$', 'event.views.delete_event', name='home'),

    ### ticket urls
    url(r'^buy/(?P<event_id>\d+)/$', 'event.views.buy', name='home'),
    url(r'^report/purchased/(?P<user_id>\d+)/(?P<purchased_id>\d+)/$', 'ticket.views.ticket', name='home'),

    ### promotion urls
    url(r'^promotion/(?P<promotion_id>\d+)/$', 'promotion.views.edit', name='home'),
    url(r'^promotion/add/$', 'promotion.views.add', name='home'),
    url(r'^promotion/(?P<promotion_id>\d+)/remove/$', 'promotion.views.remove', name='home'),

    ### report urls
    url(r'^report/purchased/(?P<user_id>\d+)/$', 'report.views.purchased', name='home'),
    url(r'^report/organized_events/(?P<user_id>\d+)/$', 'report.views.organized-events', name='home'),

    url(r'^admin/', include(admin.site.urls)),
]

