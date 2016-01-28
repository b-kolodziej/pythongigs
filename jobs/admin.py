from django.contrib import admin

# Register your models here.
from .models import Company, Ad, KeySkill

admin.site.register(Company)
admin.site.register(Ad)
admin.site.register(KeySkill)