from django.conf.urls import patterns, url
from graffiki_app import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^kml/$', views.KmlLink.as_view(), name='kmlFile'),
		url(r'^graffiti/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_graffiti, name='add_comment_to_graffiti'),
		url(r'^comment/(?P<pk>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),
		url(r'^comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),
		url(r'^parse/$', views.parse, name='parse'),
	)