from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    ### bilityab urls
    url(r'^$', 'bilityab.views.home'),
    url(r'^contact/$', 'bilityab.views.contact'),
    url(r'^about/$', 'bilityab.views.about'),
    url(r'^terms/$', 'bilityab.views.terms'),
    url(r'^FAQ/$', 'bilityab.views.FAQ'),

    ### account urls
    url(r'^profile/(?P<user_id>\d+)/$', 'account.views.profile_edit'),
    url(r'^profile/(?P<user_id>\d+)/favorites/$', 'account.views.favorites'),
    url(r'^profile/(?P<user_id>\d+)/favorites/(?P<event_id>\d+)/$', 'account.views.favorites_delete'),
    url(r'^charge/$', 'account.views.charge_user_bank'),
    url(r'^charge/(?P<user_id>\d+)/$', 'account.views.charge_user_balance'),
    url(r'^login/$', 'account.views.login'),
    url(r'^logout/$', 'account.views.logout'),
    url(r'^register/$', 'account.views.register'),
    url(r'^recover/$', 'account.views.recover'),
    url(r'^users/$', 'account.views.users'),
    url(r'^recover/(?P<random_num>[a-zA-z0-9!@#$%^&*()]+)/$', 'account.views.reset_password'),

    ### event urls
    url(r'^events/$', 'event.views.events'),
    url(r'^events/add/$', 'event.views.add_event'),
    url(r'^events/apply_edit/$', 'event.views.apply_event'),
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
    url(r'^organizers/$', 'event.views.all_organizer'),
    url(r'^organizer/(?P<organizer_id>\d+)/$', 'event.views.organizer'),
    url(r'^report/$', 'event.views.report'),
    url(r'^categories/$', 'event.views.categories'),
    url(r'^categories/add/$', 'event.views.add_category'),
    url(r'^categories/edit/(?P<category_id>\d+)/$', 'event.views.edit_category'),
    url(r'^categories/delete/(?P<category_id>\d+)/$', 'event.views.delete_category'),

    url(r'^add-comment/$', 'comment.views.add_comment'),

    ### search urls
    url(r'^search/$', 'event.views.search'),
    url(r'^search/ajax/$', 'event.views.ajax_search'),

    ### ticket urls
    url(r'^buy/$', 'ticket.views.buy'),
    url(r'^SalesChart/$', 'ticket.views.chart'),
    url(r'^ticket/(?P<user_id>\d+)/(?P<purchased_id>\d+)/$', 'ticket.views.ticket'),
    url(r'^ticket/(?P<user_id>\d+)/$', 'ticket.views.all_ticket'),

    ### promotion urls
    url(r'^promotions/$', 'promotion.views.all_promotion'),
    url(r'^promotion/(?P<event_id>\d+)/$', 'promotion.views.promotion'),

    url(r'^admin/', include(admin.site.urls)),

    ### serve media
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT
    }),
]