from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import DataWork.urls
import Agents.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AgentYou.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'datawork/', include(DataWork.urls)),
    url(r'agents/', include(Agents.urls)),

)
