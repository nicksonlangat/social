from django.shortcuts import render
from django.views.generic import TemplateView, CreateView,UpdateView,DeleteView
from .models import Image
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.

class HomePageView(TemplateView):
	template_name="home.html"

class PostCreate(LoginRequiredMixin,CreateView):
	model= Image
	template_name="create.html"
	fields=["title", "image","description"]

	def form_valid(self,form):
		form.instance.user=request.user
		return super().form_valid(form)

class PostUpdate(LoginRequiredMixin,UpdateView):
	model= Image
	template_name="update.html"
	fields=["title", "image","description"]

class PostDelete(LoginRequiredMixin,DeleteView):
	model= Image
	template_name="delete.html"
	success_url=reverse_lazy("home")
