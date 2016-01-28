from django.shortcuts import render

# Create your views here.
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView

from .forms import AdForm, CompanyForm
from .models import Ad, Contact


class AdView(FormView):
	template_name = "jobs/post.html"
	form_class = AdForm

	def post(self, request, *args, **kwargs):

    	form = self.form_class(request.POST)

    	if form.is_valid():
        	form.save(kwargs.get('pk'))
        else:
        	return self.form_invalid(form)


