from django.forms import ModelForm
from django.contrib.auth.models import User
from domain.models import PreRegisterGraduated , PreRegisterAdmin


class RegisterFormGraduated(ModelForm):
	class Meta:
		model = PreRegisterGraduated
		fields=['first_name','last_name','email','dni','country','birthday','genre','career','graduation_year']

class RegisterFormAdmin(ModelForm):
	class Meta:
		model = PreRegisterAdmin
		fields=['first_name','last_name','email','dni','country','genre','cellphone']

