from django.conf.urls import url 
from . import views

app_name = 'show'

urlpatterns = [
	
	# index
	url(r'^$', views.IndexView.as_view(), name='index'),

	url(r'^about/$', views.AboutView.as_view(), name='about'),

	# form to add show
	url(r'^add/$', views.ShowCreate.as_view(), name='show-add'),

	# edit show
	#url(r'^(?P<show>[\w ]+)/edit/$', views.ShowUpdate.as_view(), name='show-update'),

	# delete show
	url(r'^(?P<show>[\w ]+)/delete/$', views.ShowDelete.as_view(), name='show-delete'),

	# signup
	url(r'^register/$', views.UserFormView.as_view(), name='register'),

	# login
	url(r'^login/$', views.LoginView.as_view(), name='login'),

	# logout
	url(r'^logout/$', views.LogoutView.as_view(), name='logout'),

	url(r'^error/$', views.ErrorView.as_view(), name='error'),

	url(r'^(?P<show>[\w ]+)/$', views.ShowDetail.as_view(), name='show-detail'),

	url(r'^(?P<show>[\w ]+)/addseason/$', views.AddSeason.as_view(), name='addseason'),

	url(r'^(?P<show>[\w ]+)/subtractseason/$', views.SubtractSeason.as_view(), name='subtractseason'),

	url(r'^(?P<show>[\w ]+)/addepisode/$', views.AddEpisode.as_view(), name='addepisode'),

	url(r'^(?P<show>[\w ]+)/subtractepisode/$', views.SubtractEpisode.as_view(), name='subtractepisode'),


]