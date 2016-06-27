from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name = 'home'),
	url(r'^(?P<poll_id>\d+)/$',views.view_poll),
	url(r'^add/$', views.add, name = 'add_poll'),
	url(r'^(?P<poll_id>\d+)/add_choices/$', views.add_choice, name = 'add_choice'),
	url(r'^all/$', views.view_polls, name = 'polls'),
	url(r'^(?P<poll_id>\d+)/vote/$', views.add_vote, name = 'vote'),
]