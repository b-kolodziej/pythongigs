from django import forms

from .models import Ad, Company


class AdForm(ModelForm):
	class Meta:
		model = Ad

class CompanyForm(ModelForm):
	class Meta:
		model = Company

