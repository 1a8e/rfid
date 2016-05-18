from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.scroll, name='scroll'),
	url(r'^scroll/(?P<scroll_id>[0-9A-F]{12})/details/$', views.detail, name='details'),
	url(r'^(?P<scroll_id>[0-9A-F]{12})$', views.publish, name='publish'),
]