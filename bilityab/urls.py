from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'bilityab.views.home', name='home'),
    url(r'^events/$', 'bilityab.views.events', name='home'),
    url(r'^organizer/$', 'bilityab.views.organizer', name='home'),
    url(r'^contact/$', 'bilityab.views.contact', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]

