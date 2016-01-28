from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from tinymce import models as tinymce_models

from constants import *

class Company(models.Model):
	name = models.CharField(max_length=120)
	city = models.CharField(max_length=120)
	about = tinymce_models.HTMLField()
	url = models.URLField()
	email = models.EmailField()
	contact_person = models.CharField(max_length=120)
	logo = models.ImageField()
	twitter = models.URLField()


	def __unicode__(self):
		return str(self.name)


	class Meta:
		verbose_name_plural = "Companies"




class KeySkill(models.Model):
	skill = models.CharField(max_length=200)


	def __unicode__(self):
		return str(self.skill)


class Ad(models.Model):
	# user = models.ForeignKey(User)
	title = models.CharField(max_length=200)

	description = tinymce_models.HTMLField()
	seniority = models.CharField(choices=SENIORITY, max_length=200)

	start_date = models.DateField()

	skill = models.ManyToManyField(KeySkill)
	remote = models.BooleanField()
	relocation = models.BooleanField()
	visa_sponsorship = models.BooleanField()
	salary_from = models.PositiveIntegerField()
	salary_to = models.PositiveIntegerField()
	currency = models.CharField(choices=CURRENCY, max_length=200)

	created = models.DateTimeField(auto_now=False, auto_now_add=True)
	expire = models.DateTimeField()
	# active = models.BooleanField(default=True)

	def __unicode__(self):
		return str(self.title)


