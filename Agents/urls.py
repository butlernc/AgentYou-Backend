__author__ = 'butlernc'

from django.conf.urls import url, patterns

import views

urlpatterns = patterns('',
        url(r'^create/', views.create),
)