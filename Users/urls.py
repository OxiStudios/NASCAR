__author__ = 'noah'

from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',

    url(r'settings/', views.settings),
    url(r'login/', views.user_login),
    url(r'signup/', views.signup),
    url(r'logout', views.user_logout),

)
