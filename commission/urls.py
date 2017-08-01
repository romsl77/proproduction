from django.conf.urls import url

from . import views

urlpatterns = [
	# shows index at /commission/
	url(r'^$', views.index, name='index'),
	# shows choosewagon at /commission/choosewagon
	url(r'^choosewagon/(?P<okdate>\d{4}-\d{2}-\d{2})/$', views.choosewagon, name='choosewagon'),
	# shows wagon at /commission/wagon/1
	url(r'^wagon/(?P<okdate>\d{4}-\d{2}-\d{2})/(?P<wagnumber>[0-9]+)/$', views.wagon, name='wagon'),
	# shows product at wagon /commission/id....
	url(r'^(?P<pid>.*)/$', views.product, name='product'),
	#define the url getdata that we have written inside form
	url(r'^getdata/', views.index),
	
	# shows index at /commission/drawing/d387975ef2964e908efbe7ba2af2181c
	#url(r'^wagon/(?P<cuuid>[0-9a-f-]+)/$', views.drawing, name='drawing'),
	# shows index at /commission/
	#url(r'^$', views.index, name='index'),
]
