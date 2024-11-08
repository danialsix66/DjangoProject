from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# ==============================
from django.conf import settings
from django.shortcuts import redirect


def error_404_view(request, exception):

	# we add the path to the the 404.html file
	# here. The name of our HTML file is 404.html
	return render(request, '404.html')

class Home(TemplateView):
    template_name = 'home.html'

class SignupView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url=reverse_lazy('login')

