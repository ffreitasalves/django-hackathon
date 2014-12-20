from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', 'core.views.home', name='home'),

    #Authentication views
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'registration/login.html',},
        name='login'
    ),

    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page':'home'},
        name='logout'
    ),

    url(r'^accounts/password_change/$', 'django.contrib.auth.views.password_change',
        {'template_name':'registration/password_change.html'},
        name='password_change'
    ),

    url(r'^accounts/password_change_done/$', 'django.contrib.auth.views.password_change_done',
        {'template_name':'registration/password_change_ok.html'},
        name='password_change_done'
    ),

    url(r'^accounts/password_reset/$', 'django.contrib.auth.views.password_reset',
        {},
        name='password_reset'
    ),

    url(r'^accounts/password_reset_done/$', 'django.contrib.auth.views.password_reset_done',
        {},
        name='password_reset_done'
    ),

    url(r'^accounts/password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm',
        {},
        name='password_reset_confirm'
    ),

    url(r'^accounts/password_reset_complete/$', 'django.contrib.auth.views.password_reset_complete',
        {},
        name='password_reset_complete'
    ),

    url(r'^admin/', include(admin.site.urls)),
)
