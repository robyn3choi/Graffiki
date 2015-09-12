"""graffiki_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from graffiki_app.views import ProfileImageIndexView
from django.conf.urls.static import static
from graffiki_app.views import ProfileImageView, ProfileDetailView
from . import settings
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('graffiki_app.urls')), # home page
    url(r'^accounts/login/$',  'django.contrib.auth.views.login'), # login page
	url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}), # logout page = home page
    url(r'^accounts/register/', 'graffiki_web.views.register_user'), # register page 
    url(r'^accounts/register_success/', 'graffiki_web.views.register_success'), # register success page

#image upload stuff
    url(r'^$', ProfileImageIndexView.as_view(), name='home'),
    url(r'^upload/', ProfileImageView.as_view(), name='profile_image_upload'),
    url(
    r'^uploaded/(?P<pk>\d+)/$', ProfileDetailView.as_view(),
    name='profile_image'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)