from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', 'accounts.views.index', name='index'),
    url(r'^login/$', 'accounts.views.index', name='login'),
    url(r'^register/$', 'accounts.views.register', name='register'),
    url(r'^forgot_password/$', 'accounts.views.forgot_password', name='forgot_password'),
    url(r'^user_profile/$', 'accounts.views.user_profile', name='user_profile'),
    url(r'^change_password/$', 'accounts.views.change_password', name='change_password'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
