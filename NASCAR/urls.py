from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'NASCAR.views.home', name='home'),
    url(r'^users/', include('Users.urls')),
    url(r'^main/', include('Data.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
