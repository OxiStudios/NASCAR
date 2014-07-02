__author__ = 'noah'
from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
        url(r'^driver/$', views.driver_home),
        url(r'^driver/(\d+)/$', views.driver),
        url(r'^test/', views.test),
        url(r'^test_2/', views.test_2),
        url(r'^home/', views.home_page),
        url(r'^input/racer/', views.input_racer)
)