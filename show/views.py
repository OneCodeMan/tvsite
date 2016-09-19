from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.detail import DetailView
from .models import Show
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View, TemplateView
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from .forms import UserForm
from django.shortcuts import get_object_or_404

class IndexView(generic.ListView):
	template_name = 'show/index.html'
	context_object_name = 'shows'

	def get_queryset(self):
		if self.request.user.is_authenticated():
			return Show.objects.filter(owner=self.request.user)
		else:
			return None

class AboutView(TemplateView):
	template_name = 'show/about.html'

class ShowDetail(DetailView):
	model = Show
	slug_field = "title"
	slug_url_kwarg = "show"
	template_name = 'show/show-detail.html'

class ShowCreate(CreateView):
	model = Show
	fields = ['title', 'description', 'season', 'episode']

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.owner = self.request.user
		instance.save()

		return redirect('show:index')
"""
class ShowUpdate(UpdateView):
	model = Show
	slug_field = 'title'
	slug_url_kwarg = 'show'
	fields = ['description', 'season', 'episode']
"""

class AddSeason(UpdateView):
	model = Show
	slug_field = 'title'
	slug_url_kwarg = 'show'
	fields = []

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.season += 1
		instance.save()

		return redirect('show:index')

class SubtractSeason(UpdateView):
	model = Show
	slug_field = 'title'
	slug_url_kwarg = 'show'
	fields = []

	def form_valid(self, form):
		instance = form.save(commit=False)
		if (instance.season > 0):
			instance.season -= 1
		else:
			instance.season = 0

		instance.save()

		return redirect('show:index')

class AddEpisode(UpdateView):
	model = Show
	slug_field = 'title'
	slug_url_kwarg = 'show'
	fields = []

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.episode += 1
		instance.save()

		return redirect('show:index')

class SubtractEpisode(UpdateView):
	model = Show
	slug_field = 'title'
	slug_url_kwarg = 'show'
	fields = []

	def form_valid(self, form):
		instance = form.save(commit=False)
		if (instance.episode > 0):
			instance.episode -= 1
		else:
			instance.episode = 0

		instance.save()

		return redirect('show:index')

class ShowDelete(DeleteView):
	model = Show
	slug_field = 'title'
	slug_url_kwarg = 'show'
	success_url = reverse_lazy('show:index')

class UserFormView(View):
	"""
	User sign up. Logs them in after sign up. (74)
	"""
	form_class = UserForm
	template_name = 'show/registration_form.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)

			username = form.cleaned_data['username']

			if not User.objects.filter(username=username).exists():
				password = form.cleaned_data['password']
				user.set_password(password)
				user.save()

				user = authenticate(username=username, password=password)

				if user is not None:

					if user.is_active:
						login(request, user)
						return redirect('show:index')
			else:
				return redirect('show:error')
		else:
			return redirect('show:error')


class LoginView(View):
	"""
	Log in already existing user
	"""
	form_class = UserForm
	template_name = 'show/registration_form.html'

	def get(self, request):
		form = self.form_class(None) 
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)

		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user is not None:

			if user.is_active:
				login(request, user)
				return redirect('show:index')
			else:
				return redirect('show:error')
		else:
			return redirect('show:error')

class LogoutView(View):

	def get(self, request):
		logout(request)
		return redirect('show:index')

class ErrorView(TemplateView):
	template_name = 'show/error.html'